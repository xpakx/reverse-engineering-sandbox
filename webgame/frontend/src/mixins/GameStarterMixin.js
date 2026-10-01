/**
 * @mixin GameStarterMixin
 * @purpose Triggers game boot sequence on mount and tracks user registration state
 * @status deobfuscated
 * @origin 20875.js
 * @globals ???
 */

import GameBootstrapper from "../services/gameBootstrapper.js";

export default {
	name: "GameStarterMixin",

	data() {
		return {
			isNewUserRegistered: window.NXUserInfo?.is_new_user_registered,
			isDelayedRegistration: window.NXUserInfo?.is_delayed_registration
		};
	},

	mounted() {
		this.startGame();
	},

	computed: {
		isNewUser() {
			return this.isNewUserRegistered === "1";
		},
		isDelayedUser() {
			return this.isDelayedRegistration === 1;
		},
		isNewOrDelayedUser() {
			return this.isNewUser || this.isDelayedUser;
		}
	},

	methods: {
		startGame() {
			GameBootstrapper.run();
		}
	}
};
