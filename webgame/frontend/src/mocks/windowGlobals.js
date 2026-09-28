window.NXUserInfo = window.NXUserInfo || {
	user_id: 98765432,
	is_new_user_registered: true,
	is_delayed_registration: false,
	social_network: "facebook",
	isNewUserRegistered24h: true,
	groupNumber: null
};

window.NXFlashVars = window.NXFlashVars || {
	userState: {}
};

window.pagelive = window.pagelive || {
	onAppInstall: (cb) => cb(),
	onAppShowPromt: (cb) => cb(),
	onAppPromtAccepted: (cb) => cb(),
	onAppPromtDismiss: (cb) => cb()
};
