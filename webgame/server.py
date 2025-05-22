from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import processors
from extractors.lib import prepareData
from repo.userdata import GameRepository
import os
from pathlib import Path
import time
import handlers


hash = '82048d36'
versioned_root = f'./{hash}'
logs = False
gameData = prepareData(hash)


class CustomHandler(SimpleHTTPRequestHandler):
    def handle_route(self, method):
        path = self.path.split('?')[0]
        print(path)

        for route_method, route_path, handler in self.server.routes:
            if method == route_method and path == route_path:
                try:
                    status, headers, body = handler(self)
                except Exception as e:
                    self.send_error(500, str(e))
                    return

                self.send_response(status)
                for key, value in headers.items():
                    self.send_header(key, value)
                self.end_headers()

                if isinstance(body, str):
                    body = body.encode('utf-8')
                self.wfile.write(body)
                return

        # No route found - serve files
        if method == 'GET':
            super().do_GET()
        else:
            self.send_error(404, f"Endpoint {path} not found")

    def translate_path(self, path):
        original_path = super().translate_path(path)

        if versioned_root == './':
            return original_path

        rel_path = os.path.relpath(original_path, start=os.getcwd())

        if rel_path in ['.', '/', 'favicon.ico', 'css/game-adaptive.css']:
            return original_path

        if 'assets/' in rel_path:
            if '.js' in rel_path and '.json' not in rel_path:
                rel_path = rel_path.replace('assets/', 'akamaihd/')
            else:
                versioned_path = os.path.join(
                        os.getcwd(), versioned_root, rel_path)
                versioned_asset = Path(versioned_path)
                if versioned_asset.exists():
                    return versioned_path
                return original_path

        versioned_path = os.path.join(os.getcwd(), versioned_root, rel_path)
        return versioned_path

    def do_GET(self):
        self.handle_route('GET')

    def do_POST(self):
        self.handle_route('POST')

    def do_PUT(self):
        self.handle_route('PUT')

    def do_DELETE(self):
        self.handle_route('DELETE')

    def log_request(self, code='-', size='-'):
        pass  # Suppresses the "GET /path HTTP/1.1" 200 - logs


class SimpleHTTPServerWithRoutes(HTTPServer):
    def __init__(self, server_address):
        super().__init__(server_address, CustomHandler)
        self.routes = []

    def add_route(self, method, path, handler):
        self.routes.append((method, path, handler))


def getDebugFile(debut):
    if not debug:
        return None
    with open('responseData/lyria.json', 'r') as file:
        debugFile = file.read()
    return debugFile


if __name__ == '__main__':
    processor = processors.RequestProcessor()
    debug = False
    debugFile = getDebugFile(debug)

    gameRepo = GameRepository(gameData)

    def api_handler(request_handler):
        responses = []

        try:
            content_length = request_handler.headers.get('Content-Length', 0)
            content_length = int(content_length)
            raw_body = request_handler.rfile.read(content_length)

            tempState = {
                'inventory': gameRepo.getInventoryByUserId(0),
                'heroes': gameRepo.getHeroesByUserId(0),
                'shops': gameRepo.getShopsByUserId(0),
            }

            body_data = json.loads(raw_body)
            if 'calls' in body_data:
                if debug and body_data['calls'][0]['name'] == 'registration':
                    return (
                            200,
                            {'Content-Type': 'application/json'},
                            debugFile
                        )
                for call in body_data['calls']:
                    data = processor.process(call, gameRepo, gameData)
                    if data:
                        responses.append(data)
            else:
                data = processor.process(body_data, gameRepo, gameData)
                if data:
                    responses.append(data)
        except ValueError:
            return (
                    400,
                    {'Content-Type': 'text/plain'},
                    'Invalid Content-Length'
                )
        except Exception as e:
            print(f'Error: {str(e)}')
            return (
                    500,
                    {'Content-Type': 'text/plain'},
                    f'Error: {str(e)}'
                )
        resp = {}
        resp['date'] = int(time.time())
        resp['results'] = responses

        response = json.dumps(resp)
        print("RESPONSE CREATED")
        return (200, {'Content-Type': 'application/json'}, response)

    server = SimpleHTTPServerWithRoutes(('localhost', 8081))
    server.add_route('GET', '/api/clientStat/', handlers.stash_handler)
    server.add_route('POST', '/api/', api_handler)
    server.add_route('POST', '/client-tech-logs', handlers.logs_handler)
    server.add_route(
            'POST', '/api/onesignal-token.php', handlers.success_handler)
    server.add_route('POST', '/get_currencies', handlers.currencies_handler)
    server.add_route('POST', '/chat/get_info', handlers.info_handler)
    server.add_route('POST', '/landing_loaded', handlers.landing_handler)

    print("Starting server on http://localhost:8000")
    server.serve_forever()
