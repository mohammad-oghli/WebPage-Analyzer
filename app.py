from bs4 import BeautifulSoup
import requests
from helper import webpage_type, validate_webpage, get_domain, scrap_links\
    , scrap_resource, scrap_av_media, print_sources


def analyze_webpage(wp_url):
    '''
    Scrape and analyze web page data according to most common HTML tags

    :param
    wp_url(str): Valid url of the web page

    :return
    web_page(dict): Dictionary containing analytics information of the requested web page,

    if web page url is invalid it will return message indicating url error
    '''
    web_page = {}
    in_links = []
    ex_links = []
    images_sc = []
    scripts_sc = []
    audio_src = []
    video_src = []
    try:
        response = requests.get(wp_url)
        if not validate_webpage(response):
            msg = "Sorry, the requested url isn't a web page."
            return msg
        data = response.text
        domain = get_domain(wp_url)
        w_type = webpage_type(data)
        soup = BeautifulSoup(data, "html.parser")  # create a soup object using the variable 'data'

        title = soup.find('title').string.strip()
        headings = soup.findAll(name=['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        paragraphs = soup.findAll('p')
        lists = soup.findAll(name=['ul', 'ol'])
        images = soup.findAll('img')
        img_src = soup.findAll('img', src=True)
        links = soup.findAll('a', href=True)
        audios = soup.findAll('audio')
        videos = soup.findAll('video')
        tables = soup.findAll('table')
        forms = soup.findAll('form')
        inputs = soup.findAll('input')
        buttons = soup.findAll('button')
        codes = soup.findAll('code')
        drop_lists = soup.findAll('select')
        scripts = soup.findAll('script')
        script_src = soup.findAll('script', src=True)

        if len(links) > 0:
            in_links, ex_links = scrap_links(wp_url, links)
        if len(img_src) > 0:
            images_sc = scrap_resource(img_src)
        if len(audios) > 0:
            audio_src = scrap_av_media(soup, audios)
        if len(videos) > 0:
            video_src = scrap_av_media(soup, videos)
        if len(script_src) > 0:
            scripts_sc = scrap_resource(script_src)

    except requests.exceptions.ConnectionError:
        msg = "Sorry, the requested web page url is invalid."
        return msg
    except requests.exceptions.MissingSchema:
        msg = "Incorrect requested url format!"
        return msg

    summary = f"""____________Summary______________
Webpage Title: {title}
Type: {w_type}
Domain: {domain}
Total Heading: {len(headings)}
Total Paragraph: {len(paragraphs)}
Total List: {len(lists)}
Total Image: {len(images)}
Total Internal link: {len(in_links)}
Total External link: {len(ex_links)}
Total Table: {len(tables)}
Total Form: {len(forms)}
Total Input: {len(inputs)}
Total Button: {len(buttons)}
Total Code snippet: {len(codes)}
Total Drop down list: {len(drop_lists)}
Total Audio: {len(audios)}
Total Video: {len(videos)}
Total JS Script: {len(scripts)}
    """
    web_page['s'] = summary
    web_page['h'] = len(headings)
    web_page['p'] = len(paragraphs)
    web_page['img'] = len(images)
    web_page['href'] = len(links)
    web_page['table'] = len(tables)
    web_page['form'] = len(forms)
    web_page['in_links'] = in_links
    web_page['ex_links'] = ex_links
    web_page['images'] = images_sc
    web_page['audios'] = audio_src
    web_page['videos'] = video_src
    web_page['scripts'] = scripts_sc
    return web_page


if __name__ == "__main__":
    url = "https://stackoverflow.com"
    analyze_result = analyze_webpage(url)
    if type(analyze_result) is dict:
        summary = analyze_result['s']
        print(summary)
    else:
        print(analyze_result)


