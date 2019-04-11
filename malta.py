import requests
from bs4 import BeautifulSoup
import csv

file = open('Art-galleries-in-Malta.csv', 'w')
f = csv.writer(file)
f.writerow(['Name', 'Phone_no', 'Website', 'Address', 'State/Province'])
country = 'Malta'
states = ['Southern Harbour District', 'Northern Harbour District', 'South Eastern District', 'Western District', 'Northern District', 'Gozo and Comino District']
key = ##get your api key at https://developers.google.com/places/android-sdk/signup
for state in states:
        pg_tok=""
        while pg_tok != " ":
                url = "https://maps.googleapis.com/maps/api/place/textsearch/xml?query=art+galleries+in"+country+state+"&key="+key+"&pagetoken="+pg_tok
                page = requests.get(url)
                soup = BeautifulSoup(page.content,"html.parser")
                list = soup.find_all('result')

                for item in list:
                        item1 = item.find('name').contents[0].encode("utf-8")
                        print(item1.decode())
                        url1 = "https://maps.googleapis.com/maps/api/place/details/xml?query=art+galleries+in"+country+state+"&key=AIzaSyDoSmAyncbnbf-XAEQYLXz4pT9xpXQpu0I&place_id="+item.find('place_id').text
                        page1 = requests.get(url1)
                        soup1 = BeautifulSoup(page1.content,"html.parser")
                        item2 = soup1.find('international_phone_number')
                        item3 = soup1.find('website')
                        item4 = soup1.find('formatted_address')
        
                        if item2 is None:
                            item2_="".encode("utf-8")
                        else:
                            item2_=item2.contents[0].encode("utf-8")
                        if item3 is None:
                            item3_="".encode("utf-8")
                        else:
                            item3_=item3.contents[0].encode("utf-8")
                        if item4 is None:
                            item4_="".encode("utf-8")
                        else:
                            item4_=item4.contents[0].encode("utf-8")
                        f.writerow([item1,item2_,item3_,item4_,state.encode("utf-8")])
                if soup.find('next_page_token') is None:
                        pg_tok=" "
                else:
                        pg_tok = soup.find('next_page_token').contents[0]
file.flush()
file.close()
