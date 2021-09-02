from django.contrib import admin
from .models import Seller,Customer,Update,Delete,Access,Search,Purchase,Sbp
# Register your models here.
@admin.register(Seller)
class SellerModelAdmin(admin.ModelAdmin):
 list_display=['id','book_name','description','selling_price','discounted_price']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display=['id','name','phone','email','password','address']

 @admin.register(Update)
 class UpdateModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'book_name']

 @admin.register(Delete)
 class DeleteModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'book_name']

 @admin.register(Access)
 class AccessModelAdmin(admin.ModelAdmin):
  list_display = ['id','name']


 @admin.register(Search)
 class SearchModelAdmin(admin.ModelAdmin):
  list_display = ['id','book_name']

 @admin.register(Purchase)
 class PurchaseModelAdmin(admin.ModelAdmin):
  list_display = ['id','book_name']

 @admin.register(Sbp)
 class SbpModelAdmin(admin.ModelAdmin):
  list_display = ['id','book_name']





