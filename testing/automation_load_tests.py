import time
import requests
import random
import threading

list_of_domain = ["https://www.google.com/", 'https://www.at-bay.com/', 'https://www.netflix.com/',
                  "http://banaba.com/", "https://il.godaddy.com/", "https://www.ferrari.com/en-IL",
                  "https://github.com/", "https://stackoverflow.com/", "apple.com", "wordpress.org", "amazon.com",
                  "ebay.com", "spotify.com", "random_domain.co.il", "mybesturlever.com", "url.url.url.com",
                  "where_is_my_url.com", "blalalala.com", "adklasndjn.com", "adkjfgbasojfdbajfbasbd.com",
                  "akjdsdbaskjd.com", "wiki.com", "il.gov.co.il", "balagan.com"]

list_of_scans = []


def ingest_function():
    for i in range(1000):
        domain = list_of_domain[random.randint(0, len(list_of_domain) - 1)]
        res = requests.post("http://127.0.0.1:5000/ingest/", data={"domain": domain}).json()
        list_of_scans.append(res['scan_id'])
        print(f"scan id: {res['scan_id']} -> domain: {domain}")
        time.sleep(1)


def get_status():
    while True:
        if list_of_scans:
            scan_id = list_of_scans[random.randint(0, len(list_of_scans) - 1)]
            res = requests.get(
                f"http://127.0.0.1:5001/status/{scan_id}/").json()
            print(f"scan id: {res['result']['scan_id']} -> status: {res['result']['status']}")
            time.sleep(1)


t1 = threading.Thread(target=ingest_function)
t2 = threading.Thread(target=get_status)

t1.start()
t2.start()
