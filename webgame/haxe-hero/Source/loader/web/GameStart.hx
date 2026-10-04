package loader.web;

import openfl.display.Stage;
import openfl.display.StageAlign;
import openfl.display.StageScaleMode;
import engine.context.GameRenderMode;

// import loader.web.GameStartRouter;
// import engine.core.Deferred;
// import engine.core.utils.thread.ProgressBarDataProvider;
// import loader.web.GameStartLogger;
// import engine.core.utils.thread.ThreadQueue;
// import loader.web.view.PreloaderView;
// import loader.web.MultipleClientsBridge;
// import game.mechanics.preloader_overlay.OverlayPlayableBridge;
// import game.mechanics.hero_chooser.HeroScrollerBridge;
// import game.mechanics.epic_start.EpicStartPlayableBridge;


import js.Browser;

class GameStart {
	public var stage:Stage;

	public var flashVars:Dynamic; // Bf
    
	// Internal Promise / Deferred objects (Ia in JS)
	public var readyPromise:Dynamic;  // PGb
	public var initPromise:Dynamic;   // b9b



	public function new(stage:Stage) {
		this.stage = stage;

		// this.gameStartRouter = new GameStartRouter(); // oJf
		// this.unk_deferred1 = new Deferred(); // PGb
		// this.unk_deferred2 = new Deferred(); // b9b
		// this.progressBarDataProvider = new ProgressBarDataProvider(); / rvi
		// this.gameStartLogger = new GameStartLogger(); // lj
		// this.threadQueue = new ThreadQueue(); // TDb

		this.flashVars = Reflect.field(js.Browser.window, "NXFlashVars"); // Bf

		var isWeb = (this.flashVars.platformNetwork == "web");
		trace(isWeb);
		// this.preloaderView = new PreloaderView(stage, this.flashVars.interface_lang, isWeb); // h1

		// dm.F().xg(!0); // F()  looks like getSingleton or sth???
		// dm.j = "loader.web.MultipleClientsBridge";
		// this.overlayPlayableBridge = new OverlayPlayableBridge(r.u(window, "NXPlayableApi"), this.gameStartLogger.TL); // Czc

		// this.overlayPlayableBridge.register(new HeroScrollerBridge(this.threadQueue, this.unk_deferred1));
		// this.overlayPlayableBridge.register(new EpicStartPlayableBridge(this.preloaderView))
	}

	public function start():Void {
		js.Browser.console.log("[GameStart] Stub started");
	}
}
