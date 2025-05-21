from django.contrib import admin
from .models import AppVarity, AppReview, AppVerification, Store

# Register your models here.

class AppRevieInLine(admin.TabularInline):
    model = AppReview
    extra = 2

class AppVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [AppRevieInLine]

class StoreAdmin(admin.ModelAdmin): 
    list_display = ('name', 'location')
    filter_horizontal = ('app_varities', )

class AppVerificationAdmin(admin.ModelAdmin):
    list_display = ('app1', 'certificate_number')

# class AppBuyingAdmin(admin.ModelAdmin):
#     list_display = ('name', 'buying', 'issue_date')

admin.site.register(AppVarity, AppVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AppVerification, AppVerificationAdmin)
# admin.site.register(AppBuying, AppBuyingAdmin)