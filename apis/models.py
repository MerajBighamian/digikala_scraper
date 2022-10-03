from django.db import models


class Urls(models.Model):
    """
    table for store Urls from post request
    """
    url = models.URLField(max_length=500)


class Products(models.Model):
    """
    table for store procducts of every url in Urls table
    """
    url_id = models.ForeignKey(Urls, on_delete=models.CASCADE)
    title_fa = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    rating = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    count_of_rating = models.IntegerField()
    warranty = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    price = models.IntegerField()
