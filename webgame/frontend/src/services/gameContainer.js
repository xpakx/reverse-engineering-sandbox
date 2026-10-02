/**
 * @mock gameContainer
 * @origin 99881.js
 * @status mock
 * @purpose container service that prepares viewport/wrapper for Haxe
 * @globals ???
 */

const gameContainer = {
	element: null,

	init() {
		this.element = document.getElementById("flash-content");
		console.log("[GameContainer] Initialized. Target container:", this.element);

		if (this.element) {
			this.element.style.display = "block";
			this.element.style.position = "relative";
		} else {
			console.warn("[GameContainer] Warning: #flash-content not found in DOM yet!");
		}
	},
};

export default gameContainer;
