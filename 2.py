
import requests
from bs4 import BeautifulSoup as bs
 
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
URL = 'https://www.geeksforgeeks.org/page/'
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = bs(r.content, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)

# s = soup.find('div', class_='entry-content')
# content = s.find_all('p')
 
# print(content)

# z = soup.find('div', id= 'main')
 
# # Getting the leftbar
# leftbar = z.find('ul', class_='leftBarList')
 
# # All the li under the above ul
# contentz = leftbar.find_all('li')
 
# for line in contentz:
#     print(line.text)

# s = soup.find('div', class_='entry-content')
 
# lines = s.find_all('p')
 
# for line in lines:
#     print(line.text)

# for link in soup.find_all('a'):
#     print(link.get('href'))
    
# images_list = []
 
# images = soup.select('img')
# for image in images:
#     src = image.get('src')
#     alt = image.get('alt')
#     images_list.append({"src": src, "alt": alt})
     
# for image in images_list:
#     print(image)
    
# titles = soup.find_all('div',attrs = {'class','head'})
 
# print(titles[4].text)

# for page in range(1, 10):
     
#     req = requests.get(URL + str(page) + '/')
#     soup = bs(req.text, 'html.parser')
 
#     titles = soup.find_all('div', attrs={'class', 'head'})
 
#     for i in range(4, 19):
#         if page > 1:
#             print(f"{(i-3)+page*15}" + titles[i].text)
#         else:
#             print(f"{i-3}" + titles[i].text)