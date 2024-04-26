from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.admin import GenericTabularInline

from profiles.models import Freelancer, Customer, Review


class ReviewInline(GenericTabularInline):
    model = Review
    extra = 1


@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    """AdminView для модели Freelancer"""
    list_display = (
        'pk', 'user_username', 'user_email', 'user_first_name',
        'user_last_name', 'cost_of_work', 'experience', 'about_me_short',
    )
    search_fields = (
        'pk', 'user_username', 'user_email', 'user_first_name',
        'user_last_name', 'cost_of_work', 'experience', 'about_me',
    )
    inlines = [ReviewInline, ]
    fieldsets = [
        ('General Information', {
            'fields': (
                'user_first_name', 'user_last_name', 'user_email',
            ),
        }),
        ('Work Information', {
            'fields': (
                'cost_of_work', 'experience', 'about_me', 'contact_phone',
                'ownership_form', 'payment_method',
            ),
        }),
        ('Extra Information', {
            'fields': (
                'image', 'preview', 'portfolio',
            )
        })
    ]

    readonly_fields = ['user_username', 'user_email', 'user_first_name', 'user_last_name', 'preview']

    def user_username(self, obj):
        return obj.user.username

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    def user_email(self, obj):
        return obj.user.email

    def about_me_short(self, obj):
        if len(obj.about_me) >= 50:
            return obj.about_me[:50]
        return obj.about_me

    def preview(self, obj):
        return mark_safe('<img src="{}" style="max-height: 200px; max-width: 200px;" />'.format(obj.image.url))

    user_username.short_description = 'Username'
    user_email.short_description = 'Email'
    user_first_name.short_description = 'First Name'
    user_last_name.short_description = 'Last Name'
    about_me_short.short_description = 'About Me'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """AdminView для модели Customer"""
    list_display = (
        'pk', 'user_username', 'user_email', 'user_first_name', 'payment', 'experience', 'about_us_short',
    )
    search_fields = (
        'pk', 'user_username', 'user_email', 'user_first_name', 'payment', 'experience', 'about_us_short',
    )
    inlines = [ReviewInline, ]
    fieldsets = [
        ('General Information', {
            'fields': (
                'user_username', 'user_first_name', 'user_last_name', 'user_email',
            ),
        }),
        ('Work Information', {
            'fields': (
                'payment', 'experience', 'ownership_form', 'about_us', 'contact_phone'
            ),
        }),
        ('Extra Information', {
            'fields': (
                'logo', 'preview',
            ),
        }),
    ]

    readonly_fields = ['user_username', 'user_email', 'user_first_name', 'user_last_name', 'preview']

    def user_username(self, obj):
        return obj.user.username

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    def user_email(self, obj):
        return obj.user.email

    def about_us_short(self, obj):
        if len(obj.about_us) >= 50:
            return obj.about_us[:50]
        return obj.about_us

    def preview(self, obj):
        return mark_safe('<img src="{}" style="max-height: 200px; max-width: 200px;" />'.format(obj.logo.url))

    user_username.short_description = 'Username'
    user_email.short_description = 'Email'
    user_first_name.short_description = 'First Name'
    user_last_name.short_description = 'Last Name'
    about_us_short.short_description = 'About Us'
