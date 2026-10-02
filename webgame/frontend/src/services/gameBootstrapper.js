/**
 * @module gameBootstrapper
 * @origin 20875.js
 * @purpose Initializes dependencies, complies with AntiAddiction, and triggers Haxe loader
 * @status deobfuscated
 * @globals window.thisMovie, window.NXF.callClientFunction,
 *          window.apiWrapper, window.NXFlashVars, window.NXUserInfo
 *          window.NXSDK, window.FB
 */

// sideeffect: 27622; ???
import analytics from "./analytics.js";
import heroLoader from "./heroLoader.js"; // !IMPORTANT
import gameContainer from "./gameContainer.js";
// import playableModal from "./playableModal.js"; // 56349.js
// import playableController from "./playableController.js"; // 29638.js
import { PAGE_EVENT } from "../constants/pageEvents.js";
import { GAME_PAGE_EVENT } from "../constants/gameEvents.js";

// sideeffects:
// 20496; window.nxg seems ot be set up here, specifically flashGate, some callbacks etc
// 42297;; nxg have Pushd4Client set up here


window.thisMovie = function (movieName) {
	if (navigator.appName.indexOf("Microsoft") !== -1) {
		return window[movieName];
	}
	return document[movieName];
};

// RPC???
window.NXF = {
  callClientFunction(methodName, payload) {
	  const movie = window.thisMovie("flash-app");
	  if (movie && typeof movie[methodName] === "function") {
		  movie[methodName](payload);
	  }
  }
};

// ??
window.apiWrapper = function (e, t, n, r, callbackName) {
	if (typeof FB === "undefined") {
		const movie = window.thisMovie("flash-app");
		if (movie && typeof movie[callbackName] === "function") {
			movie[callbackName]();
		}
		return false;
	}
};

function launchGame(unlockAnalytics) {
	gameContainer.init();

	if (window.NXFlashVars?.playable) {
		// playable version; mini-game?
		playableController.init();
		playableModal.show();
	} else {
		// normal game mode
		heroLoader.load();
	}

	unlockAnalytics?.();
	analytics.log(GAME_PAGE_EVENT.game_init);
}

export async function run() {
	const antiAddictionService = window.NXSDK?.Auth?.Services?.AntiAddictionService;
	const unlockAnalytics = analytics.lock();

	// this is ver messy code in the original, 
	// so not sure if this is correctly reversed
	// but that seems to be an anti-addiction compliance,
	// so we don't really need it 
	if (window.NXUserInfo?.antiAddiction && antiAddictionService) {
		unlockAnalytics();
		await antiAddictionService.start(window.NXUserInfo.antiAddiction);
		analytics.log(PAGE_EVENT.button_click, {
			mode: "game",
			button: "AntiAddiction:game::start"
		});
	}

	launchGame(unlockAnalytics);
}

export default { run };
