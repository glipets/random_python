import bs4, requests



def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#listPrice')
    return elems[0].text.strip()


price = getAmazonPrice('https://shop.shadowpeak.com/product.sc?productId=10&categoryId=1')    
print ('The price is ' + price)
