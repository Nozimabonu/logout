from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from blog.managers import CustomUserManager
from blog.validators import validate_length


# Create your models here.

class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.Zero.value)
    amount = models.IntegerField(default=1)
    discount = models.IntegerField()
    slug = models.SlugField(max_length=255, null=True, default=None, blank=True)

    # attribute =models.ManyToManyField('Attribute', blank=True,  related_name='attribute')

    def get_attributes(self) -> list:
        product_attributes = ProductAttribute.objects.filter(product=self)
        attributes = []
        for pa in product_attributes:
            attributes.append({
                'attribute_name': pa.attribute.attribute_name,
                'attribute_value': pa.attribute_value.attribute_value
            })
        return attributes

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + slugify(self.price)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('blog.Product', on_delete=models.CASCADE, related_name='images')


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_value


class ProductAttribute(models.Model):
    product = models.ForeignKey('blog.Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('blog.Attribute', on_delete=models.CASCADE)
    attribute_value = models.ForeignKey('blog.AttributeValue', on_delete=models.CASCADE)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=13, validators=[validate_length], unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    billing_address = models.TextField()
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
