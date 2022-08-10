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
url = "https://drive.stackoverflow.com"
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

