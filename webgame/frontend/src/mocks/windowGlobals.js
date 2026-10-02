window.NXUserInfo = window.NXUserInfo || {
	user_id: '12345',
	language: 'en',
	sublanguage: 'en',
	currency: 'PLN',
	is_new_user_registered: false,
	social_network: 'email',
        geoip_Country_Code: 'PL',
        geoip_City: 'City',
	is_delayed_registration: 0,
	is_tooltip: 1,
	email_confirmed: '',
        ts_registration: 1790431700,
        ts_now: 1790963912,
	name: 'Test',
	fullName: 'Test',
	email: 'test@example.com',
	login: 'test@example.com',
	background_id: '0',
	can_add_login: '',
	platform: 'web',
        platform_id: "12345",
	isNewUserRegistered24h: true,
	antiAddiction: null,
	groupNumber: null,
        has_linked_phone: false,
        groupNumber: "08",
        antiFraud: true,
        support: {type: "Zendesk"},
        recaptcha: {
            clientKey: '',
            clientVisibleKey: '',
            clientKeyType: 'invisible',
        },
        otel: {
            enabled: true,
            endpoint: '',
            clientName: '',
            environment: 'production',
        },
        integrations: {"flags":{"isSolarEnabled":false,"isGtmEnabled":true},"solar":{"appKey":"","userCode":""},"gtm":{"isGtg":true,"containerId":"GTM-NZL7Z2L"}},
        session_id: "session",
};


window.NXFlashVars = window.NXFlashVars || {
	uid: "12345",
        network: "web",
        country_code: "PL",
        currency: "PLN",
        is_new_user_registered: false,
        interface_lang: "en",
        ident: "heroes",
        platformNetwork: "web",
        requestLoadingInfoTimeout: 3000,

        error_url: "http://localhost:8081",
        browser: "Firefox",
        app_id: "3",
        auth_key: "key",
        sys_id: "4",

        game_url: "",
        group_url: "",
        rpc_url: "http://localhost:8081/api/",
        discord_url: "",
        twitter_url: "",
        youtube_url: "",

        index_url: {
		"client_index": "http://localhost:8081/indices/index.client.json.gz",
		"asset_index":"http://localhost:8081/indices/index.assets.json",
		"lib_index":"http://localhost:8081/indices/index.lib.json.gz",
		"locales_index":"http://localhost:8081/indices/index.locales.json"
	},
	static_url: "http://localhost:8081/",
        static_urls: ["http://localhost:8081/"],
        url_custom_params: "",
        client_version: "691",
        client_log_url: "http://localhost:8081/",

	preloader_js: "http://localhost:8081/assets/heroes.d24aef0654d76f8bbeefb95953b00cf8.js",
	playable_js: "",
        videojsFirstLaunchPreloader: 0,
        isEpicStartSplit: false,
        initPlayableName: null,
        initPlayableLink: null,
        playableBaseUrl: "",

        userState: {
		"params": {"gtm": true},
		"groupNumber":"08",
		"emailSubscription": {"newsletter": false},
		"firstMissionCompleted":true
	},
        deviceType: "desktop",
        userIp: "1.0.0.225",

	playable: false,
};


window.pagelive = window.pagelive || {
	onAppInstall: (cb) => cb(),
	onAppShowPromt: (cb) => cb(),
	onAppPromtAccepted: (cb) => cb(),
	onAppPromtDismiss: (cb) => cb()
};

window.NXAppInfo = {
	nxSource: "",
	visiting_uid: "test-session"
};

window.NXPushDSettings = {
	server_url: "",
	network: "web",
	app_id: "heroeshx",
	access_token: ""
};
