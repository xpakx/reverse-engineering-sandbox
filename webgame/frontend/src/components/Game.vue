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

			 // setSubsribeNewsNewsletter(false, true); // TODO: mock mixin
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

			 buttonSubscribeNews(event) {
				 logEnabledSubscribeNews(true, true);
				 sendSubscribeNews(event); // TODO: mock
			 },

			 userLockLogout() {
				 UserService.logout(); // TODO: mock
			 },

			 isRegistrationUser() {
				 return UserService.UserInfo.is_delayed_registration;
			 },

			 showLanguagesDropdown(event) {
				 LanguageModal.show(event); // TODO: mock
			 },

			 openSupportModal() {
				 if (this.supportModalButtonIsWaiting) return;
				 this.supportModalButtonIsWaiting = true;

				 SupportModal.show().finally(() => { // TODO: mock
					 this.supportModalButtonIsWaiting = false;
					 this.hideSidebar();
				 });
			 },

			 showFormPopupType(payload) {
				 if (payload?.form === SIGN_UP_FORM_TYPE.EMAIL) { // TODO: mock
					 updateStateFormSignUpEmail(payload); // TODO: mock
				 } else {
					 signUpSocialButtonsFromGame(payload); // TODO: mock
				 }
			 },

			 showCreateLogin() {
				 createLoginModal.showInfo();
			 },

			 hideOverlayItems(event) {
				 const targetClass = event?.target?.className;
				 if (!targetClass || targetClass !== "overlay-dropdown-close") {
					 this.hideSidebar();
				 }
				 this.hideSupportModal(); // TODO: mock mixin
				 this.hideMeyaError(); // TODO: mock mixin
			 },

			 showConfirmEmail() {
				 if (window.NXUserInfo?.email_confirmed) {
					 UserService.verifyEmailOnServer(); // TODO: mock
				 } else {
					 this.hideOverlayItems();
					 ConfirmEmailModal.show(); // TODO: mock
				 }
			 },

			 showCookiesSettings() {
				 this.hideOverlayItems();
				 CookieConsentModal.show("menu"); // TODO: mock
			 },

			 openSidebar() {
				 this.sidebarMode = SIDEBAR_MODE_MENU;
				 this.sidebarIsVisible = true;
			 },

			 hideSidebar() {
				 if (ModalLockService.isOpened()) { // TODO: mock
					 return;
				 }

				 if (this.sidebarIsVisible) {
					 NotificationBadgeService.hideBadge(); // TODO: mock
				 }

				 this.sidebarIsVisible = false;
			 },

			 setSidebarMode(mode) {
				 this.sidebarMode = mode || SIDEBAR_MODE_MENU;
			 },

			 toggleCurrencyDropdown(event) {
				 if (this.currencyDropdownDisabled) return;

				 if (this.currencyDropdownVisible) {
					 this.hideCurrencyList(event);
				 } else {
					 this.openCurrencyList(event);
				 }
			 },

			 // TODO: move getDropdownStyle here
			 getDropdownStyle(triggerElement) {
				 const vMargin = DropdownConfig.DROPDOWN_ROOT_VERTICAL_MARGIN;
				 const hMargin = DropdownConfig.DROPDOWN_ROOT_HORIZONTAL_MARGIN;

				 const triggerRect = triggerElement.getBoundingClientRect();
				 const viewportRect = document.documentElement.getBoundingClientRect();

				 const isCustomWidth = triggerRect.width > DropdownConfig.DROPDOWN_MIN_WIDTH;
				 const isMobile = viewportRect.width <= DropdownConfig.DROPDOWN_ROOT_MOBILE_WIDTH;

				 let targetWidth;
				 if (isCustomWidth) {
					 targetWidth = triggerRect.width;
				 } else if (isMobile) {
					 targetWidth = DropdownConfig.DROPDOWN_MOBILE_WIDTH;
				 } else {
					 targetWidth = DropdownConfig.DROPDOWN_BASE_WIDTH;
				 }

				 const spaceBelow = viewportRect.height - triggerRect.bottom;
				 const spaceAbove = triggerRect.top;
				 const flipUpwards = spaceAbove > spaceBelow;

				 const rawLeft = triggerRect.left;
				 const maxLeft = viewportRect.width - targetWidth - hMargin;
				 const clampedLeft = Math.max(hMargin, Math.min(rawLeft, maxLeft));

				 const style = {
					 display: "flex",
					 maxHeight: `${Math.max(spaceAbove, spaceBelow) - vMargin * 2}px`,
					 maxWidth: `${targetWidth}px`,
					 top: flipUpwards ? "auto" : `${triggerRect.bottom + vMargin}px`,
					 bottom: flipUpwards ? `${viewportRect.height - triggerRect.top + vMargin}px` : "auto",
					 left: `${clampedLeft}px`
				 };

				 if (isCustomWidth) {
					 style.width = `${triggerRect.width}px`;
				 }

				 return style;
			 },

			 hideLangDropdown() {
				 this.langDropdownVisible = false;
				 this.langDropdownStyle = { display: "none" };

				 this.landDropdownResizeDispose?.dispose();
				 this.landDropdownResizeDispose = null;
			 },

			 openCurrencyList(event) {
				 this.currencyDropdownVisible = true;
				 const triggerEl = event.currentTarget;

				 const updatePosition = () => {
					 this.currencyDropdownStyle = this.getDropdownStyle(triggerEl);
				 };

				 this.currencyDropdownResizeDispose = WindowService.onWindowResize(updatePosition);
				 updatePosition();
			 },

			 hideCurrencyList() {
				 this.currencyDropdownVisible = false;
				 this.currencyDropdownStyle = { display: "none" };

				 this.currencyDropdownResizeDispose?.dispose();
				 this.currencyDropdownResizeDispose = null;
			 },

			 openImpressumDropdown(event) {
				 this.impressumDropdownVisible = true;
				 const triggerEl = event.currentTarget;

				 const updatePosition = () => {
					 this.impressumDropdownStyle = this.getDropdownStyle(triggerEl);
				 };

				 updatePosition();
				 this.impressumDropdownResizeDispose = WindowService.onWindowResize(updatePosition);
			 },

			 hideImpressumDropdown() {
				 this.impressumDropdownVisible = false;
				 this.impressumDropdownStyle = { display: "none" };

				 this.impressumDropdownResizeDispose?.dispose();
				 this.impressumDropdownResizeDispose = null;
			 },

			 hideUserProfile() {
				 this.sidebarMode = SIDEBAR_MODE_MENU;
			 },

			 openUserProfile() {
				 this.sendButtonClicks("menuProfile");
				 this.sidebarMode = SIDEBAR_MODE_PROFILE;
			 },

			 signUpProposal() {
				 this.hideOverlayItems();

				 analytics.log(PAGE_EVENT.button_click, {
					 button: "delayedOpenRegistrationPopup",
					 mode: BUTTONS_CLICK_PAGE.gameScreenDelayed
				 });

				 updateStateFormSignUpEmail({
					 data: {
						 title: Localization.sign_up,
						 description: Localization.reg_signup_to_save_progress
					 },
					 reason: SIGN_UP_EMAIL.LOGIN_DELAYED
				 });
			 },

			 loginDelayed() {
				 this.hideOverlayItems();

				 analytics.log(PAGE_EVENT.button_click, {
					 button: "delayedOpenLoginPopup",
					 mode: BUTTONS_CLICK_PAGE.gameScreenDelayed
				 });

				 LoginDelayedModal.show();
			 },

			 communityWidgetClick() {
				 this.sendButtonClicks("social_community");
				 CommunityService.communityWidgetClick();
			 },

			 async logoutAll() {
				 try {
					 await Api.post("/logout_all", {});
					 window.location.href = ".";
				 } catch (err) {
					 console.error("[Auth] Failed to logout all sessions:", err);
				 }
			 },
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
