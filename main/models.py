from django.db import models
# from ckeditor.fields import RichTextField  # Uncomment when CKEditor is installed

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    personal_profile_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    personal_profile_text = models.CharField(max_length=100, blank=True)
    Homepage_middle_title_text = models.CharField(max_length=300, blank=True)
    rating_text = models.CharField(max_length=100, blank=True)
    Homepage_middle_details_text = models.TextField(blank=True)
    trusted_people_photo_first = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    trusted_people_photo_second = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    trusted_people_photo_third = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    trusted_people_photo_fourth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    trusted_people_photo_fifth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    trusted_people_statement = models.TextField(blank=True)
    learn_more_button = models.CharField(max_length=100, blank=True)
    lower_buttons_photo_first = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    lower_buttons_title_text_first = models.CharField(max_length=100, blank=True)
    lower_buttons_small_display_text_first = models.CharField(max_length=200, blank=True)
    lower_buttons_photo_second = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    lower_buttons_title_text_second = models.CharField(max_length=100, blank=True)
    lower_buttons_small_display_text_second = models.CharField(max_length=200, blank=True)
    lower_buttons_photo_third = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    lower_buttons_title_text_third = models.CharField(max_length=100, blank=True)
    lower_buttons_small_display_text_third = models.CharField(max_length=200, blank=True)
    watch_video = models.TextField(blank=True, max_length=1000, verbose_name="Video URL or Embed Code")
    use_video_as_main_button = models.BooleanField(default=False, verbose_name="Use this video as the main button?")
    circle_photo_first = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_first = models.CharField(max_length=200, blank=True)
    circle_photo_second = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_second = models.CharField(max_length=200, blank=True)
    circle_photo_third = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_third = models.CharField(max_length=200, blank=True)
    circle_photo_fourth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_fourth = models.CharField(max_length=200, blank=True)
    circle_photo_fifth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_fifth = models.CharField(max_length=200, blank=True)
    circle_photo_six = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_six = models.CharField(max_length=200, blank=True)
    circle_photo_seventh = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_seventh = models.CharField(max_length=200, blank=True)
    circle_photo_eighth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_eighth = models.CharField(max_length=200, blank=True)
    circle_photo_nineth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_nineth = models.CharField(max_length=200, blank=True)
    circle_photo_tenth = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    circle_text_tenth = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class BannerText(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")

class TherapeuticClass(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    generic_name = models.CharField(max_length=100, default="")
    composition = models.CharField(max_length=500, default="")
    indication = models.CharField(max_length=1000, default="")
    dosage = models.CharField(max_length=500, default="")
    pack_size = models.CharField(max_length=200, default="")
    therapeutic_class = models.ForeignKey(TherapeuticClass, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    # description = RichTextField()  # Uncomment when CKEditor is installed
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # main image
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    pdf = models.FileField(upload_to='product_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product.name} Image"