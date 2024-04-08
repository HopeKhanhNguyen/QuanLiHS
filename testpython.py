import requests
from bs4 import BeautifulSoup

class checkrepo() :
    def __init__(self) -> None:
        self._session = requests.Session()
    def run(self) :
        rps = self._session.get("").text
        pg = BeautifulSoup(rps , "html.parser")