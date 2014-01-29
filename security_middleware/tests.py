
from django.test import TestCase
from django.test import Client


class SecurityMiddlewareTestCase(TestCase):

    def setUp(self):
        self.client = Client(HTTP_X_FORWARDED_PROTOCOL='https')

    def test_csp(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 301)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('Content-Security-Policy' in response)
        self.assertTrue("default-src 'none';" in response['Content-Security-Policy'])

    def test_xss_protection(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('X-XSS-Protection' in response)
        self.assertEqual(response['X-XSS-Protection'], '1; mode=block')

    def test_nosniff(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('X-Content-Type-Options' in response)
        self.assertEqual(response['X-Content-Type-Options'], 'nosniff')

    def test_ssl(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('Strict-Transport-Security' in response)
