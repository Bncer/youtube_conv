from django.test import TestCase
from unittest.mock import patch, MagicMock
from .models import History
from convert.service import *


class TemplateTests(TestCase):
    @patch('convert.service.youtube_dl')
    def test_download_youdl(self, mocked_youtube):
        #ls
        #response = self.client.post('/', {'url': 'url'})
        youdl_manage('url')
        mocked_youtube.YoutubeDL.assert_called_once()

        #check_history = History.objects.all()
        #self.assertEquals(response, 'downloaded')
        #self.assertEquals(check_history, 'downloaded')

