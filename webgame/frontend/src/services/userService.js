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
	is_delayed_registration: Boolean(window.NXUserInfo?.is_delayed_registration), // TODO: ???
	background_id: "dark",
};
