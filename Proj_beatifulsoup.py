import requests, csv
from bs4 import BeautifulSoup

# Download table content from website and write into a CSV file
url="https://www.w3schools.com/html/html_tables.asp"
'''
response=requests.get(url=url).content
web_content=BeautifulSoup(response,"lxml")
table_head = web_content.find("table", {"id":"customers"}).find_all("th")
thead = [th.text for th in table_head]

with open("Sample.csv","w",newline="") as file:
    csv_write=csv.writer(file)
    csv_write.writerow(thead)
    table_rows = web_content.find("table", {"id":"customers"}).find_all("tr")
    for tr in table_rows:
        tdata = [td.text for td in tr.find_all("td")]
        if tdata:
            csv_write.writerow(tdata)
        
'''

# =============================================================================================================
# Download the specific image from web site and create image file in local

url="https://www.moviecrow.com/movie/5075/madharasi/gallery"

response2 = requests.get(url=url).content
web_content2 = BeautifulSoup(response2,"lxml")
images = web_content2.find_all("img", {"alt":"Madharasi Picture Gallery"})

for img in images:
    img_url = img.get("src")
    img_name = img.get("src").split("/")[-1]
    print(img_url)
    img_content = requests.get(url=img_url).content

    with open(img_name, "wb") as file:
        file.write(img_content)



