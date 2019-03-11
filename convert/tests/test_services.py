from django.test import TestCase
from unittest.mock import patch, MagicMock

from convert.service import youdl_manage
from convert.models import History


class TemplateTests(TestCase):
    @patch('convert.service.youtube_dl')
    def test_download_youdl(self, mocked_youtube):
        youdl_manage('url')
        youtube_object = History.objects.create(history_url="url")
        url_to_check = youtube_object.history_url
        mocked_youtube.YoutubeDL.assert_called_once()
        self.assertEquals(url_to_check, 'url')

