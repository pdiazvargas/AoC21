import os
import requests
import requests_cache

requests_cache.install_cache("../cache")


def get_input(day):
    url = f"https://adventofcode.com/2021/day/{day}/input"
    return requests.get(url, cookies={"session": os.environ["SESSION"]}).text.strip()
