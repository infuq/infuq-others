#! /usr/bin/env python3.7
# -*- coding:utf-8 -*-


# pip install lxml

from lxml import etree


def parse_text():
    text = '''
    <div></div>
    <div></div>
    '''
    html = etree.HTML(text)
    print(html)


def parse_file():
    html = etree.parse('x.html')
    print(html)


def parse_file_2():
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('x.html', parser=parser)
    print(html)

    trs = html.xpath("//tr")
    for tr in trs:
        print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    parse_text()
