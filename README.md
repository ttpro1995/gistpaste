Git Paste

A simple Python program let you "paste" any binary file

Dependencies:

```
requests
```

Usage

```
# upload a file to gist.github.com
main.py ./test/testfile.pdf
https://gist.github.com/85561d0560b3da76feb8e8fa4c0beb7f
# link is print to console

# download file from gist and decode to binary file
python main.py https://gist.github.com/85561d0560b3da76feb8e8fa4c0beb7f

```