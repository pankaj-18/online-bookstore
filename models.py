from django.db import models

# Create your models here.
class Seller(models.Model):
    book_name=models.CharField(max_length=100)
    description=models.TextField()
    selling_price=models.IntegerField()
    discounted_price=models.IntegerField()

    def __str__(self):
        return self.book_name


class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Delete(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Update(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Access(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Search(models.Model):
    book_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sbp(models.Model):
    book_name=models.CharField(max_length=100)


    def __str__(self):
        return self.book_name