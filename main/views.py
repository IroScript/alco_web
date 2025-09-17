from django.shortcuts import render, get_object_or_404
from .models import Product, CompanyInfo
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
import re

def home(request):
    company = CompanyInfo.objects.first()
    
    # Process watch_video URL for embedding
    watch_video_embed = None
    if company and company.watch_video:
        video_url = company.watch_video.strip()
        
        # Check if it's already an iframe embed code
        if '<iframe' in video_url:
            # Extract src from iframe
            src_match = re.search(r'src=["\']([^"\']+)["\']', video_url)
            if src_match:
                watch_video_embed = src_match.group(1)
            else:
                watch_video_embed = video_url
        else:
            # Convert various video platform URLs to embed format
            if 'youtube.com/watch?v=' in video_url:
                video_id = video_url.split('v=')[1].split('&')[0]
                watch_video_embed = f'https://www.youtube.com/embed/{video_id}'
            elif 'youtu.be/' in video_url:
                video_id = video_url.split('youtu.be/')[1].split('?')[0]
                watch_video_embed = f'https://www.youtube.com/embed/{video_id}'
            elif 'youtube.com/embed/' in video_url:
                watch_video_embed = video_url
            elif 'facebook.com/' in video_url and '/videos/' in video_url:
                # Convert Facebook video URL to embed format
                # Example: https://www.facebook.com/username/videos/123456789/
                # To: https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2Fusername%2Fvideos%2F123456789%2F
                encoded_url = video_url.replace(':', '%3A').replace('/', '%2F')
                watch_video_embed = f'https://www.facebook.com/plugins/video.php?href={encoded_url}&show_text=false&width=734&height=413&appId'
            elif 'dailymotion.com/video/' in video_url:
                # Convert Dailymotion video URL to embed format
                # Example: https://www.dailymotion.com/video/x8c0q1
                video_id = video_url.split('/video/')[1].split('?')[0]
                watch_video_embed = f'https://www.dailymotion.com/embed/video/{video_id}'
            elif 'vimeo.com/' in video_url:
                # Convert Vimeo video URL to embed format
                # Example: https://vimeo.com/123456789
                video_id = video_url.split('vimeo.com/')[1].split('?')[0]
                watch_video_embed = f'https://player.vimeo.com/video/{video_id}'
            elif 'twitch.tv/' in video_url:
                # Convert Twitch video URL to embed format
                # Example: https://www.twitch.tv/videos/123456789
                if '/videos/' in video_url:
                    video_id = video_url.split('/videos/')[1].split('?')[0]
                    watch_video_embed = f'https://player.twitch.tv/?video=v{video_id}&parent=localhost'
                elif '/clips/' in video_url:
                    clip_id = video_url.split('/clips/')[1].split('?')[0]
                    watch_video_embed = f'https://clips.twitch.tv/embed?clip={clip_id}&parent=localhost'
            elif 'tiktok.com/' in video_url:
                # Convert TikTok video URL to embed format
                # Example: https://www.tiktok.com/@username/video/1234567890123456789
                watch_video_embed = f'https://www.tiktok.com/embed/{video_url.split("/video/")[1].split("?")[0]}'
            elif 'instagram.com/' in video_url and '/p/' in video_url:
                # Convert Instagram post URL to embed format
                # Example: https://www.instagram.com/p/ABC123/
                post_id = video_url.split('/p/')[1].split('/')[0]
                watch_video_embed = f'https://www.instagram.com/p/{post_id}/embed/'
            elif 'linkedin.com/posts/' in video_url:
                # Convert LinkedIn post URL to embed format
                # Example: https://www.linkedin.com/posts/username_activity-1234567890123456789
                activity_id = video_url.split('activity-')[1].split('?')[0]
                watch_video_embed = f'https://www.linkedin.com/embed/feed/update/urn:li:activity:{activity_id}'
            else:
                # For other video platforms or direct video files, use as is
                # This includes direct MP4, WebM, etc. files
                watch_video_embed = video_url
    
    # Prepare image data for slider
    if company and (company.circle_photo_first or company.circle_photo_second or company.circle_photo_third or company.circle_photo_fourth or company.circle_photo_fifth or company.circle_photo_six or company.circle_photo_seventh or company.circle_photo_eighth or company.circle_photo_nineth or company.circle_photo_tenth):
        images_data = []
        if company.circle_photo_first:
            images_data.append({
                'src': company.circle_photo_first.url,
                'text': company.circle_text_first or 'Image 1'
            })
        if company.circle_photo_second:
            images_data.append({
                'src': company.circle_photo_second.url,
                'text': company.circle_text_second or 'Image 2'
            })
        if company.circle_photo_third:
            images_data.append({
                'src': company.circle_photo_third.url,
                'text': company.circle_text_third or 'Image 3'
            })
        if company.circle_photo_fourth:
            images_data.append({
                'src': company.circle_photo_fourth.url,
                'text': company.circle_text_fourth or 'Image 4'
            })
        if company.circle_photo_fifth:
            images_data.append({
                'src': company.circle_photo_fifth.url,
                'text': company.circle_text_fifth or 'Image 5'
            })
        if company.circle_photo_six:
            images_data.append({
                'src': company.circle_photo_six.url,
                'text': company.circle_text_six or 'Image 6'
            })
        if company.circle_photo_seventh:
            images_data.append({
                'src': company.circle_photo_seventh.url,
                'text': company.circle_text_seventh or 'Image 7'
            })
        if company.circle_photo_eighth:
            images_data.append({
                'src': company.circle_photo_eighth.url,
                'text': company.circle_text_eighth or 'Image 8'
            })
        if company.circle_photo_nineth:
            images_data.append({
                'src': company.circle_photo_nineth.url,
                'text': company.circle_text_nineth or 'Image 9'
            })
        if company.circle_photo_tenth:
            images_data.append({
                'src': company.circle_photo_tenth.url,
                'text': company.circle_text_tenth or 'Image 10'
            })
    else:
        # Fallback images
        images_data = [
            {
                'src': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80',
                'text': 'Empowering Health'
            },
            {
                'src': 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80',
                'text': 'Innovative Research'
            },
            {
                'src': 'https://images.unsplash.com/photo-1511174511562-5f97f4f4eab6?auto=format&fit=crop&w=400&q=80',
                'text': 'Global Impact'
            }
        ]
    
    return render(request, 'index.html', {
        'company': company,
        'images_json': images_data,
        'watch_video_embed': watch_video_embed
    })

