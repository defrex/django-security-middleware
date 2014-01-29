[![Build Status](https://travis-ci.org/defrex/django-security-middleware.png)](https://travis-ci.org/defrex/django-security-middleware)

### Django Security Middleware

This is some middleware I use for my own projects. You're welcome to it if you'd
like.

#### SSL Middleware

`security_middleware.middleware.SSLMiddleware`

This middleware does two things. One, any non-https requests will get a 301 to
the https version of the same URL. And two, it adds a
`Strict-Transport-Security` header to all requests with a 1 year max age.

It can be disabled with the `SSL_ENABLED` setting.

#### Content Security Policy Middleware

`security_middleware.middleware.ContentSecurityPolicyMiddleware`

This middleware adds the `Content-Security-Policy` header. For more information,
[html5rocks has a good tutorial](http://www.html5rocks.com/en/tutorials/security/content-security-policy/).

The exact rules are governed in settings like so:

    CSP_HEADER = {
        "default-src": ("https:", "'self'"),
        "img-src": ("https://cdn.example.com",),
    }

and so forth. Don't forget items that need to be quoted in the header need to
be double quoted in the setting `"'like this'"`.

#### XSS Protection Middleware

`security_middleware.middleware.XSSProtectionMiddleware`

Adds the header `X-XSS-Protection: 1; mode=block` to all requests.

#### No Sniff Middleware

`security_middleware.middleware.NoSniffMiddleware`

Adds the header `X-Content-Type-Options: nosniff` to all requests.

Tips welcome. :) [13q4ZK9BgR4ZhKq27KmkuaEkay1GBEoUuS](https://coinbase.com/checkouts/5235423fe479cfc415f33635f75212fe)
