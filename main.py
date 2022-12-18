import requests
import bs4

url = input("Enter your url ")
response = requests.get(url)

filename= "temp.html"
bs= bs4.BeautifulSoup(response.text,"html.parser")

formatted_text=bs.prettify()
print(formatted_text)

with open(filename,"w+", encoding="utf-8") as f:
	f.write(formatted_text)