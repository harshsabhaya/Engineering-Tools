from django.contrib import admin
from .models import Register, Company_Profile, Product_Catagory, Product_Hardware

# Register your models here.
admin.site.register(Register)
admin.site.register(Company_Profile)
admin.site.register(Product_Catagory)
admin.site.register(Product_Hardware)