/**
 * @module Game
 * @origin 97867.js
 * @status mock / deobfuscation in progress
 * @purpose Game shell
 * @globals NXIsDelayedUser, NXShowDelayedFormSignup, NXShowConfirmEmail, NXAppInfo, NXFlashVars
 */

 // TODO: original uses inline templates
 <template>
	 <div class="game-container">
		 <h2>Game Canvas / Wrapper Component</h2>
		 <p>Mock Component</p>
		 <Game-Loader></Game-Loader>
		 <Game-Settings></Game-Settings>
		 <Profile></Profile>
		 <Promo-Codes-Block></Promo-Codes-Block>
	 </div>
 </template>

 <script>
	 import OuterClickDirective from "../directives/outerClick.js";
	 import AutofocusDirective from "../directives/autofocus.js";

	 import Profile from "./Profile.vue";
	 import UseSprite from "./UseSprite.vue";
	 import GameSettings from "./GameSettings.vue";
	 import PromoCodesBlock from "./PromoCodesBlock.vue";
	 import GameLoader from "./GameLoader.vue";

	 import { UserInfo } from "../services/userService.js";
	 import {
		 logEnabledSubscribeNews,
	 } from "../services/newsletterService.js";
	 import createLoginModal from "../services/createLoginModal.js";

	 const SIDEBAR_MODE_MENU = "menu";
	 const SIDEBAR_MODE_PROFILE = "profile";

	 export default {
		 name: "Game",

		 // TODO: mixins

		 components: {
			 Profile,
			 UseSprite,
			 GameSettings,
			 PromoCodesBlock,
			 GameLoader
		 },

		 directives: {
			 outerClick: OuterClickDirective,
			 autofocus: AutofocusDirective
		 },

		 data() {
			 return {
				 userInfo: UserInfo,
				 appInfo: window.NXAppInfo || {},
				 flashInfo: window.NXFlashVars || {},

				 sidebarIsVisible: false,
				 sidebarMode: SIDEBAR_MODE_MENU,

				 cookiesSettingsIsVisible: true, // TODO
				 cookiesCanBeChanged: true, // TODO

				 supportModalButtonIsWaiting: false,
				 supportModalButtonIsBadge: false,

				 langDropdownVisible: false,
				 langDropdownStyle: {},
				 landDropdownResizeDispose: null,

				 currencyDropdownVisible: false,
				 currencyDropdownStyle: {},
				 currencyDropdownResizeDispose: null,

				 impressumDropdownVisible: false,
				 impressumDropdownStyle: {},
				 impressumDropdownResizeDispose: null,
			 };
		 },

		 mounted() {

			 logEnabledSubscribeNews(false, true);
			 createLoginModal?.showInfoIfRequired?.();

			 // TODO
			 /**
			 unk_sidebar1.externalMethods = unk_sidebar1.externalMethods || {};
			 unk_sidebar1.externalMethods.hideSidebar = () => {
				 this.hideCurrencyList();
				 this.hideSidebar();
			 };

			 // maybe some kind of language sidebar?
			 unk_sidebar2.externalMethodsLanguage = unk_sidebar2.externalMethodsLanguage || {};
			 unk_sidebar2.externalMethodsLanguage.hideDropdown = () => {
				 this.hideLangDropdown();
			 };
			 unk_sidebar2.externalMethodsLanguage.hideSidebar = () => {
				 this.hideCurrencyList();
				 this.hideSidebar();
			 };

			 unk1?.init?.();
			 unk2?.init?.();
			 */

			 window.NXIsDelayedUser = this.isRegistrationUser;
			 window.NXShowDelayedFormSignup = this.showFormPopupType;
			 window.NXShowConfirmEmail = this.showConfirmEmail;
		 },

		 computed: {
			 // TODO
		 },

		 methods: {
			 // TODO
		 }
	 };
 </script>

 <style scoped>
.game-container {
	padding: 2rem;
	border: 2px dashed #42b883;
	text-align: center;
	margin: 2rem auto;
	max-width: 600px;
}
 </style>
