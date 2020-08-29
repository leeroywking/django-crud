from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.


class BlogTests(TestCase):
    def test_home_page_status(self):
        self.helper_status_code_200("home")

    def test_blog_page_status(self):
        self.helper_status_code_200("blog")

    def test_blog_template_used(self):
        url = reverse("blog")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "blog.html")

    def helper_status_code_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
