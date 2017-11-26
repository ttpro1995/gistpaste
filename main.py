import sys
import os
sys.path.append(os.getcwd())
from gistpaste import GistPaste


if __name__ == "__main__":
    only_args = sys.argv[1]
    gist_paste = GistPaste()
    if only_args[:8] == "https://" or only_args[:7] == "http://":
        gist_paste.download(only_args, '.')
        print("download complete")
    else:
        url = gist_paste.upload(only_args)
        print(url)
