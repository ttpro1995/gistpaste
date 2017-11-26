from gistpaste import GistApi
from gistpaste import FileEncoder
import os
class GistPaste:

    """Wrapper for gist api"""
    def __init__(self, client_id = None, client_secret= None):
        """
        :param client_id: client_id on gist
        :param client_secret: client_secret on gist
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.gistapi = GistApi(self.client_id, self.client_secret)

    def upload(self, filepath):
        """
        encode file to base64
        upload to gist
        :param filepath:
        :return: gist url
        """

        # encode file to base64
        file_content = FileEncoder.encode_file_to_text(filepath)

        # upload to gist
        filename = os.path.basename(filepath) + '.txt'
        url = self.gistapi.upload(file_content, name=filename)
        return url

    def download(self, url, filedir):
        """
        download file from url
        decode file to binary
        :param url: gist url
        :param filedir: save file to directory
        :return: gist url
        """

        # encode file to base64
        files_data = self.gistapi.download(url)

        for filename, content in files_data:
            real_file_name = filename[:-4] # remove .txt
            FileEncoder.decode_text_to_file(content, os.path.join(filedir, real_file_name))
