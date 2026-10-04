package js;

class JsCustomCallStack {
	public static function expandStackTraceLimit():Void {
		untyped js.Browser.window.Error.stackTraceLimit = 10000;
	}
}
