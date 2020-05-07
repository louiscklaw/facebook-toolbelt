#!/usr/bin/env python3

import os, sys

PROJ_HOME = os.path.dirname(__file__)
# from facebook_scraper import get_posts
sys.path.append(f"{PROJ_HOME}/_lib")

# import _lib.facebook_scraper_new
from _lib.facebook_scraper_new import get_posts


import datetime
import json

from multiprocessing import Pool

from time import sleep
import random



def process_datetime(post_in):
    post_in['time'] = datetime.datetime.strftime(post_in['time'], '%s')

def scrape_posts(fb_page):
    test = []
    i=0
    try:
        for post in get_posts(fb_page, pages=2, sleep=1):

            # sleep(random.randrange(1,10,1))

            i+=1
            print('scrape_post:%s:%d' %(fb_page, i))
            process_datetime(post)
            test.append(post)

        with open('./scraped/%s.json' % fb_page, 'w') as fo:
            json.dump( test, fo, ensure_ascii=False)

    except Exception as e:
        print('scrape page error')
        # raise e

    return test

if __name__ == '__main__':

    with open('./page_list.json','r') as fi:
        scrape_list = json.load(fi)

    p = Pool(30)
    p.map(scrape_posts, scrape_list)
    p.close()
    p.join()
