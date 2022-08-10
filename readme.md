# Web Page Analyzer (Daisi Hackathon)

Python function as a web service to scrape and analyze web page data according to most common **HTML** tags.

It will return the following information:

Web page title, Type of the web page, Domain of requested web page, number of heading `<h1>..<h6>` tags, number of paragraph `<p>` tags, number of ordered & unordered list `<ol><ul>` tags, number of image `<img>` tags, number of internal links of the requested web page, number of external links of the webpage, number of table `<table>` tags, number of form `<form>` tags, number of input `<input>` tags, number of button `<button>` tags, number of code snippet `<code>` tags, number of dropdown list `<select>` tags, number of audio `<audio>` tags, number of video `<video>` tags, number of Javascript client script `<script>` tags.

How to call it from Python:

Step 1 : Load the Daisi

<pre>
import pydaisi as pyd
web_page_analyzer = pyd.Daisi("oghli/Web Page Analyzer")
</pre>
Step 2 : call the `web_page_analyzer` end point, passing web page url to analyze its HTML content

<pre>
url = "https://www.stackoverflow.com"
webpage_analytics = web_page_analyzer.analyze_webpage(url).value
webpage_analytics
</pre>

returns a dictionary containing information about the requested web page.

Step 3 : print web page analysis summary 
<pre>
webpage_analytics['s']
</pre>

Output:
<pre>
____________Summary______________
Webpage Title: Stack Overflow - Where Developers Learn, Share, & Build Careers
Type: HTML 5
Domain: stackoverflow.com
Total Heading: 42
Total Paragraph: 170
Total List: 49
Total Image: 57
Total Internal link: 400
Total External link: 98
Total Table: 0
Total Form: 1
Total Input: 2
Total Button: 97
Total Code snippet: 180
Total Drop down list: 1
Total Audio: 0
Total Video: 0
Total JS Script: 14
</pre>

Define helper function to display content of any tag sources:
<pre>
def display_src(src_arr):
    if len(src_arr) > 0:
        print(*src_arr, sep="\n")
    else:
        print("Sorry, no sources for this tag")
</pre>


Display internal links of the requested wep page:
<pre>
display_src(webpage_analytics['in_links'])
</pre>

It will output links in this format:
<pre>
https://www.stackoverflow.com/#
https://www.stackoverflow.com/teams
https://www.stackoverflow.com/questions
https://www.stackoverflow.com/teams
https://stackoverflow.com
</pre>

Display external links of the requested wep page:
<pre>
display_src(webpage_analytics['ex_links'])
</pre>

Output:
<pre>
https://www.facebook.com/officialstackoverflow/
https://twitter.com/stackoverflow
https://linkedin.com/company/stack-overflow
https://www.instagram.com/thestackoverflow
</pre>
Display images sources of the requested wep page:
<pre>
display_src(webpage_analytics['images'])
</pre>
Output:
<pre>
https://cdn.sstatic.net/Img/teams/teams-illo-free-sidebar-promo.svg?v=47faa659a05e
https://cdn.sstatic.net/Img/home/illo-code.svg?v=b7ee00fff9d8
https://cdn.sstatic.net/Img/home/illo-code.svg?v=b7ee00fff9d8
https://cdn.sstatic.net/Img/home/illo-public.svg?v=14bd5a506009
https://cdn.sstatic.net/Img/home/illo-teams.svg?v=7e543f14fcc0
</pre>
Display audio sources:
<pre>
display_src(webpage_analytics['audios'])
</pre>
Display video sources:
<pre>
display_src(webpage_analytics['videos'])
</pre>
Display scripts sources:
<pre>
display_src(webpage_analytics['scripts'])
</pre>
