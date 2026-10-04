package loader.web;

import openfl.display.Stage;

class GameStart {
	public var stage:Stage;

	public function new(stage:Stage) {
		this.stage = stage;
	}

	public function start():Void {
		js.Browser.console.log("[GameStart] Stub started");
	}
}
