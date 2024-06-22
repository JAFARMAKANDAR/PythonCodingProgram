import re

# str="In blogger at http://www.pavantestingtools.com/"
#str=" My Profile: https://pavanonlinetrainingses.com/about.html"
str=" My Profile: https://pavanonlinetrainingses.com/about.html and MyBlog: http://www.pavantestingtools.com/"

#http://urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)

print(url)