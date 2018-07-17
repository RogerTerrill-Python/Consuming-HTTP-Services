import requests
from xml.etree import ElementTree
import collections
from dateutil.parser import parse
# 3:46

Episode = collections.namedtuple('Episode', 'title link pubdate')

def main():
    dom = get_xml_dom('https://talkpython.fm/rss')
    episodes = get_episodes(dom)


def get_episodes(dom):
    item_nodes = dom.findall('channel/item')
    print(len(item_nodes))


def get_xml_dom(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        return None

    dom = ElementTree.fromstring(resp.text)
    return dom


if __name__ == '__main__':
    main()
