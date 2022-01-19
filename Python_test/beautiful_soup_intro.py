import os
from bs4 import BeautifulSoup

# os.system('clear||cls')

with open("/Users/vladimir/Desktop/Python_test/html_css_intro.html",'r') as html_string:
	parsed_html = BeautifulSoup(html_string.read(), 'html.parser')

# data = parsed_html.body.contents[1].next_sibling
# data=parsed_html.find(id="css-li").parent
# data = parsed_html.body.contents[1].find_next_sibling()
data = parsed_html.body.findChildren()
print(data)



# print(parsed_html.body.ol.li)
# print(parsed_html.find_all('li'))
# print(parsed_html.find(id="css-li"))
# print('\n',parsed_html.find_all(class_="green")[1])


# print(parsed_html.find(id="css-li"))
# print(parsed_html.select('#css-li'))


# print(parsed_html.select(".green")[1].get_text())

# for var in parsed_html.select("li"):
# 	print(f'{var.attrs}')
# 	print(f'\n {var.get_text()}, {var.name}')