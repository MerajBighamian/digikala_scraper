from rest_framework.test import APITestCase
from django.urls import reverse
# Using the standard RequestFactory API to create a form POST request

class UrlTestCase(APITestCase):
    url = reverse("apis:index")
    def test_url_pass(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com/search/category-mobile-phone/product-list/?page=1"})
        self.assertEqual(200, response.status_code)
    
    def test_url_pass2(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com/search/category-mobile-phone/product-list/?page=12"})
        self.assertEqual(200, response.status_code)

    def test_url_pass3(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com/search/category-mobile-phone/product-list/?page=15"})
        self.assertEqual(200, response.status_code)

    def test_url_pass4(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com/search/category-mobile-phone/product-list/?page=13"})
        self.assertEqual(200, response.status_code)
    
    # fail test
    def test_url_fail(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com/search/category-mobile-phone/?page"})
        self.assertEqual(200, response.status_code)
    
    def test_url_fail2(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com//?page"})
        self.assertEqual(200, response.status_code)

    def test_url_fail3(self):
        response = self.client.post(self.url, {"url": "https://www.digikala.com/search/category-mobile-phone/?page="})
        self.assertEqual(200, response.status_code)

    def test_url_fail4(self):
        response = self.client.post(self.url, {"url": "://www.digikala.com/search/category-mobile-phone/?page"})
        self.assertEqual(200, response.status_code) 

    def test_url_fail5(self):
        response = self.client.post(self.url, {"url": "https://www.dg.com/search/category-mobile-phone/?page="})
        self.assertEqual(200, response.status_code)