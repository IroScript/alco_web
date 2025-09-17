from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, CompanyInfo
from .models import ProductImage, BannerText, TherapeuticClass

# from ckeditor.widgets import CKEditorWidget  # Uncomment when CKEditor is installed
from django import forms

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10

class ProductAdminForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())  # Uncomment when CKEditor is installed
    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductImageInline]
    list_display = ('name', 'generic_name', 'therapeutic_class', 'is_active')
    search_fields = ('name', 'generic_name')
    list_filter = ('therapeutic_class', 'is_active')

    # No custom save_formset needed for image count

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(BannerText)
admin.site.register(TherapeuticClass)
admin.site.register(CompanyInfo)