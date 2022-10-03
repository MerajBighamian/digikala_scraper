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

def add_products_in_db(url_model, url):
    """
    this function add products (of digikala) to database
    """
    # get products from digikala (json type)
    products = get_products(url)

    for product in products:
        url_model = url_model
        title_fa = product["title_fa"]
        title_en = product["title_en"]
        status = product["status"]
        brand = product["data_layer"]["brand"]
        image_url = product["images"]["main"]["url"][0]
        rating = product["rating"]["rate"]
        count_of_rating = int(product["rating"]["count"])
        color = product["default_variant"]["color"]["title"]
        warranty = product["default_variant"]["warranty"]["title_fa"]
        seller = product["default_variant"]["seller"]["title"]
        price = int(product["default_variant"]["price"]["selling_price"])
        Products.objects.create(url_id=url_model, title_fa=title_fa, title_en=title_en, status=status,          brand=brand,
                                image_url=image_url, rating=rating, color=color, warranty=warranty, seller=seller, count_of_rating=count_of_rating, price=price)

class GetUrlAndListData(APIView):
    """
    APIView class for get url from user and rerutn data of products
    """
    serializer_class = UrlSerializer
    # validate function for validate url
    def validate(self):
        url = self.request.data["url"]
        # raise error if url is empry
        if url == "":
            raise ValidationError({"error": "url is not empty"})
        # raise error if url is not for digikala url pattern
        if not (url.startswith("https://www.digikala.com/search/category-mobile-phone/product-list/?page=")):
            raise ValidationError({"error": "url is not for digikala category"})
            
    def post(self, request):
        url = request.data["url"]   
        self.validate() # validate data(url)
        url_model = Urls(url=url)
        url_model.save()
        add_products_in_db(url_model, url)
        json_data = get_json_of_products(url_model)
        return Response(json_data.encode('utf-8'))
