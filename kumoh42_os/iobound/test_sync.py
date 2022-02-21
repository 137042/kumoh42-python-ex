import requests
import time

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


def main():
    with requests.Session() as session:
        for _ in range(100):
            fetch(session, URL)

if __name__ == "__main__":
    start_time = time.time()
    main()
    duration = time.time() - start_time
    print(f"{duration} seconds")