import sys
from magnet_links import get_magnet_link

if __name__ == '__main__':
  print("Python version")
  print (sys.version)
  print(get_magnet_link("rick morty s06e04 1080p")["magnet_link"])

  