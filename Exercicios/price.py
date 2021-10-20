import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty.html")
text = page.read().decode("utf8")
price = text(234:238)
print(price)
