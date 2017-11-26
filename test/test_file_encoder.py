import unittest
from gistpaste import FileEncoder
import hashlib


class TestFileEncoder(unittest.TestCase):

    def test_encode_decode(self):
        content = FileEncoder.encode_file_to_text("./testfile.pdf")
        FileEncoder.decode_text_to_file(content, "./testfile_decode.pdf")
        source_file = hashlib.md5(open('./testfile.pdf', 'rb').read()).hexdigest()
        result_file = hashlib.md5(open('./testfile_decode.pdf', 'rb').read()).hexdigest()
        assert source_file == result_file
