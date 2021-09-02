from django.core import validators
from django import forms
from .models import Seller,Customer,Update,Delete,Access,Purchase,Search,Sbp

class Sellerregistration(forms.ModelForm):
    class Meta:
        model=Seller
        fields=['book_name','description','selling_price','discounted_price']

class Customerregistraion(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['id','name','phone','email','password','address']

class Updateregistraion(forms.ModelForm):
    class Meta:
        model=Update
        fields=['book_name']

class Deleteregistraion(forms.ModelForm):
    class Meta:
        model=Delete
        fields=['book_name']

class Accessregistraion(forms.ModelForm):
    class Meta:
        model=Access
        fields=['name']
class Searchregistraion(forms.ModelForm):
    class Meta:
        model=Search
        fields=['book_name']


class Purchaseregistraion(forms.ModelForm):
    class Meta:
        model=Purchase
        fields=['book_name']

class Sbpregistraion(forms.ModelForm):
    class Meta:
        model=Sbp
        fields=['book_name']


