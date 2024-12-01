# -*- coding: utf-8 -*-

import requests

# 获取Python镜像源数据
def pypi():
    # 清华大学
    # url = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    # 阿里云
    # url = 'http://mirrors.aliyun.com/pypi/simple/'
    # 中国科技大学
    # url = 'https://mirrors.ustc.edu.cn/pypi/simple/'
    # 腾讯
    url = 'https://mirrors.cloud.tencent.com/pypi/simple/'
    response = requests.get(url)
    
    # print(response.text)
    # print(response.content.decode('utf-8'))
    with open('pypi_tencent.html', 'w', encoding='utf-8') as f:
        f.write(response.content.decode('utf-8'))
    


if __name__ == '__main__':
    pypi()