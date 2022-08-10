from urllib.parse import urlparse
from collections import Counter


def validate_webpage(r):
    if 'text/html' in r.headers['content-type']:
        return True
    return False


def webpage_type(p):
    if "<!doctype html>" in p[0:30].lower():
        return "HTML 5"
    else:
        return "HTML 4"


def get_domain(url):
    d = ""
    url_parse = urlparse(url).netloc
    url_arr = Counter(url_parse)
    if url_arr['.'] > 1:
        d_pos = url_parse.find('.')
        d = url_parse[d_pos + 1:]
    else:
        d = url_parse
    return d


def scrap_links(url, links):
    i_links = []
    e_links = []
    d = get_domain(url)
    for a in links:
        href = a.get('href')
        if href:
            if d in href:
                i_links.append(href)
            elif href[0] == "#":
                i_links.append(url + "/#")
            elif href[0] == "/":
                i_links.append(url + href)
            else:
                if "http" in href:
                    e_links.append(href)
    return i_links, e_links


def scrap_resource(resources):
    src = []
    for r in resources:
        src.append(r.get('src'))
    return src


def scrap_av_media(soup, m_resources):
    a_src = []
    v_src = []
    if m_resources[0].name == "audio":
        for m in m_resources:
            mp3 = soup.find('source', type='audio/mpeg')
            if mp3:
                a_src.append(soup.find('source', type='audio/mpeg').get('src'))
        return a_src
    else:
        for m in m_resources:
            mp4 = soup.find('source', type='video/mp4')
            if mp4:
                v_src.append(soup.find('source', type='video/mp4').get('src'))
        return v_src


def display_sources(src_arr):
    if len(src_arr) > 0:
        print(*src_arr, sep="\n")
    else:
        print("Sorry, no sources for this tag")
