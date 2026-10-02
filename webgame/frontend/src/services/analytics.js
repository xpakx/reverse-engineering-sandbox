/**
 * @module AnalyticsService
 * @origin 63279.js
 * @status mock
 * @purpose analytics
 * @globals ???
 */

class AnalyticsService {
	constructor() {
		this.isLocked = false;
	}

	log(eventName, payload = null) {
		console.log(`[Analytics] Event: ${eventName}`, payload || "");
	}

	subscribe(listeners, immediate = false) {
		console.log(`[Analytics] Subscribed to events:`, listeners, { immediate });
		if (immediate) {
			Object.values(listeners).forEach((callback) => typeof callback === "function" && callback());
		}
	}

	lock() {
		this.isLocked = true;
		console.log("[Analytics] Event dispatching locked");

		return () => {
			this.isLocked = false;
			console.log("[Analytics] Event dispatching unlocked");
		};
	}
}

export default new AnalyticsService();
