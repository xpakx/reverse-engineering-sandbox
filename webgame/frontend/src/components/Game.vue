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

	 import { CommunityService } from "../services/communityService.js";
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

	 const isGeoBlockedCountry = [].includes(window.NXUserInfo?.geoip_Country_Code);
	 // == false, minification artifact?

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

			 // TODO: import tests
			 console.log("backgroundCssClass:", this.backgroundCssClass);
			 console.log("menuIsVisible:", this.menuIsVisible);
			 console.log("profileIsVisible:", this.profileIsVisible);
			 console.log("supportButtonCssClass:", this.supportButtonCssClass);
			 console.log("moreButtonCssClass:", this.moreButtonCssClass);
			 // console.log("supportOrMoreButtonCssClass:", this.supportOrMoreButtonCssClass);

			 // console.log("createLoginIsVisible:", this.createLoginIsVisible);
			 // console.log("createLoginButtonCssClass:", this.createLoginButtonCssClass);
			 console.log("currencyDropdownDisabled:", this.currencyDropdownDisabled);
			 // console.log("subscribeNewsManageLoading:", this.subscribeNewsManageLoading);
			 // console.log("subscribeNewsButtonCssClass:", this.subscribeNewsButtonCssClass);
			 // console.log("subscribeNewsIsShow:", this.subscribeNewsIsShow);
			 console.log("promoCodesBlockIsVisible:", this.promoCodesBlockIsVisible);
		 },

		 computed: {
			 backgroundCssClass() {
				 return `bg_color_${UserInfo.background_id}`;
			 },

			 menuIsVisible() {
				 return this.sidebarMode === SIDEBAR_MODE_MENU && Boolean(this.sidebarIsVisible);
			 },

			 profileIsVisible() {
				 return this.sidebarMode === SIDEBAR_MODE_PROFILE && Boolean(this.sidebarIsVisible);
			 },

			 supportButtonCssClass() {
				 return {
					 waiting: this.supportModalButtonIsWaiting,
					 badge: this.supportModalButtonIsBadge
				 };
			 },

			 moreButtonCssClass() {
				 return {
					 badge: CommunityService.notificatorIsVisible
				 };
			 },

			 supportOrMoreButtonCssClass() {
				 return {
					 badge: (
						 CommunityService.notificatorIsVisible || 
						 this.supportModalButtonIsBadge || 
						 NotificationBadgeService.state.isShown // TODO: mock
					 )
				 };
			 },

			 createLoginIsVisible() {
				 return createLoginState.isEnabled; // TODO: mock
			 },

			 createLoginButtonCssClass() {
				 return {
					 badge: createLoginState.firstOpenClick
				 };
			 },

			 currencyDropdownDisabled() {
				 return this.manageCurrencyLoading || isGeoBlockedCountry; // TODO: mixin
			 },

			 subscribeNewsManageLoading() {
				 return UserService.updateUserStatePromise; // TODO: mock
			 },

			 subscribeNewsButtonCssClass() {
				 return {
					 waiting: this.subscribeNewsManageLoading
				 };
			 },

			 subscribeNewsIsShow() {
				 return getSubscribeNewsNewsletter(); // TODO: mock
			 },

			 promoCodesBlockIsVisible() {
				 return window.NXAppInfo?.isPromoCodesEnabled;
			 }
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
