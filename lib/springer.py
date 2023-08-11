"""
springer.py
some function for springer
20201106
"""

import urllib
from urllib.request import urlopen, Request
import time
import bs4
from bs4 import BeautifulSoup
from tqdm import tqdm
from slugify import slugify

def get_paper_name_link_from_url(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    paper_dict = {}
    req = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(req, timeout=10).read()
    soup = BeautifulSoup(content, 'html5lib')
    paper_list_bar = tqdm(soup.find_all(['li'], {'class': 'chapter-item content-type-list__item'}))
    for paper in paper_list_bar:
        try:
            title = slugify(paper.find('div', {'class': 'content-type-list__title'}).text)
            link = urllib.parse.urljoin(url, paper.find('div', {'class': 'content-type-list__action'}).a.get('href'))
            paper_dict[title] = link
        except Exception as e:
            print(f'ERROR: {str(e)}')
    return paper_dict


if __name__ == '__main__':
    papers = get_paper_name_link_from_url('https://link.springer.com/book/10.1007%2F978-3-319-46448-0')