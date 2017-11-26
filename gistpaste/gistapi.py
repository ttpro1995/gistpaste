import requests
import json


class GistApi:
    """Wrapper for gist api"""
    def __init__(self, client_id=None, client_secret=None):
        """
        :param client_id: client_id on gist
        :param client_secret: client_secret on gist
        """
        self.client_id = client_id
        self.client_secret = client_secret

    def upload(self, content, name="meow", description=""):
        """
        Upload your log to gist
        :param content: content of gist file
        :param name: file name on gist
        :param description: description on gist
        :return:
        """
        """
        {
          "description": "the description for this gist",
          "public": false,
          "files": {
            "file1.txt": {
              "content": "String file contents"
            }
          }
        }
        """
        "?client_id=xxxx&client_secret=yyyy"
        file_content = content
        gist_obj = dict()
        gist_obj['description'] = description
        gist_obj['public'] = False
        gist_obj['files'] = {}
        gist_obj['files'][name] = {}
        gist_obj['files'][name]['content'] = file_content
        json_string = json.dumps(gist_obj)
        params = {'client_id': self.client_id, 'client_secret': self.client_secret}
        r = requests.post('https://api.github.com/gists', data=json_string, params=params)
        response = json.loads(r.content)
        html_url = response['html_url']
        return html_url

    def download(self, url):
        """

        :param url: gist url from upload function
        :return:
        """
        id = url.split('/')[-1]
        params = {'client_id': self.client_id, 'client_secret': self.client_secret}
        r = requests.get('https://api.github.com/gists/'+id, params=params)
        response = json.loads(r.content)
        files = response['files']
        files_data = []
        for filename in files:
            file_content = requests.get(files[filename]['raw_url']).text
            files_data.append((filename, file_content))
        return files_data
