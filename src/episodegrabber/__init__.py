import sys
from magnet_links import get_magnet_link
from get_current_country import get_ip, get_country


if __name__ == '__main__':
  input_file = open('input.txt', 'r')
  line = input_file.read()
  base_URL = ''
  if len(line.split(' ')) == 3:
    base_URL = line.split()[-1]
  else:
    print('Wrong base URL given / tokenized')
    exit()
  input_file.close()

  print("Python version")
  print (sys.version)
  print(get_magnet_link("rick morty s06e04 1080p", base_URL=base_URL)["magnet_link"])
  current_country = get_country(get_ip())
  if current_country == 'US':
    exit()
  else:
    print('continue')