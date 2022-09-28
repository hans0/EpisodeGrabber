import requests
from bs4 import BeautifulSoup

base_URL = "https://1337x.to"

def get_magnet_link(search_string):
  URL = base_URL + "/search/"+"+".join(search_string.split())+"/1/"
  user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
  headers = {'User-Agent': user_agent}
  response = requests.get(URL, headers=headers)
  if (int(response.status_code) != 200):
    return response.status_code
  soup = BeautifulSoup(response.content, "html.parser")
  td = soup.find('td')
  td = str(td)
  try:
    start_index = td.index("/torrent")
  except ValueError:
    return ""
  end_index = start_index + td[start_index:].index('"')
  torrent_link_substring = td[start_index:end_index]
  response.close()
  URL = base_URL + torrent_link_substring
  response = requests.get(URL, headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")
  div = soup.findAll("div", {"class": "clearfix"})
  magnet_start_index = int(str(div).index("magnet:?"))
  magnet_end_index = int(str(div).index("\"", magnet_start_index))
  response.close()
  result = {
    "status_code": int(response.status_code),
    "magnet_link": str(div)[magnet_start_index:magnet_end_index]
  }
  return result

#print(get_magnet_link("rick morty s06e04 1080p"))