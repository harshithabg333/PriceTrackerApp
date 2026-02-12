import requests
from bs4 import BeautifulSoup
# URL = "https://www.flipkart.com/samsung-galaxy-f36-5g-black-128-gb/p/itmd18f56e2be5da?pid=MOBHDFVTWJGWETBG&lid=LSTMOBHDFVTWJGWETBGLLJCUJ&marketplace=FLIPKART&q=mobiles+samsung&store=tyy%2F4io&srno=s_1_14&otracker=search&otracker1=search&fm=Search&iid=0a99cb8e-9890-40bc-864e-92c724c045e6.MOBHDFVTWJGWETBG.SEARCH&ppt=sp&ppn=sp&ssid=7pykclraw00000001770635382989&qH=4be745d2531e4b61"
# URL = "https://www.flipkart.com/vivo-t4x-5g-marine-blue-128-gb/p/itm017656bdd097b?pid=MOBH9JUSTWEMVADU&param=3838&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTE0LDk5OSoiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJWaXZvIFQ0eCA1RyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkg5SlVTVFdFTVZBRFUiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19"
# URL = "https://www.flipkart.com/samsung-galaxy-m16-5g-blush-pink-128-gb/p/itmf46b23a1eccd9?pid=MOBH9UYUUHJNEYSG&lid=LSTMOBH9UYUUHJNEYSGIK6EGY&marketplace=FLIPKART&q=mobiles+samsung&store=tyy%2F4io&srno=s_1_18&otracker=search&otracker1=search&fm=Search&iid=0a99cb8e-9890-40bc-864e-92c724c045e6.MOBH9UYUUHJNEYSG.SEARCH&ppt=sp&ppn=sp&ssid=7pykclraw00000001770635382989&qH=4be745d2531e4b61"
products_to_track = [   
    {
		"product_url":"https://www.amazon.in/Samsung-Storage-Enhanced-Unmatched-Nightography/dp/B0FDB9H277/ref=pd_day0_d_sccl_2_7/262-1259654-6378831?pd_rd_w=Z6KfC&content-id=amzn1.sym.ccf6529f-31bd-4606-ad8e-481144df5d59&pf_rd_p=ccf6529f-31bd-4606-ad8e-481144df5d59&pf_rd_r=4VJ1WDCFH00SR2FNTWYE&pd_rd_wg=LRMbe&pd_rd_r=73d6432e-6696-4760-9e9f-dd5ab64936c7&pd_rd_i=B0FDB9H277&th=1",
		"name": "Samsung Galaxy M36 5G",
        "target_price":17000
        
	},
	{
		"product_url":"https://www.amazon.in/Samsung-Sapphire-Storage-Upgrades-Lag-Free/dp/B0FN7WCV5Y/ref=sr_1_3?crid=1P74POSQK2IMB&dib=eyJ2IjoiMSJ9.XLRA96PYh8hoMWPl38hRNsgiHDm43ZTzaTJFt9HWuqwFE3xSSrO3p9WfBH-9Ec76m8nEPg4TjziNF4_z7ecWrGQ48dqDCYfC0TcFx8Gl_bxr68nbUm-1yUsLD-3XXi3ytUVU4vA0FyoSyA1m0DOT9KwrbziQ8R8kTat9RRgXiDWWi26NeqMvuF_j9ErT7kCkxl3lG20zbRTHtNK4mMrH2yqoENMNelJ1i9JFjqVkUdQ.-KrKt7o7x6MxK4t1kXA8oo3b9fAOS_7rzJFKHvX6ekw&dib_tag=se&keywords=samsung+mobile&qid=1770828538&sprefix=samasung+mobil%2Caps%2C366&sr=8-3",
		"name": "Samsung Galaxy M17",
        "target_price":14000
	},
	{
		"product_url": "https://www.amazon.in/Samsung-Slimmest-Enhanced-Nightography-Processor/dp/B0F43WXC8K/ref=sr_1_5?crid=1P74POSQK2IMB&dib=eyJ2IjoiMSJ9.XLRA96PYh8hoMWPl38hRNsgiHDm43ZTzaTJFt9HWuqwFE3xSSrO3p9WfBH-9Ec76m8nEPg4TjziNF4_z7ecWrGQ48dqDCYfC0TcFx8Gl_bxr68nbUm-1yUsLD-3XXi3ytUVU4vA0FyoSyA1m0DOT9KwrbziQ8R8kTat9RRgXiDWWi26NeqMvuF_j9ErT7kCkxl3lG20zbRTHtNK4mMrH2yqoENMNelJ1i9JFjqVkUdQ.-KrKt7o7x6MxK4t1kXA8oo3b9fAOS_7rzJFKHvX6ekw&dib_tag=se&keywords=samsung+mobile&qid=1770828538&sprefix=samasung+mobil%2Caps%2C366&sr=8-5",
		"name": "Samsung Galaxy M56",
        "target_price":20000
	},
    {
		"product_url": "https://www.amazon.in/samsung-Galaxy-Awesome-Storage-Without/dp/B0CXMD9YX5/ref=sr_1_10?crid=1P74POSQK2IMB&dib=eyJ2IjoiMSJ9.XLRA96PYh8hoMWPl38hRNsgiHDm43ZTzaTJFt9HWuqwFE3xSSrO3p9WfBH-9Ec76m8nEPg4TjziNF4_z7ecWrGQ48dqDCYfC0TcFx8Gl_bxr68nbUm-1yUsLD-3XXi3ytUVU4vA0FyoSyA1m0DOT9KwrbziQ8R8kTat9RRgXiDWWi26NeqMvuF_j9ErT7kCkxl3lG20zbRTHtNK4mMrH2yqoENMNelJ1i9JFjqVkUdQ.-KrKt7o7x6MxK4t1kXA8oo3b9fAOS_7rzJFKHvX6ekw&dib_tag=se&keywords=samsung+mobile&qid=1770828538&sprefix=samasung+mobil%2Caps%2C366&sr=8-10",
		"name": "Samsung Galaxy A35 5G",
        "target_price":19000
	},
    {
        "product_url": "https://www.amazon.in/iQOO-Aquamarine-Quad-Curved-Dimensity-Processor/dp/B0FHB4F4TN/ref=lp_1389432031_1_12?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=K3R793B607YH8X7F8CTB&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D",
		"name": "iQOO Z10R 5G",
        "target_price":30000
        
    }
 ]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #price_element = soup.select_one("div.v1zwn21j v1zwn20 _1psv1zeb9 _1psv1ze0") Flipkart
    #price_element = soup.select_one(".sc-dOfePm.haKcEH") Meesho
    price_element = soup.select_one("span.a-price-whole") #Amazon product

    if price_element:
        product_price = price_element.get_text(strip=True)
        #print(product_price)
    else:
        print("Price not found. Possible bot blocking.")
        #print(price_element)
    return price_element.get_text()
result_File = open('my_result_file.txt','w')
    
try:    
    for every_product in products_to_track :
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))
      
    
        my_product_price= product_price_returned[0:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))
        print(my_product_price)
        if my_product_price < every_product.get("target_price") :
            print("Available at your best price")
            #result_File.write(every_product.get("name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')
            #result_File.write(f"{product.get('name')} -\tAvailable at Target Price, Current Price - {my_product_price}\n")
            result_File.write(f"{every_product.get('name')} -\tAvailable at Target Price, Current Price - {my_product_price}\n")
            
        else :
            print("still at the current price") 
except Exception as e:
    print("ERROR OCCURRED:", e)              
          
finally :
    
    result_File.close()        
    