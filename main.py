import threading
from queue import Queue
from crawl_object import Crawler
from crawler_demo import data_to_set
from domain_extract import get_domain_nm

PROJECT_NM = 'page'
HOMEPAGE = 'https://www.reddit.com/'
DOMAIN_NAME = get_domain_nm(HOMEPAGE)
QUEUE_FILE = PROJECT_NM + '/files_to_crawl.txt'
CRAWLED = PROJECT_NM + '/crawled.txt'
NUM_THREADS = 5
queue = Queue
Crawler(PROJECT_NM, HOMEPAGE, DOMAIN_NAME)


def crawl():
    queue_urls = data_to_set(QUEUE_FILE)
    if len(queue_urls) > 0:
        start_process()


def start_process():
    for url in data_to_set(QUEUE_FILE):
        queue.put(url)
        queue.join()
        crawl()


def create_thread():
    for _ in range(NUM_THREADS):
        thread_obj = threading.Thread(target=do_crawl())
        thread_obj.daemon = True
        thread_obj.start()


def do_crawl():
    while(True):
        url = queue.get()
        Crawler.crawl_one(threading.current_thread().name, url)
        queue.task_done()


create_thread()
crawl()