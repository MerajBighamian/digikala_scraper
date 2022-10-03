import requests
import re
import json
from rest_framework.exceptions import ValidationError

def get_products(url):
    """
    this function get a url and scrap data from it
    the url should be this pattern : https://www.digikala.com/search/category-mobile-phone/product-list/?page=number_of page 
    
    """
    try:
        page_number = re.findall(r'\d+', url)[-1] # get page number from url
    
        data = requests.get(f"https://api.digikala.com/v1/categories/mobile-phone/search/?page={page_number}")
        #get data from url 
        json_data = json.loads(data.text) # convert json data to python dictionary
        products = json_data["data"]["products"] # get products of url (digikala page)
        return products
    except IndexError:
        raise ValidationError({"error":"url have not page number!"})
    except:
        raise ValidationError({"error":"connection is lost or url is bad url"})
        

