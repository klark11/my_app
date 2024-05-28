from django.contrib import admin

# Register your models here.


from products import models


admin.site.register(models.Product)
admin.site.register(models.ProductAttribute)
admin.site.register(models.Game)
admin.site.register(models.Service)
admin.site.register(models.ProductAttributeValue)