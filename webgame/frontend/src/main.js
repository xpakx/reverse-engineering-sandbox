/**
 * @module main
 * @origin 85699.js
 * @status deobfuscated
 * @purpose Entry point of the whole app
 * @globals window.NXShowPaymentBox, window.is_game_loaded
 */

import { createApp } from "vue";
import Game from "./components/Game.vue"; // !IMPORTANT

import "./mocks/windowGlobals.js";

import analytics from "./services/analytics.js";
import { GAME_PAGE_EVENT, PUSHD_EVENT } from "./constants/gameEvents.js";
import { PAGE_EVENT } from "./constants/pageEvents.js";
import { UserService } from "./services/userService.js";
import gameSdk from "./services/gameSdk.js";
import paymentModule from "./services/payment.js";


// sideeffect: 81324; prolly polyfill-related?
// sideeffect: 67262; prolly polyfill-related?
// sideeffect: 18290; looks like production/dev check, and devtools setting
// sideeffect: 65693; more window patching, ToS links
// sideeffect: 20496; ??? seems somehow important, sth flash related? !IMPORTANT
// sideeffect: 42297; sth related to websocket
// sideeffect: 96110; sth related to pwa

window.is_game_loaded = false;
window.NXShowPaymentBox = paymentModule.show;

function markGameAsLoaded() {
	window.is_game_loaded = true;
	console.log("[State] window.is_game_loaded set to true");
}

const app = createApp(Game);
app.mount("#app");

window.addEventListener("load", () => {
	analytics.log(GAME_PAGE_EVENT.game_launch);

	if (window.NXUserInfo.is_new_user_registered) {
		analytics.log(GAME_PAGE_EVENT.account_created);

		if (!window.NXUserInfo.is_delayed_registration) {
			analytics.log(GAME_PAGE_EVENT.simple_registration, {
				socialNetwork: window.NXUserInfo.social_network
			});
		}
	}

	if (window.NXUserInfo.isNewUserRegistered24h) {
		analytics.log(GAME_PAGE_EVENT.account_created_today);
	}
});

// we prolly don't care about PWA
window.pagelive.onAppInstall(() => {
	analytics.log(PAGE_EVENT.button_click, { button: "onAppInstall", mode: "pwa" });
});

window.pagelive.onAppShowPromt(() => {
	analytics.log(PAGE_EVENT.button_click, { button: "onAppShowPromt", mode: "pwa" });
});

window.pagelive.onAppPromtAccepted(() => {
	analytics.log(PAGE_EVENT.button_click, { button: "onAppPromtAccepted", mode: "pwa" });
});

window.pagelive.onAppPromtDismiss(() => {
	analytics.log(PAGE_EVENT.button_click, { button: "onAppPromtDismiss", mode: "pwa" });
});

analytics.subscribe({
	[PUSHD_EVENT.registration]: markGameAsLoaded,
	[PUSHD_EVENT.login]: markGameAsLoaded
}, true);

// we prolly don't care about that either, bc this is A/B testing apparently
// might remove later for simplification
if (!window.NXUserInfo.groupNumber) {
	const actionTimestamp = performance.now() || 0;
	const userGroupNumber = ("00" + window.NXUserInfo.user_id).slice(-2);

	analytics.log(GAME_PAGE_EVENT.user_retargeting, userGroupNumber);
	window.NXFlashVars.userState.groupNumber = userGroupNumber;

	UserService.updateUserState({
		context: {
			actionTs: actionTimestamp
		}
	});
}

gameSdk.init("game");
