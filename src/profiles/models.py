from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Freelancer(models.Model):
    """Модель фрилансера(исполнителя заказов)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cost_of_work = models.PositiveIntegerField(verbose_name='The cost of work', blank=False, null=False, default=0)
    experience = models.CharField(
        max_length=50, verbose_name='Work experience', blank=False, null=False, default='No experience'
    )
    contact_phone = models.CharField(max_length=15, verbose_name='Contact phone', blank=False, null=False)
    ownership_form = models.CharField(
        max_length=50, verbose_name='Ownership form', blank=False, null=False, default='Natural person'
    )
    payment_method = models.CharField(
        max_length=50, verbose_name='Payment method', blank=False, null=False, default='Paypal'
    )
    about_me = models.TextField(max_length=1000, verbose_name='About me', blank=False, null=False)
    portfolio = models.FileField(
        verbose_name='Professional portfolio', upload_to='profiles/portfolio', blank=True, null=True
    )
    image = models.ImageField(
        verbose_name='Photo of freelancer', upload_to='profiles/freelancers_photo', blank=True, null=True
    )
    review = GenericRelation('Review', related_query_name='freelancer')

    class Meta:
        verbose_name = 'Freelancer'

    def __str__(self):
        return 'Freelancer profile'


class Customer(models.Model):
    """Модель заказчика"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment = models.PositiveIntegerField(verbose_name='Minimal payment for work', blank=False, null=False, default=0)
    experience = models.CharField(
        max_length=50, verbose_name='Work experience', blank=False, null=False, default='No experience'
    )
    contact_phone = models.CharField(
        max_length=15, verbose_name='Contact phone', blank=False, null=False, default='+7...'
    )
    ownership_form = models.CharField(
        max_length=50, verbose_name='Ownership form', blank=False, null=False, default='Legal entity'
    )
    about_us = models.TextField(max_length=1000, verbose_name='About me', blank=False, null=False)
    logo = models.ImageField(
        verbose_name='Photo of company', upload_to='profiles/customer_logo', blank=True, null=True
    )
    review = GenericRelation('Review', related_query_name='customer')

    class Meta:
        verbose_name = 'Customer'

    def __str__(self):
        return 'Customer profile'


class Review(models.Model):
    """Модель отзыва"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=512, verbose_name='Review', blank=False, null=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Review'

    def __str__(self):
        return 'Review to user'
