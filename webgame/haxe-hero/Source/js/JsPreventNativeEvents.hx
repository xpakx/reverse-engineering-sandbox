package js;

import js.Browser;
import js.html.KeyboardEvent;
import js.html.MouseEvent;

class JsPreventNativeEvents {
	private static function getTarget():Dynamic {
		return Browser.window;
	}

	public static function preventArrowAndTabKeys():Void {
		var keyNames = ["Tab", "ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Left", "Right", "Up", "Down"];
		var keyCodes = [37, 39, 38, 40, 9];
		var target = getTarget();

		var handler = function(e:KeyboardEvent) {
			if (e.key != null) {
				if (keyNames.indexOf(e.key) != -1) {
					e.preventDefault();
				}
			} else if (keyCodes.indexOf(e.keyCode) != -1) {
				e.preventDefault();
			}
		};

		target.addEventListener("keydown", handler);
		target.addEventListener("keyup", handler);
		target.addEventListener("keypress", handler);
	}

	public static function enforceWindowFocusOnMouseDown():Void {
		var target = getTarget();

		target.addEventListener("mousedown", function(e:MouseEvent) {
				if (!Browser.document.hasFocus()) {
				Browser.window.focus();
				}
				e.preventDefault();
				});
	}
}
