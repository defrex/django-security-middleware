
from django.http import HttpResponsePermanentRedirect
from django.conf import settings


SSL_ENABLED = getattr(settings, 'SSL_ENABLED', True)

CSP_HEADER = getattr(settings, 'CSP_HEADER', {'default-src': ["'none'"]})
CSP_VALUE = ''
for key, values in CSP_HEADER.items():
    CSP_VALUE += key + ' ' + ' '.join(values) + '; '


class SSLMiddleware(object):
    def process_request(self, request):
        if SSL_ENABLED and not request.is_secure():
            return HttpResponsePermanentRedirect(request.build_absolute_uri())

    def process_response(self, request, response):
        if SSL_ENABLED:
            response['Strict-Transport-Security'] = 'max-age:{0}'.format(
                60 * 60 * 24 * 30 * 12 # 1 year
            )
        return response


class ContentSecurityPolicyMiddleware(object):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = CSP_VALUE
        return response


class XSSProtectionMiddleware(object):
    def process_response(self, request, response):
        response['X-XSS-Protection'] = '1; mode=block'
        return response


class NoSniffMiddleware(object):
    def process_response(self, request, response):
        response['X-Content-Type-Options'] = 'nosniff'
        return response
