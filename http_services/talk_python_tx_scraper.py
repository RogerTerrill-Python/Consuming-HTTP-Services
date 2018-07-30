from requests_html import HTMLSession
from xml.etree import ElementTree
session = HTMLSession()


def main():
    tx_urls = get_transcripts_urls()
    print(tx_urls)


def get_transcripts_urls():
    sitemap_url = 'https://talkpython.fm/sitemap.xml'
    response = session.get(sitemap_url)
    if response.status_code != 200:
        print(f"Cannot get sitemap, {response.status_code} {response.text}")
        return []

    xml_text = response.text.replace('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', '')
    dom = ElementTree.fromstring(xml_text)

    tx_urls = [
        n.text
        for n in dom.findall('url/loc')
        if n.text.find('/episodes/transcript') > 0
    ]

    return tx_urls


if __name__ == '__main__':
    main()