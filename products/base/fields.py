from django.db.models import DecimalField
from django.conf import settings



class ProductMoneyField(DecimalField):
    def __init__(
            self,
            verbose_name=None,
            name=None,
            max_digits=settings.MAX_PRODUCT_PRICE,
            decimal_places=2,
            **kwargs,

    ):
        super().__init__(verbose_name,name,max_digits,decimal_places,**kwargs)