def product_list(request):
    # Get all distinct values for dropdowns
    all_products = Product.objects.all()
    brand_names = all_products.values_list('name', flat=True).distinct().order_by('name')
    generic_names = all_products.values_list('generic_name', flat=True).distinct().order_by('generic_name')
    therapeutic_classes = all_products.exclude(therapeutic_class__isnull=True).values_list('therapeutic_class__name', flat=True).distinct().order_by('therapeutic_class__name')

    # Get filter parameters
    search_query = request.GET.get('search', '')
    letter = request.GET.get('letter', '')
    sort_by = request.GET.get('sort_by', 'brand')
    filter_value = request.GET.get('filter_value', '')

    # Initialize queryset
    products = all_products

    # Apply filters
    if filter_value:
        if sort_by == 'brand':
            products = products.filter(name=filter_value)
        elif sort_by == 'generic':
            products = products.filter(generic_name=filter_value)
        elif sort_by == 'therapeutic':
            products = products.filter(therapeutic_class__name=filter_value)
    
    # Apply sorting
    if sort_by == 'generic':
        products = products.order_by('generic_name')
    elif sort_by == 'therapeutic':
        products = products.order_by('therapeutic_class__name', 'name')
    else:  # sort by brand name
        products = products.order_by('name')
    
    # Apply search filter
    if search_query:
        if sort_by == 'generic':
            products = products.filter(generic_name__icontains=search_query)
        elif sort_by == 'therapeutic':
            products = products.filter(therapeutic_class__name__icontains=search_query)
        else:
            products = products.filter(name__icontains=search_query)
    
    # Apply letter filter
    if letter and letter != 'ALL':
        if sort_by == 'generic':
            products = products.filter(generic_name__istartswith=letter)
        elif sort_by == 'therapeutic':
            products = products.filter(therapeutic_class__name__istartswith=letter)
        else:
            products = products.filter(name__istartswith=letter)

    # Pagination
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle AJAX requests
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('partials/product_grid.html', {
            'products': page_obj.object_list,
            'page_obj': page_obj,
            'paginator': paginator,
            'request': request,
        })
        return HttpResponse(html)

    # Regular request
    company = CompanyInfo.objects.first()
    return render(request, 'product_list.html', {
        'products': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
        'brand_names': brand_names,
        'generic_names': generic_names,
        'therapeutic_classes': therapeutic_classes,
        'company': company,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = product.images.all()
    similar_products = Product.objects.filter(therapeutic_class=product.therapeutic_class).exclude(pk=product.pk)[:6]
    return render(request, 'individual_product.html', {
        'product': product,
        'images': images,
        'similar_products': similar_products,
    })
