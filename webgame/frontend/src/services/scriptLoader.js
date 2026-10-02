/**
 * @module ScriptLoader
 * @origin 13633.js
 * @purpose Abstract script loader with retry logic, error reporting, and lifecycle hooks
 * @status deobfuscated
 * @globals ???
 */

// import sentry from "./errorLogger.js";       // 22186.js
// import { DebugLogger } from "./logger.js";   // 16797.js
import loaderEvents from "./loaderEvents.js"; // 56940.js
import { GameLoadingError } from "../constants/errors.js"; // 22473.js
import { GAME_PAGE_EVENT } from "../constants/gameEvents.js";
import analytics from "./analytics.js";

export default class ScriptLoader {
	static MAX_RETRY_ATTEMPTS = 3;

	constructor(clientType) {
		this.script = null;
		this.element = null;
		this.retryTimeout = null;
		this.retryCount = 0;
		this.isLoading = false;
		this.isLoaded = false;

		// this.logger = new DebugLogger(clientType);
		this.logger = console;
		this.onScriptLoaded = this.onScriptLoaded.bind(this);
		this.onScriptError = this.onScriptError.bind(this);
	}

	checkCanBeLoaded() {
		return !this.script && !this.isLoading && !this.isLoaded;
	}

	loadScript() {
		this.isLoading = true;
		this.script = document.createElement("script");
		this.script.addEventListener("load", this.onScriptLoaded);
		this.script.addEventListener("error", this.onScriptError);
		this.script.src = this.getScriptSrc();
		this.script.defer = true;
		document.head.appendChild(this.script);
	}

	onScriptLoaded() {
		this.logMetrics();
		try {
			this.init();
			this.retryCount = 0;
			this.isLoading = false;
			this.isLoaded = true;
			this.logger.log(`${this.getClientType()} loaded`);
		} catch (err) {
			this.handleError(GameLoadingError.INITIALIZATION, err);
		}
	}

	onScriptError() {
		this.handleError(GameLoadingError.SCRIPT);
	}

	handleError(errorType, errorObj = null) {
		this.retryCount++;

		if (this.retryCount < ScriptLoader.MAX_RETRY_ATTEMPTS) {
			loaderEvents.emit(loaderEvents.EVENT_SHOW_LOADER);
			this.logger.log(`Load attempt for ${this.getClientType()} #${this.retryCount} failed (${errorType}), retrying...`);
			this.cleanup();

			this.retryTimeout = setTimeout(() => {
				this.loadScript();
			}, 1000);
		} else {
			this.isLoading = false;
			this.logger.log(`All load attempts for ${this.getClientType()} failed`);
			this.logFinalError(errorType, errorObj);
			this.showError();
		}
	}

	logFinalError(errorType, errorObj) {
		const client = this.getClientType();
		const error = new Error();

		switch (errorType) {
			case GameLoadingError.SCRIPT:
				error.message = `Script load error: ${client}`;
				error.cause = errorObj;
				break;
			case GameLoadingError.INITIALIZATION:
				error.message = `Initialization error: ${client}`;
				error.cause = errorObj;
				break;
		}

		this.logger.log(error.message);
		// sentry.captureException(error); // TODO
	}

	cleanup() {
		if (this.script) {
			this.script.removeEventListener("load", this.onScriptLoaded);
			this.script.removeEventListener("error", this.onScriptError);
			this.script.remove();
			this.script = null;
		}

		if (this.retryTimeout) {
			clearTimeout(this.retryTimeout);
			this.retryTimeout = null;
		}
	}

	hide() {
		if (this.element) {
			this.element.style.visibility = "hidden";
		}
	}

	dispose() {
		this.isLoading = false;
		if (this.element?.remove) {
			this.element.remove();
			this.element = null;
		}
		this.cleanup();
	}

	showError() {
		loaderEvents.emit(loaderEvents.EVENT_SHOW_ERROR);
	}

	logMetrics() {
		analytics.log(GAME_PAGE_EVENT.game_client_loading, {
			refplace: window.NXAppInfo?.nxSource,
			userId: window.NXFlashVars?.uid,
			countryCode: window.NXFlashVars?.country_code,
			uniqSessionId: window.NXAppInfo?.visiting_uid,
			clientType: this.getClientType()
		});
	}

	getScriptSrc() {
		throw new Error("getScriptSrc() must be implemented");
	}

	getClientType() {
		throw new Error("getClientType() must be implemented");
	}

	init() {
		throw new Error("init() must be implemented");
	}
}
