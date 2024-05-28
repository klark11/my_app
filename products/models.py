from django.db import models
import uuid
from products.base.fields import ProductMoneyField
from django.core.validators import MinValueValidator
# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'game'


class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'service'


class ProductAttribute(models.Model):
    class TypeChoices(models.TextChoices):
        BOOL = 'BOOL', 'Bool'
        Text = 'TEXT', 'Text'
        CHECKBOX = 'CHECKBOX', 'Checkbox'

    type = models.CharField(choices=TypeChoices, default=TypeChoices.Text, max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'product type {self.name} with type {self.type}'

    class Meta:
        db_table = 'productAttribute'
        constraints = [
            models.UniqueConstraint(fields=['type','name'],
                name='unique_type_name'
            )
        ]


class Product(models.Model):
    class StatusProductChoices(models.TextChoices):
        MODERATION = 'MODERATION', 'Moderation'
        PUBLISH = 'PUBLISH', 'Publish'
        CLOSE = 'CLOSE', 'Close'

    service_id=models.ForeignKey(Service, related_name='service_products',on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # seller_id = models.ForeignKey(User, related_name='user_products')
    price = ProductMoneyField(validators=[MinValueValidator(1, 'value must be greater than 1')])
    count = models.SmallIntegerField(default=1)
    status = models.CharField(choices=StatusProductChoices.choices, max_length=20, default=StatusProductChoices.MODERATION)


    def __str__(self):
        return f'product {self.id}'

    class Meta:
        db_table = 'product'

class ProductAttributeValue(models.Model):
    product_id = models.ForeignKey(Product, related_name='fields_values', on_delete=models.CASCADE)
    field_id = models.ForeignKey(ProductAttribute, related_name='service_fields_values',on_delete=models.CASCADE)
    value = models.TextField(blank=True)

    def __str__(self):
        return f'value - {self.value}'