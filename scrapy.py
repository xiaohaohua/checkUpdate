import requests
from bs4 import BeautifulSoup
import time
import textMyself
import re
import json
import datetime

filename = 'myNovelData.json'
try:
    with open(filename, 'r') as fileObj:
        lengthofcontents = json.load(fileObj)
except FileNotFoundError:
    with open(filename, 'w') as fileObj:
        json.dump(0, fileObj)
    lengthofcontents = 0

url = 'http://book.qidian.com/info/1004608738#Catalog'
status = True
n = 1
regex1 = re.compile("^(//read.qidian.com)")
regex2 = re.compile("^(//vipreader.qidian.com)")

while True:
    try:
        dt = datetime.datetime.now()
        print(dt, end='')
        print('  执行第 %s 次检查小说更新' % n)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        dirct1 = soup.find_all("a", {"href": regex1})
        dirct2 = soup.find_all("a", {"href": regex2})
        dircts = dirct1 + dirct2
        if len(dircts) > lengthofcontents:
            contents = dircts
            with open(filename, 'w') as fileObj:
                json.dump(len(contents), fileObj)
            print('小说已更新...正在发送短信...')
            break
    except Exception as e:
        status = False
        print('检查更新出现异常')
        print(e.__traceback__)
        try:
            textMyself.text_myself('检查小说更新程序出现异常')
            print('警告短信已发送')
        except Exception as e:
            print('发送警告短信失败')
            print(e.__traceback__)
        break
    n += 1
    print('小说未更新，5分钟后再次检查')
    time.sleep(300)

if status is True:
    try:
        textMyself.text_myself('小说已更新')
        print('短信已发送，小说更新检查完毕')
    except Exception as e:
        print('发送更新出现异常')
        print(e.__traceback__)
