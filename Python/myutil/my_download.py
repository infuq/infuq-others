import os

'''
pip install you-get
'''

def download(url):
    os.system("you-get --playlist %s" % (url))
    

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1mi4y1T7KY?from=search&seid=16625093456813847926"
    download(url)
