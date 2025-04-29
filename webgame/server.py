from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import processors
from extractors.lib import prepareData
from controllers.items import getTestInventory
import os

versioned_root = './91c10ca0'
logs = False
gameData = prepareData()
tempState = {
        'inventory': getTestInventory()
        }


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


if __name__ == '__main__':
    processor = processors.RequestProcessor()

    def api_handler(request_handler):
        responses = []

        try:
            content_length = int(request_handler.headers.get('Content-Length', 0))
            raw_body = request_handler.rfile.read(content_length)

            body_data = json.loads(raw_body)
            if 'calls' in body_data:
                for call in body_data['calls']:
                    data = processor.process(call, tempState, gameData)
                    if data:
                        responses.append(data)
            else:
                data = processor.process(body_data, tempState, gameData)
                if data:
                    responses.append(data)
            # print(body_data)
        except ValueError:
            return (400, {'Content-Type': 'text/plain'}, 'Invalid Content-Length')
        except Exception as e:
            return (500, {'Content-Type': 'text/plain'}, f'Error: {str(e)}')
        resp = {}
        resp['date'] = 1745545330.034689
        resp['results'] = responses

        response = json.dumps(resp)
        print("RESPONSE CREATED")
        return (200, {'Content-Type': 'application/json'}, response)

    def stash_handler(request_handler):
        return (
            200,
            {'Content-Type': 'application/json'},
            '{error: 0}'
        )

    def logs_handler(request_handler):
        print('error')
        if logs:
            content_length = int(request_handler.headers.get('Content-Length', 0))
            raw_body = request_handler.rfile.read(content_length)
            print(raw_body)
        return (
            200,
            {'Content-Type': 'application/json'},
            '{error: 0}'
        )

    server = SimpleHTTPServerWithRoutes(('localhost', 8081))
    server.add_route('GET', '/api/clientStat/', stash_handler)
    server.add_route('POST', '/api/', api_handler)
    server.add_route('POST', '/client-tech-logs', logs_handler)

    print("Starting server on http://localhost:8000")
    server.serve_forever()
