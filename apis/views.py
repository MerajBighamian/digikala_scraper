from .serializer import UrlSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Urls, Products
from .scraper import get_products
import json
from rest_framework.exceptions import ValidationError
