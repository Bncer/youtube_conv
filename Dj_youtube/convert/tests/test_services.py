from django.test import TestCase
from unittest.mock import patch, MagicMock

from convert.service import youdl_manage
from convert.models import  History


class TemplateTests(TestCase):
    @patch('convert.service.youtube_dl')
    def test_download_youdl(self, mocked_youtube):
        youdl_manage('url')
        mocked_youtube.YoutubeDL.assert_called_once()
        youtube_object = History.objects.get(history_url="url")
        print(youtube_object)
        #check_history = History.objects.all()
        #self.assertEquals(response, 'downloaded')
        #self.assertEquals(check_history, 'downloaded')

