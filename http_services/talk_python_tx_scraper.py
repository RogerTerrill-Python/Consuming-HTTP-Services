import requests_html
from xml.etree import ElementTree
import collections
session = requests_html.HTMLSession()

Page = collections.namedtuple('Page', 'url title paragraphs')
Paragraph = collections.namedtuple('Paragraph', 'text seconds')


def main():
    tx_urls = get_transcripts_urls()
    pages = download_transcript_pages(tx_urls[:3])
    show_pages(pages)


def download_transcript_pages(tx_urls):
    pages = []

    for url in tx_urls:
        page = build_page_from_url(url)
        pages.append(page)

    return pages


def build_page_from_url(url):
    print(f"Downloading {url}", flush=True)
    response = session.get(url)
    h1_element = response.html.find('h1', first=True)
    title = clean_line(h1_element.text)

    paragraphs = [
        Paragraph(clean_line(p.text), int(p.attrs["seconds"]))
        for p in response.html.find('.transcript-segment')
    ]

    return Page(url, title, paragraphs)


def get_transcripts_urls():
    sitemap_url = 'https://talkpython.fm/sitemap.xml'
    response = session.get(sitemap_url)
    if response.status_code != 200:
        print(f"Cannot get sitemap, {response.status_code} {response.text}")
        return []

    xml_text = response.text.replace('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', '')
    dom = ElementTree.fromstring(xml_text)

    # Pulls any episodes that have a transcript since not all do through xml
    tx_urls = [
        n.text  # Returns the text of the returned loc
        for n in dom.findall('url/loc')  # Traverses the xlm, specifically the url then loc tags
        if n.text.find('/episodes/transcript') > 0  # Pulls only those that contain the string transcripts in them
    ]

    return tx_urls


def clean_line(text):
    text = text.replace('\n', ' ').replace('\t', ' ')
    size = len(text) + 1
    while size > len(text):
        size = len(text)
        text = text.replace('  ', ' ')
    return text.strip()


def show_pages(pages):
    for p in pages:
        print(p.title)
        print(f"* {p.url}")
        print(f"* {len(p.paragraphs):,} paragraphs")
        print(f" 1. {p.paragraphs[0].text}")
        print()


if __name__ == '__main__':
    main()