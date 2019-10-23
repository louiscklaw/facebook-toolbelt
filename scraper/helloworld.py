#!/usr/bin/env python3

from facebook_scraper import get_posts
import datetime
import json

def process_datetime(post_in):
    post_in['time'] = datetime.datetime.strftime(post_in['time'], '%s')

def scrape_posts(fb_page):
    test = []
    i=0
    try:
        for post in get_posts(fb_page, pages=999):
            i+=1
            print(i)
            process_datetime(post)
            test.append(post)

    except Exception as e:
        print('scrape page error')
        # raise e

    return test

with open('./page_list.json','r') as fi:
    scrape_list = json.load(fi)

for facebook_page in scrape_list:
    i = 0
    with open('./scraped/%s.json' % facebook_page, 'w') as fo:
        i+=1
        print(facebook_page+':%d' % i)
        result  = scrape_posts(facebook_page)
        json.dump( result, fo, ensure_ascii=False)