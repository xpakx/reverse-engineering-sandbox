package;

import openfl.display.Sprite;
import openfl.events.Event;
import openfl.net.URLRequestDefaults;
import loader.web.GameStart;
// import loader.web.util.GameLoadingDurationLogger;
import engine.loader.ClientVersion;
// import js.JsFullscreenAlignmentFix;
// import js.JsPakoCompression;
// import js.JsMouseWheelHandler;
import js.JsPreventNativeEvents;
// import js.JsFullscreenEventHandler;
import js.JsCustomCallStack;
// import com.progrestar.common.util.ExternalInterfaceProxy;

class Main extends Sprite {

    public function new() {
	    super(); // Ah.call(this);

	    // GameLoadingDurationLogger.start(); // nU.start();
	    // URLRequestDefaults.idleTimeout = 180000; // vU.ALd = 18E4;

	    js.Browser.console.log(
			    "%cgame:" + ClientVersion.getVersion(),  // qy.wIj()
			    "color: #888; background: #aaaaaa33;"
	    );

	    // JsFullscreenAlignmentFix.init(); // Ikc.init();
	    // JsPakoCompression.init(); // ulc.init();
	    // JsMouseWheelHandler.init(); // Skc.init();

	    JsPreventNativeEvents.preventArrowAndTabKeys(); // q9.MKn();
	    JsPreventNativeEvents.enforceWindowFocusOnMouseDown(); // q9.NKn();

	    // JsFullscreenEventHandler.init(); // Bt.init();
	    JsCustomCallStack.expandStackTraceLimit(); // Ft.apn();
	    // ExternalInterfaceProxy.init(); //  Yc.init();

	    this.addEventListener(Event.ADDED_TO_STAGE, runGame);
    }

    private function runGame(event:Event) {
            var gameStart = new GameStart(this.stage);
	    gameStart.start();
    }
}
