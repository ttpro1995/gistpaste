import unittest
from gistpaste import GistPaste
import hashlib


class TestGistPaste(unittest.TestCase):

    def setUp(self):
        self.gist_paste = GistPaste()
        self.gist_api = self.gist_paste.gistapi

    def test_upload_file(self):
        gist_url = self.gist_paste.upload("./testfile.pdf")
        print(gist_url)

    # https://gist.github.com/cf2c34fb1d4de050de305ad034ca6015

    def test_download_file(self):
        url = self.gist_paste.upload("./testfile.pdf")
        self.gist_paste.download(url= url, filedir="./download")
        source_file = hashlib.md5(open('./testfile.pdf', 'rb').read()).hexdigest()
        result_file = hashlib.md5(open('./download/testfile.pdf', 'rb').read()).hexdigest()
        assert source_file == result_file
