(() => {
  var e,
    t,
    n,
    r,
    o,
    i,
    u = {
      4691: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => r });
        const r = Object.freeze({
          init: function (e) {
            var t = e.pagelive,
              n = e.resolvers,
              r = new Map(),
              o = window.NXSDKSetup || (window.NXSDKSetup = []),
              i = window.NXSDK || (window.NXSDK = {});
            function u() {
              for (
                var e = [],
                  t = [],
                  o = arguments.length,
                  u = new Array(o),
                  a = 0;
                a < o;
                a++
              )
                u[a] = arguments[a];
              u.splice(0, u.length).forEach(function (o) {
                o &&
                  ("function" != typeof o
                    ? e.push(
                        (function (e) {
                          r.has(e) ||
                            r.set(
                              e,
                              new Promise(function (t, r) {
                                return e in i
                                  ? t(i[e])
                                  : e in n
                                  ? n[e]()
                                      .then(function (n) {
                                        t((i[e] = n));
                                      })
                                      .catch(function (t) {
                                        try {
                                          r(
                                            "NXSDK Init error in module: "
                                              .concat(e, ". Error: ")
                                              .concat(
                                                (null == t
                                                  ? void 0
                                                  : t.message) || t
                                              )
                                          );
                                        } catch (t) {
                                          r(
                                            "NXSDK Init error in module: " +
                                              e +
                                              ". NXSDK catch"
                                          );
                                        }
                                      })
                                  : r("NXSDK Unknown module: " + e);
                              })
                            );
                          return r.get(e);
                        })(o)
                      )
                    : t.push(o));
              }),
                Promise.allSettled(e).then(function (e) {
                  var n = e
                      .filter(function (e) {
                        return "rejected" === e.status;
                      })
                      .map(function (e) {
                        return e.reason;
                      }),
                    r = [i];
                  n.length && r.push(n),
                    Promise.allSettled(
                      t.map(function (e) {
                        return new Promise(function (t, n) {
                          try {
                            e.apply(null, r), t(!0);
                          } catch (e) {
                            n(e);
                          }
                        });
                      })
                    );
                });
            }
            (o.unshift = u),
              t.onWindowReady(function () {
                (o.push = u), u.apply(null, o);
              });
          },
        });
      },
      17166: (e, t, n) => {
        "use strict";
        n.r(t),
          n.d(t, {
            COOKIE_GDPR_EVENT: () => i,
            METRICS_EVENT: () => r.METRICS_EVENT,
            PAGE_EVENT: () => o,
          });
        var r = n(51783),
          o = {
            button_click: "button_click",
            social_button_click: "social_button_click",
            landing_loaded: "landing_loaded",
            plain_log: "landingSend",
            landing_page_loading: "landing_page_loading",
            landing_page_time_loading: "landing_page_time_loading",
            ad_block: "ad_block",
            push_consent: "push_consent",
            mkt_cookie: "mkt_cookie",
          },
          i = {
            show_cookie_window: "gdpr.show_cookie_window",
            show_cookie_policy: "gdpr.show_cookie_policy",
            accept_disclaimer: "gdpr.accept_disclaimer",
            accept_all: "gdpr.accept_all",
            accept_strict: "gdpr.accept_strict",
            show_settings: "gdpr.show_settings",
            hide_settings: "gdpr.hide_settings",
            accept_all_settings: "gdpr.accept_all_settings",
            accept_selected_settings: "gdpr.accept_selected_settings",
            show_description: "gdpr.open_description",
            hide_description: "gdpr.hide_description",
            allow_feature_click: "gdpr.allow_feature_click",
            disable_feature_click: "gdpr.disable_feature_click",
            control_point: "control_point",
          };
      },
      51783: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { METRICS_EVENT: () => r });
        var r = { init: "metrics_init" };
      },
      69442: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => r });
        const r = Object.freeze({
          USER_INFO: "UserInfo",
          LOCALIZATION: "Localization",
          MAIN_METRICS: "MainMetrics",
          SDK_METRICS: "SdkMetrics",
          CONSENT_UI: "ConsentUi",
          CONSENT: "Consent",
          API: "Api",
          USER: "User",
          AUTH: "Auth",
        });
      },
      32862: (e, t, n) => {
        "use strict";
        function r(e) {
          return (
            (r =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            r(e)
          );
        }
        function o(e, t) {
          for (var n = 0; n < t.length; n++) {
            var o = t[n];
            (o.enumerable = o.enumerable || !1),
              (o.configurable = !0),
              "value" in o && (o.writable = !0),
              Object.defineProperty(
                e,
                ((i = o.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== r(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var o = n.call(e, t || "default");
                    if ("object" !== r(o)) return o;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(i, "string")),
                "symbol" === r(u) ? u : String(u)),
                o
              );
          }
          var i, u;
        }
        n.r(t), n.d(t, { default: () => u });
        var i = 0,
          u = (function () {
            function e(t, n) {
              !(function (e, t) {
                if (!(e instanceof t))
                  throw new TypeError("Cannot call a class as a function");
              })(this, e),
                (this._key = t),
                (this._ttl = n);
            }
            var t, n, r;
            return (
              (t = e),
              (n = [
                {
                  key: "key",
                  get: function () {
                    return this._key || (this._key = "hw_store_".concat(i++));
                  },
                },
                {
                  key: "ttl",
                  get: function () {
                    return this._ttl || (this._ttl = 2592e6);
                  },
                },
                {
                  key: "getItem",
                  value: function () {
                    for (
                      var e = this.key + "=",
                        t = document.cookie.split(";"),
                        n = 0;
                      n < t.length;
                      n++
                    ) {
                      for (var r = t[n]; " " == r.charAt(0); )
                        r = r.substring(1, r.length);
                      if (0 == r.indexOf(e))
                        return r.substring(e.length, r.length);
                    }
                    return null;
                  },
                },
                {
                  key: "setTtl",
                  value: function (e) {
                    this._ttl = e;
                  },
                },
                {
                  key: "setItem",
                  value: function () {
                    var e =
                        arguments.length > 0 && void 0 !== arguments[0]
                          ? arguments[0]
                          : "",
                      t = new Date(+new Date() + this.ttl);
                    document.cookie =
                      this.key +
                      "=" +
                      e +
                      "; path=/; expires=" +
                      t.toUTCString();
                  },
                },
                {
                  key: "removeItem",
                  value: function () {
                    (document.cookie =
                      this.key + "=; expires=Thu, 01 Jan 1970 00:00:01 GMT;"),
                      (document.cookie =
                        this.key +
                        "=; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;");
                  },
                },
              ]),
              n && o(t.prototype, n),
              r && o(t, r),
              Object.defineProperty(t, "prototype", { writable: !1 }),
              e
            );
          })();
      },
      70724: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => u });
        var r = n(58387);
        function o(e) {
          return (
            (o =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            o(e)
          );
        }
        function i(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(
                e,
                ((i = r.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== o(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var r = n.call(e, t || "default");
                    if ("object" !== o(r)) return r;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(i, "string")),
                "symbol" === o(u) ? u : String(u)),
                r
              );
          }
          var i, u;
        }
        var u = (function () {
          function e(t, n) {
            var o = this;
            !(function (e, t) {
              if (!(e instanceof t))
                throw new TypeError("Cannot call a class as a function");
            })(this, e);
            var i = n.getItem();
            (this._type = t), (this._storage = n);
            try {
              this._value = JSON.parse(i);
            } catch (e) {
              this._value = /\[.+\]/.test(i) ? null : i;
            }
            r.default.subscribe(t, function () {
              r.default[t] ? o.setItem() : o.removeItem();
            });
          }
          var t, n, o;
          return (
            (t = e),
            (n = [
              {
                key: "type",
                get: function () {
                  return this._type;
                },
              },
              {
                key: "storage",
                get: function () {
                  return this._storage;
                },
              },
              {
                key: "value",
                get: function () {
                  return this._value;
                },
                set: function (e) {
                  this._value = JSON.stringify(e);
                },
              },
              {
                key: "getItem",
                value: function () {
                  return this.value;
                },
              },
              {
                key: "setItem",
                value: function (e) {
                  void 0 !== e && (this.value = e),
                    r.default[this._type] && this.storage.setItem(this.value);
                },
              },
              {
                key: "removeItem",
                value: function () {
                  this.storage.removeItem(this.value);
                },
              },
            ]) && i(t.prototype, n),
            o && i(t, o),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            e
          );
        })();
      },
      43325: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => l });
        var r = n(70724),
          o = n(32862);
        function i(e) {
          return (
            (i =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            i(e)
          );
        }
        function u(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(
                e,
                ((o = r.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== i(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var r = n.call(e, t || "default");
                    if ("object" !== i(r)) return r;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(o, "string")),
                "symbol" === i(u) ? u : String(u)),
                r
              );
          }
          var o, u;
        }
        function a(e, t) {
          return (
            (a = Object.setPrototypeOf
              ? Object.setPrototypeOf.bind()
              : function (e, t) {
                  return (e.__proto__ = t), e;
                }),
            a(e, t)
          );
        }
        function c(e) {
          var t = (function () {
            if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
            if (Reflect.construct.sham) return !1;
            if ("function" == typeof Proxy) return !0;
            try {
              return (
                Boolean.prototype.valueOf.call(
                  Reflect.construct(Boolean, [], function () {})
                ),
                !0
              );
            } catch (e) {
              return !1;
            }
          })();
          return function () {
            var n,
              r = s(e);
            if (t) {
              var o = s(this).constructor;
              n = Reflect.construct(r, arguments, o);
            } else n = r.apply(this, arguments);
            return (function (e, t) {
              if (t && ("object" === i(t) || "function" == typeof t)) return t;
              if (void 0 !== t)
                throw new TypeError(
                  "Derived constructors may only return object or undefined"
                );
              return (function (e) {
                if (void 0 === e)
                  throw new ReferenceError(
                    "this hasn't been initialised - super() hasn't been called"
                  );
                return e;
              })(e);
            })(this, n);
          };
        }
        function s(e) {
          return (
            (s = Object.setPrototypeOf
              ? Object.getPrototypeOf.bind()
              : function (e) {
                  return e.__proto__ || Object.getPrototypeOf(e);
                }),
            s(e)
          );
        }
        var l = (function (e) {
          !(function (e, t) {
            if ("function" != typeof t && null !== t)
              throw new TypeError(
                "Super expression must either be null or a function"
              );
            (e.prototype = Object.create(t && t.prototype, {
              constructor: { value: e, writable: !0, configurable: !0 },
            })),
              Object.defineProperty(e, "prototype", { writable: !1 }),
              t && a(e, t);
          })(s, e);
          var t,
            n,
            r,
            i = c(s);
          function s(e, t, n) {
            var r;
            !(function (e, t) {
              if (!(e instanceof t))
                throw new TypeError("Cannot call a class as a function");
            })(this, s);
            var u = new o.default(e, n);
            return ((r = i.call(this, t, u))._cookieStorage = u), r;
          }
          return (
            (t = s),
            (n = [
              {
                key: "setTtl",
                value: function (e) {
                  this._cookieStorage.setTtl(e);
                },
              },
            ]) && u(t.prototype, n),
            r && u(t, r),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            s
          );
        })(r.default);
      },
      16712: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => l });
        var r = n(70724),
          o = n(93902);
        function i(e) {
          return (
            (i =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            i(e)
          );
        }
        function u(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(
                e,
                ((o = r.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== i(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var r = n.call(e, t || "default");
                    if ("object" !== i(r)) return r;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(o, "string")),
                "symbol" === i(u) ? u : String(u)),
                r
              );
          }
          var o, u;
        }
        function a(e, t) {
          return (
            (a = Object.setPrototypeOf
              ? Object.setPrototypeOf.bind()
              : function (e, t) {
                  return (e.__proto__ = t), e;
                }),
            a(e, t)
          );
        }
        function c(e) {
          var t = (function () {
            if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
            if (Reflect.construct.sham) return !1;
            if ("function" == typeof Proxy) return !0;
            try {
              return (
                Boolean.prototype.valueOf.call(
                  Reflect.construct(Boolean, [], function () {})
                ),
                !0
              );
            } catch (e) {
              return !1;
            }
          })();
          return function () {
            var n,
              r = s(e);
            if (t) {
              var o = s(this).constructor;
              n = Reflect.construct(r, arguments, o);
            } else n = r.apply(this, arguments);
            return (function (e, t) {
              if (t && ("object" === i(t) || "function" == typeof t)) return t;
              if (void 0 !== t)
                throw new TypeError(
                  "Derived constructors may only return object or undefined"
                );
              return (function (e) {
                if (void 0 === e)
                  throw new ReferenceError(
                    "this hasn't been initialised - super() hasn't been called"
                  );
                return e;
              })(e);
            })(this, n);
          };
        }
        function s(e) {
          return (
            (s = Object.setPrototypeOf
              ? Object.getPrototypeOf.bind()
              : function (e) {
                  return e.__proto__ || Object.getPrototypeOf(e);
                }),
            s(e)
          );
        }
        var l = (function (e) {
          !(function (e, t) {
            if ("function" != typeof t && null !== t)
              throw new TypeError(
                "Super expression must either be null or a function"
              );
            (e.prototype = Object.create(t && t.prototype, {
              constructor: { value: e, writable: !0, configurable: !0 },
            })),
              Object.defineProperty(e, "prototype", { writable: !1 }),
              t && a(e, t);
          })(s, e);
          var t,
            n,
            r,
            i = c(s);
          function s(e, t) {
            return (
              (function (e, t) {
                if (!(e instanceof t))
                  throw new TypeError("Cannot call a class as a function");
              })(this, s),
              i.call(this, t, new o.default(e, localStorage))
            );
          }
          return (
            (t = s),
            n && u(t.prototype, n),
            r && u(t, r),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            t
          );
        })(r.default);
      },
      39373: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => l });
        var r = n(70724),
          o = n(93902);
        function i(e) {
          return (
            (i =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            i(e)
          );
        }
        function u(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(
                e,
                ((o = r.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== i(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var r = n.call(e, t || "default");
                    if ("object" !== i(r)) return r;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(o, "string")),
                "symbol" === i(u) ? u : String(u)),
                r
              );
          }
          var o, u;
        }
        function a(e, t) {
          return (
            (a = Object.setPrototypeOf
              ? Object.setPrototypeOf.bind()
              : function (e, t) {
                  return (e.__proto__ = t), e;
                }),
            a(e, t)
          );
        }
        function c(e) {
          var t = (function () {
            if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
            if (Reflect.construct.sham) return !1;
            if ("function" == typeof Proxy) return !0;
            try {
              return (
                Boolean.prototype.valueOf.call(
                  Reflect.construct(Boolean, [], function () {})
                ),
                !0
              );
            } catch (e) {
              return !1;
            }
          })();
          return function () {
            var n,
              r = s(e);
            if (t) {
              var o = s(this).constructor;
              n = Reflect.construct(r, arguments, o);
            } else n = r.apply(this, arguments);
            return (function (e, t) {
              if (t && ("object" === i(t) || "function" == typeof t)) return t;
              if (void 0 !== t)
                throw new TypeError(
                  "Derived constructors may only return object or undefined"
                );
              return (function (e) {
                if (void 0 === e)
                  throw new ReferenceError(
                    "this hasn't been initialised - super() hasn't been called"
                  );
                return e;
              })(e);
            })(this, n);
          };
        }
        function s(e) {
          return (
            (s = Object.setPrototypeOf
              ? Object.getPrototypeOf.bind()
              : function (e) {
                  return e.__proto__ || Object.getPrototypeOf(e);
                }),
            s(e)
          );
        }
        var l = (function (e) {
          !(function (e, t) {
            if ("function" != typeof t && null !== t)
              throw new TypeError(
                "Super expression must either be null or a function"
              );
            (e.prototype = Object.create(t && t.prototype, {
              constructor: { value: e, writable: !0, configurable: !0 },
            })),
              Object.defineProperty(e, "prototype", { writable: !1 }),
              t && a(e, t);
          })(s, e);
          var t,
            n,
            r,
            i = c(s);
          function s(e, t) {
            return (
              (function (e, t) {
                if (!(e instanceof t))
                  throw new TypeError("Cannot call a class as a function");
              })(this, s),
              i.call(this, t, new o.default(e, sessionStorage))
            );
          }
          return (
            (t = s),
            n && u(t.prototype, n),
            r && u(t, r),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            t
          );
        })(r.default);
      },
      93902: (e, t, n) => {
        "use strict";
        function r(e) {
          return (
            (r =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            r(e)
          );
        }
        function o(e, t) {
          for (var n = 0; n < t.length; n++) {
            var o = t[n];
            (o.enumerable = o.enumerable || !1),
              (o.configurable = !0),
              "value" in o && (o.writable = !0),
              Object.defineProperty(
                e,
                ((i = o.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== r(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var o = n.call(e, t || "default");
                    if ("object" !== r(o)) return o;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(i, "string")),
                "symbol" === r(u) ? u : String(u)),
                o
              );
          }
          var i, u;
        }
        n.r(t), n.d(t, { default: () => i });
        document.cookie;
        var i = (function () {
          function e(t, n) {
            !(function (e, t) {
              if (!(e instanceof t))
                throw new TypeError("Cannot call a class as a function");
            })(this, e),
              (this._key = t),
              (this._storage = n);
          }
          var t, n, r;
          return (
            (t = e),
            (n = [
              {
                key: "key",
                get: function () {
                  return this._key;
                },
              },
              {
                key: "storage",
                get: function () {
                  return this._storage;
                },
              },
              {
                key: "getItem",
                value: function () {
                  return this.storage.getItem(this.key);
                },
              },
              {
                key: "setItem",
                value: function (e) {
                  return this.storage.setItem(this.key, e);
                },
              },
              {
                key: "removeItem",
                value: function () {
                  return this.storage.removeItem(this.key);
                },
              },
            ]) && o(t.prototype, n),
            r && o(t, r),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            e
          );
        })();
      },
      58387: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => y });
        var r = n(93902),
          o = n(9339),
          i = new r.default("gdpr_settings", localStorage),
          u = {},
          a = {},
          c = [o.default.strict, o.default.functional],
          s = JSON.parse(i.getItem() || "{}");
        for (var l in (void 0 !== s[o.default.metrics] &&
          void 0 === s[o.default.partners] &&
          (s[o.default.partners] = s[o.default.metrics]),
        o.default)) {
          var f = o.default[l],
            d = b(f) || s[f] || null;
          (u[f] = d), (a[f] = []);
        }
        var p = new Proxy(u, {
          get: function (e, t) {
            switch (t) {
              case "subscribe":
                return v;
              case "acceptAll":
                return m;
              case "acceptStrict":
                return h;
              default:
                return e[t];
            }
          },
          set: function (e, t, n) {
            if ("settings" === t) {
              var r = Object.assign({}, u);
              for (var c in (Object.assign(u, n), r))
                r[c] !== n[c] &&
                  a[c].forEach(function (e) {
                    e();
                  });
              return (
                (function (e) {
                  if (!u[o.default.functional]) return i.removeItem();
                  i.setItem(JSON.stringify(e));
                })(u),
                !0
              );
            }
            return !1;
          },
        });
        const y = p;
        function v(e, t) {
          Object.values(o.default).indexOf(e) < 0 || a[e].push(t);
        }
        function m() {
          var e = {};
          for (var t in o.default) {
            e[o.default[t]] = !0;
          }
          p.settings = e;
        }
        function h() {
          var e = {};
          for (var t in o.default) {
            var n = o.default[t];
            e[n] = b(n);
          }
          p.settings = e;
        }
        function b(e) {
          return c.indexOf(e) >= 0;
        }
      },
      85656: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => o });
        var r = n(72182);
        const o = new Proxy(
          { isCookieSplit: !0, cookieSplitGroup: r.default.HIGH },
          {
            get: function (e, t) {
              return "cookieSplitGroup" === t
                ? (e.isCookieSplit && e.cookieSplitGroup) || null
                : e[t];
            },
            set: function (e, t, n) {
              switch (t) {
                case "isCookieSplit":
                  return void 0 === n || (e.isCookieSplit = !!n), !0;
                case "cookieSplitGroup":
                  return (
                    Object.values(r.default).indexOf(n) < 0 ||
                      (e.cookieSplitGroup = n),
                    !0
                  );
                default:
                  return !1;
              }
            },
          }
        );
      },
      9339: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => r });
        const r = {
          strict: "strict",
          functional: "functional",
          metrics: "metrics",
          partners: "partners",
        };
      },
      83654: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { GAME_SETTINGS: () => r });
        var r = {
          ADAPTIVE_SCREEN_FLAG: "is_design_updated",
          WIDE_SCREEN_FLAG: "is_wide_screen",
        };
      },
      72182: (e, t, n) => {
        "use strict";
        n.r(t),
          n.d(t, {
            COOKIE_SPLIT_EVENT_NAME: () => o,
            COOKIE_SPLIT_GROUP: () => r,
            default: () => i,
          });
        var r = { LOW: "A", HIGH: "B", MEDIUM: "C" },
          o = {
            banner_low_compliance: "banner_low_compliance",
            banner_high_compliance: "banner_high_compliance",
            banner_medium_compliance: "banner_medium_compliance",
            settings_window_high_compliance: "settings_window_high_compliance",
            settings_window_medium_compliance:
              "settings_window_medium_compliance",
            settings_window_low_compliance: "settings_window_low_compliance",
          };
        const i = r;
      },
      25232: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => f });
        var r = n(9339),
          o = n(72182),
          i = n(85656),
          u = n(58387),
          a = n(43325),
          c = n(16712),
          s = n(39373),
          l = n(44846);
        const f =
          window.consent ||
          (window.consent = new Proxy(
            {
              preferences: u.default,
              settings: i.default,
              FeatureType: r.default,
              SplitGroup: o.default,
              Data: {
                GdprCookieStorage: a.default,
                GdprLocalStorage: c.default,
                GdprSessionStorage: s.default,
                CookieAlertStorage: l.default,
              },
            },
            {
              get: function (e, t) {
                switch (t) {
                  case "subscribe":
                  case "acceptAll":
                  case "acceptStrict":
                    return u.default[t];
                  default:
                    return e[t];
                }
              },
              set: function (e, t, n) {
                switch (t) {
                  case "settings":
                    return (i.default[t] = n), !0;
                  case "preferences":
                    return (u.default.settings = n), !0;
                  default:
                    return !1;
                }
              },
            }
          ));
      },
      44846: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => c });
        var r = n(25232),
          o = n(43325),
          i = n(9339),
          u = new o.default("cookie_alert_accepted", i.default.functional),
          a = u.getItem();
        const c = Object.freeze({
          cookieIsAccepted: a,
          accept: function () {
            u.setTtl(
              ((e = { ACCEPT_ALL: 63072e6, ACCEPT_OPTIONS: 6048e5 }),
              Object.values(r.default.preferences).indexOf(!1) > -1
                ? e.ACCEPT_OPTIONS
                : e.ACCEPT_ALL)
            ),
              u.setItem("yes");
            var e;
          },
        });
      },
      63474: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => c });
        var r = n(16712),
          o = n(9339),
          i = n(83654),
          u = new r.default(
            i.GAME_SETTINGS.ADAPTIVE_SCREEN_FLAG,
            o.default.functional
          ),
          a = new r.default(
            i.GAME_SETTINGS.WIDE_SCREEN_FLAG,
            o.default.functional
          );
        const c = {
          adaptiveGetItem: function () {
            return JSON.parse(u.getItem());
          },
          adaptiveSetItem: function (e) {
            u.setItem(e);
          },
          wideScreenGetItem: function () {
            return JSON.parse(a.getItem());
          },
          wideScreenSetItem: function (e) {
            a.setItem(e);
          },
        };
      },
      8622: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => u });
        var r = n(51783);
        function o(e) {
          return (
            (o =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            o(e)
          );
        }
        function i(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(
                e,
                ((i = r.key),
                (u = void 0),
                (u = (function (e, t) {
                  if ("object" !== o(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var r = n.call(e, t || "default");
                    if ("object" !== o(r)) return r;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(i, "string")),
                "symbol" === o(u) ? u : String(u)),
                r
              );
          }
          var i, u;
        }
        var u = (function () {
          function e() {
            !(function (e, t) {
              if (!(e instanceof t))
                throw new TypeError("Cannot call a class as a function");
            })(this, e);
          }
          var t, n, o;
          return (
            (t = e),
            (n = [
              {
                key: "events",
                get: function () {
                  return this._events || (this._events = {});
                },
              },
              {
                key: "subscribe",
                value: function (e, t) {
                  var n = this.events[e] || (this.events[e] = []);
                  return (
                    n.push(t),
                    {
                      dispose: function () {
                        var e = n.indexOf(t);
                        e < 0 || n.splice(e, 1);
                      },
                    }
                  );
                },
              },
              {
                key: "unsubscribe",
                value: function (e, t) {
                  var n = this.events[e] || [],
                    r = n.indexOf(t);
                  r < 0 || n.splice(r, 1);
                },
              },
              {
                key: "emit",
                value: function (e, t, n) {
                  var o = this.events[e],
                    i = [];
                  return (
                    e === r.METRICS_EVENT.init &&
                      delete this.events[r.METRICS_EVENT.init],
                    null == o ||
                      o.forEach(function (e) {
                        var r = e(t, n);
                        r instanceof Promise && i.push(r);
                      }),
                    Promise.all(i)
                  );
                },
              },
            ]) && i(t.prototype, n),
            o && i(t, o),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            e
          );
        })();
      },
      85139: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => d });
        var r = n(8622),
          o = n(24649),
          i = n(51783);
        function u(e) {
          return (
            (u =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            u(e)
          );
        }
        function a(e, t) {
          var n =
            ("undefined" != typeof Symbol && e[Symbol.iterator]) ||
            e["@@iterator"];
          if (!n) {
            if (
              Array.isArray(e) ||
              (n = s(e)) ||
              (t && e && "number" == typeof e.length)
            ) {
              n && (e = n);
              var r = 0,
                o = function () {};
              return {
                s: o,
                n: function () {
                  return r >= e.length
                    ? { done: !0 }
                    : { done: !1, value: e[r++] };
                },
                e: function (e) {
                  throw e;
                },
                f: o,
              };
            }
            throw new TypeError(
              "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          }
          var i,
            u = !0,
            a = !1;
          return {
            s: function () {
              n = n.call(e);
            },
            n: function () {
              var e = n.next();
              return (u = e.done), e;
            },
            e: function (e) {
              (a = !0), (i = e);
            },
            f: function () {
              try {
                u || null == n.return || n.return();
              } finally {
                if (a) throw i;
              }
            },
          };
        }
        function c(e) {
          return (
            (function (e) {
              if (Array.isArray(e)) return l(e);
            })(e) ||
            (function (e) {
              if (
                ("undefined" != typeof Symbol && null != e[Symbol.iterator]) ||
                null != e["@@iterator"]
              )
                return Array.from(e);
            })(e) ||
            s(e) ||
            (function () {
              throw new TypeError(
                "Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
              );
            })()
          );
        }
        function s(e, t) {
          if (e) {
            if ("string" == typeof e) return l(e, t);
            var n = Object.prototype.toString.call(e).slice(8, -1);
            return (
              "Object" === n && e.constructor && (n = e.constructor.name),
              "Map" === n || "Set" === n
                ? Array.from(e)
                : "Arguments" === n ||
                  /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)
                ? l(e, t)
                : void 0
            );
          }
        }
        function l(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
          return r;
        }
        function f(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(
                e,
                ((o = r.key),
                (i = void 0),
                (i = (function (e, t) {
                  if ("object" !== u(e) || null === e) return e;
                  var n = e[Symbol.toPrimitive];
                  if (void 0 !== n) {
                    var r = n.call(e, t || "default");
                    if ("object" !== u(r)) return r;
                    throw new TypeError(
                      "@@toPrimitive must return a primitive value."
                    );
                  }
                  return ("string" === t ? String : Number)(e);
                })(o, "string")),
                "symbol" === u(i) ? i : String(i)),
                r
              );
          }
          var o, i;
        }
        var d = (function () {
          function e(t) {
            !(function (e, t) {
              if (!(e instanceof t))
                throw new TypeError("Cannot call a class as a function");
            })(this, e),
              (this._key = t),
              (this.init = this.lock("".concat(t, "::init")));
          }
          var t, n, u;
          return (
            (t = e),
            (n = [
              {
                key: "emitter",
                get: function () {
                  return (
                    this._emitter || (this._emitter = new r.default(this._key))
                  );
                },
              },
              {
                key: "storage",
                get: function () {
                  var e = this;
                  return (
                    this._storage ||
                    (this._storage = new o.default(this._key, function () {
                      e.notify();
                    }))
                  );
                },
              },
              {
                key: "locks",
                get: function () {
                  return this._locks || (this._locks = new Set());
                },
              },
              {
                key: "subscribers",
                get: function () {
                  return this._subscribers || (this._subscribers = []);
                },
              },
              {
                key: "log",
                value: function (e, t) {
                  var n = {
                    key: e,
                    data: t,
                    meta: { pts: performance.now(), dts: Date.now() },
                  };
                  this.storage.push(n);
                },
              },
              {
                key: "lock",
                value: function (e) {
                  var t = this,
                    n = Symbol(e);
                  return (
                    this.locks.add(n),
                    function () {
                      t.locks.delete(n), t.notify();
                    }
                  );
                },
              },
              {
                key: "subscribe",
                value: function (e) {
                  var t,
                    n = {},
                    r = a(
                      [].concat(
                        c(Object.keys(e)),
                        c(Object.getOwnPropertySymbols(e))
                      )
                    );
                  try {
                    for (r.s(); !(t = r.n()).done; ) {
                      var o = t.value;
                      n[o] = this.emitter.subscribe(o, e[o]);
                    }
                  } catch (e) {
                    r.e(e);
                  } finally {
                    r.f();
                  }
                  return n;
                },
              },
              {
                key: "clearStoreData",
                value: function () {
                  this.storage.clearStoreData();
                },
              },
              {
                key: "notify",
                value: function () {
                  var e = this;
                  return new Promise(function (t) {
                    if (e.locks.size) return t();
                    var n = e.storage.getFreeEntries();
                    e.emitter.emit(i.METRICS_EVENT.init).then(function () {
                      var r,
                        o = [],
                        i = a(n);
                      try {
                        var u = function () {
                          var t = r.value,
                            n = t.key,
                            i = t.data,
                            u = t.meta;
                          o.push(
                            e.emitter.emit(n, i, u).then(function () {
                              t.dispose();
                            })
                          );
                        };
                        for (i.s(); !(r = i.n()).done; ) u();
                      } catch (e) {
                        i.e(e);
                      } finally {
                        i.f();
                      }
                      Promise.all(o).then(function () {
                        t();
                      });
                    });
                  });
                },
              },
            ]) && f(t.prototype, n),
            u && f(t, u),
            Object.defineProperty(t, "prototype", { writable: !1 }),
            e
          );
        })();
      },
      24649: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => m });
        var r = n(25232),
          o = n(86152);
        function i(e) {
          return (
            (i =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            i(e)
          );
        }
        function u(e, t) {
          var n = Object.keys(e);
          if (Object.getOwnPropertySymbols) {
            var r = Object.getOwnPropertySymbols(e);
            t &&
              (r = r.filter(function (t) {
                return Object.getOwnPropertyDescriptor(e, t).enumerable;
              })),
              n.push.apply(n, r);
          }
          return n;
        }
        function a(e) {
          for (var t = 1; t < arguments.length; t++) {
            var n = null != arguments[t] ? arguments[t] : {};
            t % 2
              ? u(Object(n), !0).forEach(function (t) {
                  c(e, t, n[t]);
                })
              : Object.getOwnPropertyDescriptors
              ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n))
              : u(Object(n)).forEach(function (t) {
                  Object.defineProperty(
                    e,
                    t,
                    Object.getOwnPropertyDescriptor(n, t)
                  );
                });
          }
          return e;
        }
        function c(e, t, n) {
          return (
            (t = d(t)) in e
              ? Object.defineProperty(e, t, {
                  value: n,
                  enumerable: !0,
                  configurable: !0,
                  writable: !0,
                })
              : (e[t] = n),
            e
          );
        }
        function s(e, t) {
          var n =
            ("undefined" != typeof Symbol && e[Symbol.iterator]) ||
            e["@@iterator"];
          if (!n) {
            if (
              Array.isArray(e) ||
              (n = (function (e, t) {
                if (!e) return;
                if ("string" == typeof e) return l(e, t);
                var n = Object.prototype.toString.call(e).slice(8, -1);
                "Object" === n && e.constructor && (n = e.constructor.name);
                if ("Map" === n || "Set" === n) return Array.from(e);
                if (
                  "Arguments" === n ||
                  /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)
                )
                  return l(e, t);
              })(e)) ||
              (t && e && "number" == typeof e.length)
            ) {
              n && (e = n);
              var r = 0,
                o = function () {};
              return {
                s: o,
                n: function () {
                  return r >= e.length
                    ? { done: !0 }
                    : { done: !1, value: e[r++] };
                },
                e: function (e) {
                  throw e;
                },
                f: o,
              };
            }
            throw new TypeError(
              "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          }
          var i,
            u = !0,
            a = !1;
          return {
            s: function () {
              n = n.call(e);
            },
            n: function () {
              var e = n.next();
              return (u = e.done), e;
            },
            e: function (e) {
              (a = !0), (i = e);
            },
            f: function () {
              try {
                u || null == n.return || n.return();
              } finally {
                if (a) throw i;
              }
            },
          };
        }
        function l(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
          return r;
        }
        function f(e, t) {
          for (var n = 0; n < t.length; n++) {
            var r = t[n];
            (r.enumerable = r.enumerable || !1),
              (r.configurable = !0),
              "value" in r && (r.writable = !0),
              Object.defineProperty(e, d(r.key), r);
          }
        }
        function d(e) {
          var t = (function (e, t) {
            if ("object" !== i(e) || null === e) return e;
            var n = e[Symbol.toPrimitive];
            if (void 0 !== n) {
              var r = n.call(e, t || "default");
              if ("object" !== i(r)) return r;
              throw new TypeError(
                "@@toPrimitive must return a primitive value."
              );
            }
            return ("string" === t ? String : Number)(e);
          })(e, "string");
          return "symbol" === i(t) ? t : String(t);
        }
        var p = new (0, r.default.Data.GdprLocalStorage)(
            "stored_logs",
            r.default.FeatureType.functional
          ),
          y = p.getItem(),
          v = {
            strict: h(o.default.strict),
            consent: h(o.default.consent),
            metrics: h(o.default.metrics),
          },
          m = (function () {
            function e(t, n) {
              !(function (e, t) {
                if (!(e instanceof t))
                  throw new TypeError("Cannot call a class as a function");
              })(this, e),
                (this._key = t),
                (this._entries = new Set(v[t] || [])),
                (this._onPushHandler = n);
            }
            var t, n, r;
            return (
              (t = e),
              (n = [
                {
                  key: "entries",
                  get: function () {
                    return this._entries || (this._entries = new Set());
                  },
                },
                {
                  key: "inProgressEntries",
                  get: function () {
                    return (
                      this._progressEntries ||
                      (this._progressEntries = new Set())
                    );
                  },
                },
                {
                  key: "push",
                  value: function (e) {
                    this.entries.add(e),
                      this.updateStoreData(),
                      this._onPushHandler();
                  },
                },
                {
                  key: "getFreeEntries",
                  value: function () {
                    var e,
                      t = this,
                      n = [],
                      r = s(this.entries);
                    try {
                      var o = function () {
                        var r = e.value;
                        if (t.inProgressEntries.has(r)) return "continue";
                        t.inProgressEntries.add(r),
                          n.push(
                            a(
                              a({}, r),
                              {},
                              {
                                dispose: function () {
                                  t.entries.delete(r),
                                    t.inProgressEntries.delete(r),
                                    t.updateStoreData();
                                },
                              }
                            )
                          );
                      };
                      for (r.s(); !(e = r.n()).done; ) o();
                    } catch (e) {
                      r.e(e);
                    } finally {
                      r.f();
                    }
                    return n;
                  },
                },
                {
                  key: "clearStoreData",
                  value: function () {
                    this.entries.clear(),
                      this.entries.clear(),
                      this.updateStoreData();
                  },
                },
                {
                  key: "updateStoreData",
                  value: function () {
                    this._key;
                    var e = Array.from(this.entries).reverse();
                    (e.length = Math.min(e.length, 1e3)),
                      (v[this._key] = e),
                      p.setItem(v);
                  },
                },
              ]) && f(t.prototype, n),
              r && f(t, r),
              Object.defineProperty(t, "prototype", { writable: !1 }),
              e
            );
          })();
        function h(e) {
          if (!y || !Array.isArray(null == y ? void 0 : y[e])) return [];
          var t = Date.now(),
            n = [];
          return (
            y[e].forEach(function (e) {
              var r, o;
              t >
                (null !==
                  (r =
                    null == e || null === (o = e.meta) || void 0 === o
                      ? void 0
                      : o.dts) && void 0 !== r
                  ? r
                  : 1 / 0) +
                  432e6 || n.push(e);
            }),
            n
          );
        }
      },
      86152: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => r });
        const r = Object.freeze({
          strict: "strict",
          consent: "consent",
          metrics: "metrics",
        });
      },
      63279: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => o });
        var r = n(25232);
        const o =
          window.metrics ||
          (window.metrics =
            ((a = n(17166).PAGE_EVENT),
            (c = n(85139).default),
            (s = n(86152).default),
            (l = new c(s.strict)),
            (f = new c(s.consent)),
            (d = new c(s.metrics)),
            r.default.preferences[r.default.FeatureType.metrics] ||
              (u = d.lock()),
            null === r.default.preferences[r.default.FeatureType.metrics] &&
              (i = f.lock()),
            r.default.preferences.subscribe(
              r.default.FeatureType.metrics,
              function () {
                return new Promise(function () {
                  !1 === r.default.preferences[r.default.FeatureType.metrics]
                    ? (d.clearStoreData(), i && i(), (i = null))
                    : (u && u(), (u = null), i && i(), (i = null));
                });
              }
            ),
            Object.freeze({
              init: function () {
                l.init(), f.init(), d.init();
              },
              log: function () {
                var e = [l.log.apply(l, arguments), f.log.apply(f, arguments)];
                return (
                  !1 !== r.default.preferences[r.default.FeatureType.metrics] &&
                    e.push(d.log.apply(d, arguments)),
                  Promise.all(e)
                );
              },
              lock: function (e) {
                var t = l.lock(e),
                  n = f.lock(e),
                  r = d.lock(e);
                return function () {
                  t(), n(), r();
                };
              },
              subscribe: function (e) {
                var t =
                  arguments.length > 1 &&
                  void 0 !== arguments[1] &&
                  arguments[1];
                (t ? f : d).subscribe(e);
              },
              strictSubscribe: function (e) {
                l.subscribe(e);
              },
              PAGE_EVENT: a,
            })));
        var i, u, a, c, s, l, f, d;
      },
      31891: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => r });
        const r =
          window.pagelive ||
          (window.pagelive = (function () {
            var e = "http://localhost:8081",
              t = [],
              n = [],
              r = new Set(),
              o = new Set(),
              i = new Set(),
              u = new Set(),
              a = {
                isInstalled: null,
                isStandAlone: null,
                beforeInstallEvent: null,
              },
              c = { isDocumentReady: !1, isResizeDebounce: !1 },
              s = new Map();
            return (
              window.addEventListener("DOMContentLoaded", function (e) {
                (c.isDocumentReady = !0), y(t);
              }),
              window.visualViewport.addEventListener(
                "resize",
                function (e) {
                  var t = performance.now();
                  c.isResizeDebounce &&
                    (cancelAnimationFrame(c.isResizeDebounce),
                    (c.isResizeDebounce = !1));
                  function n() {
                    c.isResizeDebounce = requestAnimationFrame(r);
                  }
                  function r(e) {
                    e - t < 8 ? n() : v();
                  }
                  n();
                },
                !0
              ),
              window.addEventListener("beforeinstallprompt", function (e) {
                e.preventDefault(), (a.beforeInstallEvent = e);
              }),
              window.addEventListener("appinstalled", function () {
                (a.beforeInstallEvent = null),
                  r.forEach(function (e) {
                    e.notify();
                  });
              }),
              document.addEventListener("visibilitychange", function () {
                "visible" === document.visibilityState &&
                  "clearAppBadge" in navigator &&
                  navigator.clearAppBadge();
              }),
              {
                onWindowReady: function (e) {
                  return (
                    (c.isDocumentReady &&
                      new Promise(function (t) {
                        e(), t();
                      })) ||
                    p(t, e)
                  );
                },
                onWindowResize: function (e) {
                  return p(n, e);
                },
                loadScript: function (t, n) {
                  var r = "".concat(n || e).concat(t);
                  s.has(r) ||
                    s.set(
                      r,
                      new Promise(function (r, o) {
                        var i = document.createElement("script"),
                          u = "".concat(n || e).concat(t);
                        (i.onload = function () {
                          r();
                        }),
                          (i.onerror = function (e) {
                            o(e.error);
                          }),
                          (i.src = u),
                          document.head.appendChild(i);
                      })
                    );
                  return s.get(r);
                },
                loadStyle: function (t, n) {
                  return new Promise(function (r) {
                    var o = document.createElement("link"),
                      i = "".concat(n || e).concat(t);
                    (o.onload = function () {
                      r();
                    }),
                      o.setAttribute("href", i),
                      o.setAttribute("rel", "stylesheet"),
                      document.head.appendChild(o);
                  });
                },
                notifyResizeSubscribers: v,
                assetUrl: e,
                apiUrl: "",
                isStandAloneCheck: f,
                pwaInstallIsAvailable: d,
                showPwaInstallRequest: function () {
                  var e;
                  if (!d()) return;
                  var t = a.beforeInstallEvent;
                  o.forEach(function (e) {
                    e.notify();
                  }),
                    t.prompt(),
                    null === (e = t.userChoice) ||
                      void 0 === e ||
                      e.then(function (e) {
                        return (
                          (a.beforeInstallEvent = null),
                          "accepted" === e
                            ? i.forEach(function (e) {
                                e.notify();
                              })
                            : u.forEach(function (e) {
                                e.notify();
                              })
                        );
                      });
                },
                onAppInstall: l(r),
                onAppShowPromt: l(o),
                onAppPromtAccepted: l(i),
                onAppPromtDismiss: l(u),
              }
            );
            function l(e) {
              return function (t) {
                var n = {
                  notify: function () {
                    t();
                  },
                  dispose: function () {
                    e.delete(n);
                  },
                };
                return e.add(n), n;
              };
            }
            function f() {
              var e, t;
              return (
                null !==
                  (e =
                    null === (t = window) || void 0 === t
                      ? void 0
                      : t.matchMedia("(display-mode: standalone)").matches) &&
                void 0 !== e &&
                e
              );
            }
            function d() {
              return !!a.beforeInstallEvent && !f();
            }
            function p(e, t) {
              var n = {
                handler: t,
                dispose: function () {
                  var t = e.indexOf(n);
                  if (t < 0) return;
                  e.splice(t, 1);
                },
              };
              return e.push(n), n;
            }
            function y(e, t) {
              e.forEach(function (e) {
                e.handler(t);
              });
            }
            function v() {
              for (
                var e = arguments.length, t = new Array(e), r = 0;
                r < e;
                r++
              )
                t[r] = arguments[r];
              var o = document.documentElement.getBoundingClientRect();
              n.forEach(function (e) {
                t.indexOf(e.handler) >= 0 || e.handler(o);
              }),
                y(n, o);
            }
          })());
      },
      89305: (e, t, n) => {
        "use strict";
        n.r(t), n.d(t, { default: () => u });
        var r = n(31891),
          o = n(63474),
          i = document.documentElement;
        const u = {
          processLayoutSize: function e(t) {
            var n = i.getBoundingClientRect(),
              u = o.default.wideScreenGetItem() ? 0.46 : 0.64,
              a = "layout-design-updated",
              c = "layout-design-wide-screen",
              s = "layout-portrait",
              l = "layout-landscape",
              f = n.width - 112,
              d = n.height - 56,
              p = Math.min(n.height, d) * u,
              y = Math.min(n.width, f) * u,
              v = n.width - p,
              m = n.height - y,
              h = v >= m;
            m >= 56 && (h = !1),
              i.classList.toggle(a, o.default.adaptiveGetItem()),
              i.classList.toggle(c, o.default.wideScreenGetItem()),
              i.classList.toggle(s, !h),
              i.classList.toggle(l, h),
              t || r.default.notifyResizeSubscribers(e);
          },
          updateScreenStorage: function () {
            var e =
              null === o.default.wideScreenGetItem() ||
              o.default.wideScreenGetItem();
            o.default.wideScreenSetItem(e);
            var t =
              null === o.default.adaptiveGetItem() ||
              o.default.adaptiveGetItem();
            o.default.adaptiveSetItem(t);
          },
        };
      },
      25128: (e, t, n) => {
        "use strict";
        n.r(t);
        var r,
          o = n(69442),
          i = n(31891),
          u = n(63279),
          a = n(25232),
          c = n(4691);
        function s(e) {
          return (
            (s =
              "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                ? function (e) {
                    return typeof e;
                  }
                : function (e) {
                    return e &&
                      "function" == typeof Symbol &&
                      e.constructor === Symbol &&
                      e !== Symbol.prototype
                      ? "symbol"
                      : typeof e;
                  }),
            s(e)
          );
        }
        function l(e, t, n) {
          return (
            (t = (function (e) {
              var t = (function (e, t) {
                if ("object" !== s(e) || null === e) return e;
                var n = e[Symbol.toPrimitive];
                if (void 0 !== n) {
                  var r = n.call(e, t || "default");
                  if ("object" !== s(r)) return r;
                  throw new TypeError(
                    "@@toPrimitive must return a primitive value."
                  );
                }
                return ("string" === t ? String : Number)(e);
              })(e, "string");
              return "symbol" === s(t) ? t : String(t);
            })(t)) in e
              ? Object.defineProperty(e, t, {
                  value: n,
                  enumerable: !0,
                  configurable: !0,
                  writable: !0,
                })
              : (e[t] = n),
            e
          );
        }
        var f =
          (l((r = {}), o.default.USER_INFO, function () {
            return new Promise(function (e, t) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).unshift(
                o.default.USER,
                function (n) {
                  n.User.getUserInfo()
                    .then(function (n) {
                      n.text()
                        .then(function (n) {
                          try {
                            var r = JSON.parse(n),
                              o = Object.assign({}, r, window.NXUserInfo || {});
                            (a.default.settings.isCookieSplit =
                              o.splits.isCookieSplit),
                              (a.default.settings.cookieSplitGroup =
                                o.splits.cookieSplitGroup),
                              e(o);
                          } catch (e) {
                            t(
                              "apply responce error [".concat(
                                n.substring(0, 255),
                                "]"
                              )
                            );
                          }
                        })
                        .catch(t);
                    })
                    .catch(t);
                }
              );
            });
          }),
          l(r, o.default.LOCALIZATION, function () {
            return new Promise(function (e, t) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).push(
                o.default.USER_INFO,
                function (n) {
                  var r,
                    o = window.NXLocales,
                    u =
                      (null === (r = n.UserInfo) || void 0 === r
                        ? void 0
                        : r.language) || "en";
                  i.default
                    .loadScript(
                      "/js/locale/".concat(u, "/autoGenerateTranslate.js")
                    )
                    .then(function () {
                      var t = Object.assign({}, window.NXLocales, o || {});
                      (window.NXLocales = o),
                        e(
                          new Proxy(t, {
                            get: function (e, t) {
                              return t in e
                                ? e[t]
                                : "".concat("", "::").concat(t);
                            },
                          })
                        );
                    })
                    .catch(t);
                }
              );
            });
          }),
          l(r, o.default.MAIN_METRICS, function () {
            return new Promise(function (e) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).push(
                o.default.API,
                function () {
                  return n
                    .e(3435)
                    .then(n.t.bind(n, 73435, 23))
                    .then(function (t) {
                      return e(t.default);
                    });
                }
              );
            });
          }),
          l(r, o.default.SDK_METRICS, function () {
            return new Promise(function (e) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).push(
                o.default.API,
                function () {
                  return n
                    .e(8728)
                    .then(n.t.bind(n, 38728, 23))
                    .then(function (t) {
                      return e(t.default);
                    });
                }
              );
            });
          }),
          l(r, o.default.CONSENT_UI, function () {
            return new Promise(function (e) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).push(
                o.default.API,
                o.default.LOCALIZATION,
                o.default.USER_INFO,
                function () {
                  return n
                    .e(197)
                    .then(n.t.bind(n, 20197, 23))
                    .then(function (t) {
                      return e(t.default);
                    });
                }
              );
            });
          }),
          l(r, o.default.CONSENT, function () {
            return new Promise(function (e) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).push(
                o.default.SDK_METRICS,
                o.default.CONSENT_UI,
                function (t) {
                  i.default.loadStyle("/css/sdk.css").then(function () {
                    t.ConsentUi.init("landings(sdk)"),
                      u.default.init(),
                      e(t.ConsentUi);
                  });
                }
              );
            });
          }),
          l(r, o.default.API, function () {
            return n
              .e(5792)
              .then(n.t.bind(n, 75792, 23))
              .then(function (e) {
                return e.default;
              });
          }),
          l(r, o.default.USER, function () {
            var e = i.default.apiUrl.slice(0, -1) + "/user/info",
              t = {
                accept: "application/json",
                "Content-Type": "application/json; charset=UTF-8",
              };
            return Promise.resolve({
              getUserInfo: function () {
                return fetch(e, { headers: t });
              },
              updateUserInfo: function (t) {
                return fetch(e, {
                  method: "POST",
                  body: JSON.stringify(t),
                  creadentials: "include",
                  headers: {
                    accept: "application/json",
                    "Content-Type": "application/json; charset=UTF-8",
                    "x-xsrf-token":
                      ((n = document.cookie.match(
                        new RegExp(
                          "(?:^|; )" +
                            "XSRF-TOKEN".replace(
                              /([.$?*|{}()[\]\\/+^])/g,
                              "\\$1"
                            ) +
                            "=([^;]*)"
                        )
                      )),
                      n ? decodeURIComponent(n[1]) : ""),
                  },
                });
                var n;
              },
            });
          }),
          l(r, o.default.AUTH, function () {
            return new Promise(function (e) {
              (window.NXSDKSetup || (window.NXSDKSetup = [])).push(
                o.default.API,
                o.default.LOCALIZATION,
                o.default.USER_INFO,
                function () {
                  n.e(7706)
                    .then(n.t.bind(n, 17706, 23))
                    .then(function (t) {
                      return e(t.default);
                    });
                }
              );
            });
          }),
          r);
        window.NXSDK || (window.NXSDK = {}),
          c.default.init({
            pagelive: i.default,
            metrics: u.default,
            consent: a.default,
            resolvers: f,
          });
      },
      59382: (e, t, n) => {
        function r(e, t) {
          var n =
            ("undefined" != typeof Symbol && e[Symbol.iterator]) ||
            e["@@iterator"];
          if (!n) {
            if (
              Array.isArray(e) ||
              (n = (function (e, t) {
                if (!e) return;
                if ("string" == typeof e) return o(e, t);
                var n = Object.prototype.toString.call(e).slice(8, -1);
                "Object" === n && e.constructor && (n = e.constructor.name);
                if ("Map" === n || "Set" === n) return Array.from(e);
                if (
                  "Arguments" === n ||
                  /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)
                )
                  return o(e, t);
              })(e)) ||
              (t && e && "number" == typeof e.length)
            ) {
              n && (e = n);
              var r = 0,
                i = function () {};
              return {
                s: i,
                n: function () {
                  return r >= e.length
                    ? { done: !0 }
                    : { done: !1, value: e[r++] };
                },
                e: function (e) {
                  throw e;
                },
                f: i,
              };
            }
            throw new TypeError(
              "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."
            );
          }
          var u,
            a = !0,
            c = !1;
          return {
            s: function () {
              n = n.call(e);
            },
            n: function () {
              var e = n.next();
              return (a = e.done), e;
            },
            e: function (e) {
              (c = !0), (u = e);
            },
            f: function () {
              try {
                a || null == n.return || n.return();
              } finally {
                if (c) throw u;
              }
            },
          };
        }
        function o(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
          return r;
        }
        n(65606).env.DEV_TOOLS &&
          document.documentElement.addEventListener(
            "contextmenu",
            function (e) {
              var t,
                n = r(e.path || (e.composedPath && e.composedPath()));
              try {
                for (n.s(); !(t = n.n()).done; ) {
                  if (t.value instanceof HTMLCanvasElement)
                    return void e.preventDefault();
                }
              } catch (e) {
                n.e(e);
              } finally {
                n.f();
              }
            },
            !0
          );
      },
      38117: () => {
        (Element.prototype._addEventListener =
          Element.prototype.addEventListener),
          (Element.prototype._removeEventListener =
            Element.prototype.removeEventListener),
          (Element.prototype.addEventListener = function (e, t) {
            var n =
              arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
            this._addEventListener(e, t, n),
              this.eventListenerList || (this.eventListenerList = {}),
              this.eventListenerList[e] || (this.eventListenerList[e] = []),
              this.eventListenerList[e].push({
                type: e,
                listener: t,
                useCapture: n,
              });
          }),
          (Element.prototype.removeEventListener = function (e, t) {
            var n =
              arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
            this._removeEventListener(e, t, n),
              this.eventListenerList || (this.eventListenerList = {}),
              this.eventListenerList[e] || (this.eventListenerList[e] = []);
            for (var r = 0; r < this.eventListenerList[e].length; r++)
              if (
                this.eventListenerList[e][r].listener === t &&
                this.eventListenerList[e][r].useCapture === n
              ) {
                this.eventListenerList[e].splice(r, 1);
                break;
              }
            0 == this.eventListenerList[e].length &&
              delete this.eventListenerList[e];
          }),
          (Element.prototype.getEventListeners = function (e) {
            return (
              this.eventListenerList || (this.eventListenerList = {}),
              void 0 === e ? this.eventListenerList : this.eventListenerList[e]
            );
          }),
          window.addEventListener(
            "touchstart",
            function (e) {
              var t = (function () {
                  var e =
                      Math.round(
                        (document.documentElement.clientWidth /
                          window.innerWidth) *
                          100
                      ) / 100,
                    t = Math.abs(1 - e) > 1e-5;
                  return t;
                })(),
                n = document.getElementById("flash-content"),
                r = !t || !n || e.touches < 2,
                o = ["touchstart", "touchmove"],
                i = {};
              if (r) return;
              (function () {
                for (var e = n.getEventListeners(), t = 0; t < o.length; ++t) {
                  var r = o[t],
                    u = e[r];
                  if (u)
                    for (
                      var a = i[r] || (i[r] = []), c = 0;
                      c < u.length;
                      ++c
                    ) {
                      var s = u[c],
                        l = s.listener,
                        f = s.useCapture;
                      a.push(s), n.removeEventListener(r, l, f);
                    }
                }
              })(),
                window.addEventListener(
                  "touchend",
                  function e() {
                    !(function () {
                      for (var e in i) {
                        for (var t = i[e], r = 0; r < t.length; ++r) {
                          var o = t[r],
                            u = o.listener,
                            a = o.useCapture;
                          n.addEventListener(e, u, a);
                        }
                        delete i[e];
                      }
                    })(),
                      window.removeEventListener("touchend", e, !0);
                  },
                  !0
                );
            },
            !0
          );
      },
      49418: (e, t, n) => {
        "use strict";
        n.r(t);
        n(59382), n(38117);
      },
      65606: (e) => {
        var t,
          n,
          r = (e.exports = {});
        function o() {
          throw new Error("setTimeout has not been defined");
        }
        function i() {
          throw new Error("clearTimeout has not been defined");
        }
        function u(e) {
          if (t === setTimeout) return setTimeout(e, 0);
          if ((t === o || !t) && setTimeout)
            return (t = setTimeout), setTimeout(e, 0);
          try {
            return t(e, 0);
          } catch (n) {
            try {
              return t.call(null, e, 0);
            } catch (n) {
              return t.call(this, e, 0);
            }
          }
        }
        !(function () {
          try {
            t = "function" == typeof setTimeout ? setTimeout : o;
          } catch (e) {
            t = o;
          }
          try {
            n = "function" == typeof clearTimeout ? clearTimeout : i;
          } catch (e) {
            n = i;
          }
        })();
        var a,
          c = [],
          s = !1,
          l = -1;
        function f() {
          s &&
            a &&
            ((s = !1),
            a.length ? (c = a.concat(c)) : (l = -1),
            c.length && d());
        }
        function d() {
          if (!s) {
            var e = u(f);
            s = !0;
            for (var t = c.length; t; ) {
              for (a = c, c = []; ++l < t; ) a && a[l].run();
              (l = -1), (t = c.length);
            }
            (a = null),
              (s = !1),
              (function (e) {
                if (n === clearTimeout) return clearTimeout(e);
                if ((n === i || !n) && clearTimeout)
                  return (n = clearTimeout), clearTimeout(e);
                try {
                  return n(e);
                } catch (t) {
                  try {
                    return n.call(null, e);
                  } catch (t) {
                    return n.call(this, e);
                  }
                }
              })(e);
          }
        }
        function p(e, t) {
          (this.fun = e), (this.array = t);
        }
        function y() {}
        (r.nextTick = function (e) {
          var t = new Array(arguments.length - 1);
          if (arguments.length > 1)
            for (var n = 1; n < arguments.length; n++) t[n - 1] = arguments[n];
          c.push(new p(e, t)), 1 !== c.length || s || u(d);
        }),
          (p.prototype.run = function () {
            this.fun.apply(null, this.array);
          }),
          (r.title = "browser"),
          (r.browser = !0),
          (r.env = {}),
          (r.argv = []),
          (r.version = ""),
          (r.versions = {}),
          (r.on = y),
          (r.addListener = y),
          (r.once = y),
          (r.off = y),
          (r.removeListener = y),
          (r.removeAllListeners = y),
          (r.emit = y),
          (r.prependListener = y),
          (r.prependOnceListener = y),
          (r.listeners = function (e) {
            return [];
          }),
          (r.binding = function (e) {
            throw new Error("process.binding is not supported");
          }),
          (r.cwd = function () {
            return "/";
          }),
          (r.chdir = function (e) {
            throw new Error("process.chdir is not supported");
          }),
          (r.umask = function () {
            return 0;
          });
      },
      82558: (e, t, n) => {
        "use strict";
        var r = new Error();
        e.exports = new Promise((e, t) => {
          if ("undefined" != typeof apps) return e();
          n.l(
            "./akamaihd/apps.js",
            (n) => {
              if ("undefined" != typeof apps) return e();
              var o = n && ("load" === n.type ? "missing" : n.type),
                i = n && n.target && n.target.src;
              (r.message = "Loading script failed.\n(" + o + ": " + i + ")"),
                (r.name = "ScriptExternalLoadError"),
                (r.type = o),
                (r.request = i),
                t(r);
            },
            "apps"
          );
        }).then(() => apps);
      },
    },
    a = {};
  function c(e) {
    var t = a[e];
    if (void 0 !== t) return t.exports;
    var n = (a[e] = { exports: {} });
    return u[e](n, n.exports, c), n.exports;
  }
  (c.m = u),
    (c.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return c.d(t, { a: t }), t;
    }),
    (t = Object.getPrototypeOf
      ? (e) => Object.getPrototypeOf(e)
      : (e) => e.__proto__),
    (c.t = function (n, r) {
      if ((1 & r && (n = this(n)), 8 & r)) return n;
      if ("object" == typeof n && n) {
        if (4 & r && n.__esModule) return n;
        if (16 & r && "function" == typeof n.then) return n;
      }
      var o = Object.create(null);
      c.r(o);
      var i = {};
      e = e || [null, t({}), t([]), t(t)];
      for (var u = 2 & r && n; "object" == typeof u && !~e.indexOf(u); u = t(u))
        Object.getOwnPropertyNames(u).forEach((e) => (i[e] = () => n[e]));
      return (i.default = () => n), c.d(o, i), o;
    }),
    (c.d = (e, t) => {
      for (var n in t)
        c.o(t, n) &&
          !c.o(e, n) &&
          Object.defineProperty(e, n, { enumerable: !0, get: t[n] });
    }),
    (c.f = {}),
    (c.e = (e) =>
      Promise.all(Object.keys(c.f).reduce((t, n) => (c.f[n](e, t), t), []))),
    (c.u = (e) =>
      3435 === e
        ? "js/3435.js"
        : 8728 === e
        ? "js/8728.js"
        : 197 === e
        ? "js/197.js"
        : 5792 === e
        ? "js/5792.js"
        : 7706 === e
        ? "js/7706.js"
        : 3800 === e
        ? "js/3800.js"
        : void 0),
    (c.miniCssF = (e) => {}),
    (c.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (c.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t)),
    (n = {}),
    (r = "nx-hw-web:"),
    (c.l = (e, t, o, i) => {
      if (n[e]) n[e].push(t);
      else {
        var u, a;
        if (void 0 !== o)
          for (
            var s = document.getElementsByTagName("script"), l = 0;
            l < s.length;
            l++
          ) {
            var f = s[l];
            if (
              f.getAttribute("src") == e ||
              f.getAttribute("data-webpack") == r + o
            ) {
              u = f;
              break;
            }
          }
        u ||
          ((a = !0),
          ((u = document.createElement("script")).charset = "utf-8"),
          (u.timeout = 120),
          c.nc && u.setAttribute("nonce", c.nc),
          u.setAttribute("data-webpack", r + o),
          (u.src = e)),
          (n[e] = [t]);
        var d = (t, r) => {
            (u.onerror = u.onload = null), clearTimeout(p);
            var o = n[e];
            if (
              (delete n[e],
              u.parentNode && u.parentNode.removeChild(u),
              o && o.forEach((e) => e(r)),
              t)
            )
              return t(r);
          },
          p = setTimeout(
            d.bind(null, void 0, { type: "timeout", target: u }),
            12e4
          );
        (u.onerror = d.bind(null, u.onerror)),
          (u.onload = d.bind(null, u.onload)),
          a && document.head.appendChild(u);
      }
    }),
    (c.r = (e) => {
      "undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 });
    }),
    (o = {
      197: [20197],
      3435: [73435],
      3800: [3800],
      5792: [75792],
      7706: [17706],
      8728: [38728],
    }),
    (i = {
      3800: ["default", "./game", 82558],
      17706: ["default", "./nx_sdk_auth", 82558],
      20197: ["default", "./consent_ui", 82558],
      38728: ["default", "./sdk_metrics", 82558],
      73435: ["default", "./main_metrics", 82558],
      75792: ["default", "./nx_sdk_api", 82558],
    }),
    (c.f.remotes = (e, t) => {
      c.o(o, e) &&
        o[e].forEach((e) => {
          var n = c.R;
          n || (n = []);
          var r = i[e];
          if (!(n.indexOf(r) >= 0)) {
            if ((n.push(r), r.p)) return t.push(r.p);
            var o = (t) => {
                t || (t = new Error("Container missing")),
                  "string" == typeof t.message &&
                    (t.message +=
                      '\nwhile loading "' + r[1] + '" from ' + r[2]),
                  (c.m[e] = () => {
                    throw t;
                  }),
                  (r.p = 0);
              },
              u = (e, n, i, u, a, c) => {
                try {
                  var s = e(n, i);
                  if (!s || !s.then) return a(s, u, c);
                  var l = s.then((e) => a(e, u), o);
                  if (!c) return l;
                  t.push((r.p = l));
                } catch (e) {
                  o(e);
                }
              },
              a = (e, t, o) => u(t.get, r[1], n, 0, s, o),
              s = (t) => {
                (r.p = 1),
                  (c.m[e] = (e) => {
                    e.exports = t();
                  });
              };
            u(
              c,
              r[2],
              0,
              0,
              (e, t, n) => (e ? u(c.I, r[0], 0, e, a, n) : o()),
              1
            );
          }
        });
    }),
    (() => {
      var e = {
          197: [20197],
          3435: [73435],
          3800: [3800],
          5792: [75792],
          7706: [17706],
          8728: [38728],
        },
        t = {
          3800: ["default", "./game", 82558],
          17706: ["default", "./nx_sdk_auth", 82558],
          20197: ["default", "./consent_ui", 82558],
          38728: ["default", "./sdk_metrics", 82558],
          73435: ["default", "./main_metrics", 82558],
          75792: ["default", "./nx_sdk_api", 82558],
        };
      c.f.remotes = (n, r) => {
        c.o(e, n) &&
          e[n].forEach((e) => {
            var n = c.R;
            n || (n = []);
            var o = t[e];
            if (!(n.indexOf(o) >= 0)) {
              if ((n.push(o), o.p)) return r.push(o.p);
              var i = (t) => {
                  t || (t = new Error("Container missing")),
                    "string" == typeof t.message &&
                      (t.message +=
                        '\nwhile loading "' + o[1] + '" from ' + o[2]),
                    (c.m[e] = () => {
                      throw t;
                    }),
                    (o.p = 0);
                },
                u = (e, t, n, u, a, c) => {
                  try {
                    var s = e(t, n);
                    if (!s || !s.then) return a(s, u, c);
                    var l = s.then((e) => a(e, u), i);
                    if (!c) return l;
                    r.push((o.p = l));
                  } catch (e) {
                    i(e);
                  }
                },
                a = (e, t, r) => u(t.get, o[1], n, 0, s, r),
                s = (t) => {
                  (o.p = 1),
                    (c.m[e] = (e) => {
                      e.exports = t();
                    });
                };
              u(
                c,
                o[2],
                0,
                0,
                (e, t, n) => (e ? u(c.I, o[0], 0, e, a, n) : i()),
                1
              );
            }
          });
      };
    })(),
    (() => {
      var e = {
          197: [20197],
          3435: [73435],
          3800: [3800],
          5792: [75792],
          7706: [17706],
          8728: [38728],
        },
        t = {
          3800: ["default", "./game", 82558],
          17706: ["default", "./nx_sdk_auth", 82558],
          20197: ["default", "./consent_ui", 82558],
          38728: ["default", "./sdk_metrics", 82558],
          73435: ["default", "./main_metrics", 82558],
          75792: ["default", "./nx_sdk_api", 82558],
        };
      c.f.remotes = (n, r) => {
        c.o(e, n) &&
          e[n].forEach((e) => {
            var n = c.R;
            n || (n = []);
            var o = t[e];
            if (!(n.indexOf(o) >= 0)) {
              if ((n.push(o), o.p)) return r.push(o.p);
              var i = (t) => {
                  t || (t = new Error("Container missing")),
                    "string" == typeof t.message &&
                      (t.message +=
                        '\nwhile loading "' + o[1] + '" from ' + o[2]),
                    (c.m[e] = () => {
                      throw t;
                    }),
                    (o.p = 0);
                },
                u = (e, t, n, u, a, c) => {
                  try {
                    var s = e(t, n);
                    if (!s || !s.then) return a(s, u, c);
                    var l = s.then((e) => a(e, u), i);
                    if (!c) return l;
                    r.push((o.p = l));
                  } catch (e) {
                    i(e);
                  }
                },
                a = (e, t, r) => u(t.get, o[1], n, 0, s, r),
                s = (t) => {
                  (o.p = 1),
                    (c.m[e] = (e) => {
                      e.exports = t();
                    });
                };
              u(
                c,
                o[2],
                0,
                0,
                (e, t, n) => (e ? u(c.I, o[0], 0, e, a, n) : i()),
                1
              );
            }
          });
      };
    })(),
    (() => {
      c.S = {};
      var e = {},
        t = {};
      c.I = (n, r) => {
        r || (r = []);
        var o = t[n];
        if ((o || (o = t[n] = {}), !(r.indexOf(o) >= 0))) {
          if ((r.push(o), e[n])) return e[n];
          c.o(c.S, n) || (c.S[n] = {});
          c.S[n];
          var i = [];
          if ("default" === n)
            ((e) => {
              var t = (e) => {
                return (
                  (t = "Initialization of sharing external failed: " + e),
                  void (
                    "undefined" != typeof console &&
                    console.warn &&
                    console.warn(t)
                  )
                );
                var t;
              };
              try {
                var o = c(e);
                if (!o) return;
                var u = (e) => e && e.init && e.init(c.S[n], r);
                if (o.then) return i.push(o.then(u, t));
                var a = u(o);
                if (a && a.then) return i.push(a.catch(t));
              } catch (e) {
                t(e);
              }
            })(82558);
          return i.length
            ? (e[n] = Promise.all(i).then(() => (e[n] = 1)))
            : (e[n] = 1);
        }
      };
    })(),
    (() => {
      var e;
      c.g.importScripts && (e = c.g.location + "");
      var t = c.g.document;
      if (
        !e &&
        t &&
        (t.currentScript &&
          "SCRIPT" === t.currentScript.tagName.toUpperCase() &&
          (e = t.currentScript.src),
        !e)
      ) {
        var n = t.getElementsByTagName("script");
        if (n.length)
          for (var r = n.length - 1; r > -1 && (!e || !/^http(s?):/.test(e)); )
            e = n[r--].src;
      }
      if (!e)
        throw new Error(
          "Automatic publicPath is not supported in this browser"
        );
      (e = e
        .replace(/#.*$/, "")
        .replace(/\?.*$/, "")
        .replace(/\/[^\/]+$/, "/")),
        (c.p = e + "../../");
    })(),
    (() => {
      var e = { 2420: 0 };
      c.f.j = (t, n) => {
        var r = c.o(e, t) ? e[t] : void 0;
        if (0 !== r)
          if (r) n.push(r[2]);
          else if (2420 == t) {
            var o = new Promise((n, o) => (r = e[t] = [n, o]));
            n.push((r[2] = o));
            var i = c.p + c.u(t),
              u = new Error();
            c.l(
              i,
              (n) => {
                if (c.o(e, t) && (0 !== (r = e[t]) && (e[t] = void 0), r)) {
                  var o = n && ("load" === n.type ? "missing" : n.type),
                    i = n && n.target && n.target.src;
                  (u.message =
                    "Loading chunk " + t + " failed.\n(" + o + ": " + i + ")"),
                    (u.name = "ChunkLoadError"),
                    (u.type = o),
                    (u.request = i),
                    r[1](u);
                }
              },
              "chunk-" + t,
              t
            );
          } else e[t] = 0;
      };
      var t = (t, n) => {
          var r,
            o,
            [i, u, a] = n,
            s = 0;
          if (i.some((t) => 0 !== e[t])) {
            for (r in u) c.o(u, r) && (c.m[r] = u[r]);
            if (a) a(c);
          }
          for (t && t(n); s < i.length; s++)
            (o = i[s]), c.o(e, o) && e[o] && e[o][0](), (e[o] = 0);
        },
        n = (self.webpackChunknx_hw_web = self.webpackChunknx_hw_web || []);
      n.forEach(t.bind(null, 0)), (n.push = t.bind(null, n.push.bind(n)));
    })();
  var s = {};
  (() => {
    "use strict";
    c.r(s);
    c(49418), c(25128);
    var e,
      t,
      n = c(69442),
      r = c(89305);
    (window.consent.settings.isCookieSplit =
      null === (e = window.NXAppInfo) || void 0 === e
        ? void 0
        : e.isCookieSplit),
      (window.consent.settings.cookieSplitGroup =
        null === (t = window.NXAppInfo) || void 0 === t
          ? void 0
          : t.cookieSplitGroup);
    var o = document.documentElement,
      i = "" + window.NXFlashVars.playableIsEnabled == "true",
      u = window.NXFlashVars.preloaderOverlayPlayable,
      a = i && u;
    o.classList.toggle("playable_prepare", a),
      r.default.updateScreenStorage(),
      r.default.processLayoutSize(),
      window.visualViewport.addEventListener(
        "resize",
        r.default.processLayoutSize,
        !0
      ),
      (NXSDK.UserInfo = Object.assign({}, window.NXUserInfo)),
      NXSDKSetup.push(n.default.LOCALIZATION, n.default.AUTH, function () {
        window.gamePage ||
          (window.gamePage =
            (c
              .e(3800)
              .then(c.t.bind(c, 3800, 23))
              .finally(function () {
                window.metrics.init();
              }),
            !0));
      });
  })();
})();
