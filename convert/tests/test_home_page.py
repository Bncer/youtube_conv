from django.test import TestCase


class TemplateTests(TestCase):

    def test_home_page_status_cols(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Enter youtube url</h1>')

    def test_home_page_post_request(self):
        response = self.client.post('/', {'url': 'url'})
        self.assertEquals(response.status_code, 200)









