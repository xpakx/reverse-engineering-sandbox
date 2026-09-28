/**
 * @module userService
 * @origin 21407.js
 * @status mock
 * @purpose service for user actions/state
 * @globals ???
 */

export const UserService = {
	updateUserState(payload) {
		console.log("[UserService] updateUserState:", payload);
	}
};

export const UserInfo = {
	constructor(data = {}) {
		this.is_delayed_registration = !!data.is_delayed_registration;
	}
};
