/**
 * @module AnalyticsService
 * @origin 63279.js
 * @status mock
 * @purpose analytics
 * @globals ???
 */

class AnalyticsService {
	log(eventName, payload = null) {
		console.log(`[Analytics] Event: ${eventName}`, payload || "");
	}

	subscribe(listeners, immediate = false) {
		console.log(`[Analytics] Subscribed to events:`, listeners, { immediate });
		if (immediate) {
			Object.values(listeners).forEach((callback) => typeof callback === "function" && callback());
		}
	}
}

export default new AnalyticsService();
