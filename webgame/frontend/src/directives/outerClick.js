/**
 * @module outerClick
 * @origin 60753.js
 * @status mock
 * @purpose directive for clicking outrside of element
 * @globals None
 */

export default {
	mounted(el, binding) {
		el.__outerClick__ = (event) => {
			if (!(el === event.target || el.contains(event.target))) {
				binding.value(event);
			}
		};
		document.addEventListener("click", el.__outerClick__);
	},
	unmounted(el) {
		document.removeEventListener("click", el.__outerClick__);
	}
};
