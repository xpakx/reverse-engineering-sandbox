 /**
 * @module HeroLoader
 * @origin 41480.js
 * @purpose Boots the Hero Wars Haxe/Lime OpenFL engine
 * @status deobfuscated
 * @globals ???
 */

import loaderEvents from "./loaderEvents.js";
import ScriptLoader from "./scriptLoader.js";

class HeroLoader extends ScriptLoader {
	constructor() {
		super("client");
		this.WRAPPER_SELECTOR = "flash-content";
		this.element = null;
	}

	load() {
		this.logger.log("client loading");

		if (this.checkCanBeLoaded()) {
			this.retryCount = 0;
			this.loadScript();
		}
	}

	getScriptSrc() {
		return window.NXFlashVars.preloader_js;
	}

	getClientType() {
		return "main";
	}

	init() {
		this.element = document.getElementById(this.WRAPPER_SELECTOR);
		loaderEvents.emit(loaderEvents.EVENT_HIDE_LOADER);
		document.documentElement.classList.add("game_ready");
		this.element.innerHTML = "";
		this.element.style.visibility = "visible";

		window.lime.embed("heroeshx", this.WRAPPER_SELECTOR, 0, 0, {
			parameters: {}
		});

		window.nxg.setFlashMovie(window.thisMovie("flash-app"));
	}

	show() {
		if (this.element) {
			this.element.style.visibility = "visible";
		}
	}
}

export default new HeroLoader();
