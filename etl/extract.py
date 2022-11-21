from bs4 import BeautifulSoup
import requests

url = 'https://www.fundsexplorer.com.br/ranking'
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"
}
response = requests.get(url, header)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find(id="table-ranking")
