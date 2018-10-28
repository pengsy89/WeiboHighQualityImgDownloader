import sys
import time
import requests
import json
import re
import random
import logging
import threading
from bs4 import BeautifulSoup as BS4
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    weibo(sys.argv[1], sys.argv[2])
    # for arg in sys.argv[1:]:
    #     print (arg)


def weibo(file_root, weibo_id):
    url = "https://m.weibo.cn/statuses/show?id=" + weibo_id
    response = requests.get(url)
    raw_text = response.text
    after_json_parse = json.loads(raw_text)
    if "pics" in after_json_parse["data"]:
        pics = after_json_parse["data"]["pics"]
        for i in pics:
            large_url = i["large"]["url"]
            file_name=large_url.split(r"/")
            file = file_root + "/" + file_name[4]
            print(file)
            createNewDownloadThread(large_url, file)


def download(link, filelocation):
    r = requests.get(link, stream=True)
    with open(filelocation, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)


def createNewDownloadThread(link, filelocation):
    download_thread = threading.Thread(
        target=download, args=(link, filelocation))
    download_thread.start()

if __name__ == "__main__":
    main()
    # weibo("d:\\d\\", "4298984039923256")