


```python
1. pip config set global.index-url https://pypi.doubanio.com/simple
2. pip3 install scrapy         if Linux
   pip3 install -U scrapy     更新安装
3. pip3 install pypiwin32      if windows
   pip3 install Twisted
   pip3 install scrapy
4. 
$ scrapy startproject PROJECT_NAME
$ cd PROJECT_NAME
$ scrapy genspider douban movie.douban.com
$ scrapy crawl douban -o douban.csv

pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

































