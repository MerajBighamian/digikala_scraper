from .serializer import UrlSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Urls, Products
from .scraper import get_products
import json
from rest_framework.exceptions import ValidationError

def get_json_of_products(url_id):
    """
    this function get products from database and 
    """
    product_json = []
    # queryset for get product of url with url_id
    products_in_db = Products.objects.filter(url_id=url_id)
    for product_in_db in products_in_db:
        # build product list from Product object
        product = [product_in_db.pk, product_in_db.title_en, product_in_db.title_fa, product_in_db.status, product_in_db.brand, product_in_db.image_url, product_in_db.rating,
                   product_in_db.count_of_rating, product_in_db.seller, product_in_db.color, product_in_db.price, product_in_db.warranty, product_in_db.rating]
        # add product lists to product_json list for convert to json
        product_json.append(product)
    product_json = {"data": product_json}
    # convert product_json list to json
    json_string = json.dumps(product_json, ensure_ascii=False).encode("utf-8")
    # decode json_stirng for show persian character
    json_string = json_string.decode()
    return json_string