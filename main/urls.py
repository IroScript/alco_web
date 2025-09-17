from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views




urlpatterns = [
    # Add your URL patterns here
    # Example:
    # path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)