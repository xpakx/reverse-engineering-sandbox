/**
 * @module loaderEvents
 * @origin 56940.js
 * @purpose Event bus for game loader transitions & errors
 * @status mock
 * @globals ???
 */

class LoaderEvents {
	EVENT_HIDE_LOADER = "hide_loader";
	EVENT_SHOW_LOADER = "show_loader";
	EVENT_SHOW_ERROR = "show_error";

	constructor() {
		this.handlers = {};
	}

	on(event, handler) {
		this.handlers[event] ||= [];
		this.handlers[event].push(handler);
	}

	off(event, handler) {
		if (!this.handlers[event]) return;
		this.handlers[event] = this.handlers[event].filter(h => h !== handler);
	}

	emit(event, data) {
		console.log(`[LoaderEvents] EMIT: ${event}`, data || "");
		if (!this.handlers[event]) return;
		this.handlers[event].forEach(handler => handler(data));
	}
}

export default new LoaderEvents();
