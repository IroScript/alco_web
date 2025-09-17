# Video Popup Setup Guide

## How to Use the "Watch Our Corporate Video" Feature

### 1. Setting Up the Video URL in Django Admin

1. **Access Django Admin Panel**
   - Go to `http://yourdomain.com/admin/`
   - Login with your admin credentials

2. **Navigate to Company Info**
   - Find and click on "Company infos" under the "Main" section
   - Click on your existing company record or create a new one

3. **Add Video URL**
   - Find the "Watch video" field
   - Enter your video URL in one of these formats:

### 2. Supported Video Platforms & URL Formats

#### YouTube Videos (Recommended - Most Reliable)
```
# Standard YouTube watch URL
https://www.youtube.com/watch?v=VIDEO_ID

# YouTube short URL
https://youtu.be/VIDEO_ID

# YouTube embed URL (already in correct format)
https://www.youtube.com/embed/VIDEO_ID
```

#### Facebook Videos
```
# Facebook video post URL
https://www.facebook.com/username/videos/123456789/

# Facebook video with query parameters
https://www.facebook.com/username/videos/123456789/?t=123
```

#### Vimeo Videos
```
# Standard Vimeo URL
https://vimeo.com/123456789

# Vimeo with query parameters
https://vimeo.com/123456789?h=abcdef123456
```

#### Dailymotion Videos
```
# Dailymotion video URL
https://www.dailymotion.com/video/x8c0q1

# Dailymotion with query parameters
https://www.dailymotion.com/video/x8c0q1?start=30
```

#### Twitch Videos
```
# Twitch video URL
https://www.twitch.tv/videos/123456789

# Twitch clip URL
https://www.twitch.tv/username/clip/ABC123
```

#### TikTok Videos
```
# TikTok video URL
https://www.tiktok.com/@username/video/1234567890123456789
```

#### Instagram Posts (with videos)
```
# Instagram post URL
https://www.instagram.com/p/ABC123/
```

#### LinkedIn Posts (with videos)
```
# LinkedIn post URL
https://www.linkedin.com/posts/username_activity-1234567890123456789
```

#### Direct Video Files
```
# MP4 file
https://example.com/video.mp4

# WebM file
https://example.com/video.webm

# OGV file
https://example.com/video.ogv
```

#### Iframe Embed Codes
```
# Complete iframe code
<iframe src="https://www.youtube.com/embed/VIDEO_ID" width="560" height="315" frameborder="0" allowfullscreen></iframe>

# Just the iframe src
https://www.youtube.com/embed/VIDEO_ID
```

### 3. Common Issues & Solutions

#### "Refused to Connect" Error

This error typically occurs due to:

1. **Cross-Origin Resource Sharing (CORS) Restrictions**
   - Some video platforms block embedding from certain domains
   - Solution: Use the platform's official embed URL format

2. **Mixed Content (HTTP/HTTPS)**
   - If your site is HTTPS but video is HTTP
   - Solution: Use HTTPS video URLs only

3. **Platform-Specific Restrictions**
   - Some platforms require specific parameters
   - Solution: Use the exact URL formats listed above

#### Platform-Specific Troubleshooting

**Facebook Videos:**
- Facebook videos require the page to be publicly accessible
- Private videos cannot be embedded
- Use the official Facebook embed format

**Vimeo Videos:**
- Vimeo videos must have embedding enabled by the uploader
- Check video privacy settings in Vimeo

**Dailymotion Videos:**
- Most Dailymotion videos support embedding
- Ensure the video is not region-restricted

**Twitch Videos:**
- Twitch requires the `parent` parameter for security
- The system automatically adds your domain as parent

### 4. How It Works

#### Frontend Behavior
- **Video Button**: Located at the bottom-right corner of the page
- **Click Action**: Opens a modal popup with the video
- **Modal Features**:
  - Responsive design (works on mobile and desktop)
  - Close button (×) in the top-right corner
  - Click outside to close
  - Press Escape key to close
  - Auto-play for supported platforms
  - Prevents background scrolling when open
  - Error handling with fallback options

#### Backend Processing
- Django automatically converts various URL formats to embed format
- Supports multiple video platforms with proper URL conversion
- Handles iframe embed codes
- Passes processed URL to frontend via JSON

### 5. Testing Your Video URL

1. **Test Direct Access**
   - Open the video URL directly in a browser
   - Ensure it plays correctly

2. **Test Embed Format**
   - For YouTube: Replace `watch?v=` with `embed/`
   - For Vimeo: Replace `vimeo.com/` with `player.vimeo.com/video/`

3. **Check Browser Console**
   - Open Developer Tools (F12)
   - Look for error messages in the Console tab
   - Check the Network tab for failed requests

### 6. Example URLs to Test

#### YouTube Examples
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
https://www.youtube.com/embed/dQw4w9WgXcQ
```

#### Facebook Example
```
https://www.facebook.com/facebook/videos/10157241591791729/
```

#### Vimeo Example
```
https://vimeo.com/148751763
```

#### Dailymotion Example
```
https://www.dailymotion.com/video/x8c0q1
```

### 7. Error Handling Features

The system now includes:

- **Automatic URL Conversion**: Converts various URL formats to embed format
- **Error Detection**: Shows helpful error messages if video fails to load
- **Fallback Options**: "Open in new tab" link when embedding fails
- **Loading Timeout**: 10-second timeout with user feedback
- **Cross-Platform Support**: Handles different video platforms automatically

### 8. Troubleshooting

#### Video Not Playing
1. **Check URL Format**: Ensure the URL is in a supported format
2. **Test URL**: Try opening the URL directly in a browser
3. **Check Console**: Open browser developer tools and check for errors
4. **Admin Panel**: Verify the URL is saved correctly in Django admin
5. **Platform Restrictions**: Some platforms block embedding from certain domains

#### "Refused to Connect" Error
1. **CORS Issues**: Check if the video platform allows embedding
2. **Mixed Content**: Ensure both your site and video use HTTPS
3. **Domain Restrictions**: Some platforms require whitelisting
4. **Try Alternative Format**: Use a different URL format for the same video

#### Modal Not Opening
1. **JavaScript Errors**: Check browser console for JavaScript errors
2. **URL Field**: Ensure the `watch_video` field has a value
3. **Template**: Verify the template changes are applied

#### Mobile Issues
1. **Responsive Design**: The modal is designed to work on mobile
2. **Touch Events**: Tap outside the modal to close
3. **Video Size**: Videos automatically resize for mobile screens
4. **Platform Support**: Some platforms have limited mobile embedding support

### 6. Customization Options

#### Change Modal Title
Edit the template file `main/templates/index.html`:
```html
<div class="video-modal-title">
    {% if company and company.name %}
        {{ company.name }} Corporate Video
    {% else %}
        Alco Pharma Ltd. Corporate Video
    {% endif %}
</div>
```

#### Change Button Text
Edit the video popup button:
```html
<div class="video-popup" onclick="watchVideo()">
    <span class="play-button" style="font-size:1.2rem;margin-right:0.5rem;">▶️</span>
    <span style="font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
        Watch Our Corporate Video
    </span>
</div>
```

#### Modify Modal Styling
Edit the CSS in the `<style>` section:
```css
.video-modal-content {
    width: 90%;
    max-width: 800px;  /* Change modal width */
    max-height: 80vh;  /* Change modal height */
    background: #1a2230;  /* Change background color */
}
```

### 7. Security Considerations

- **URL Validation**: The system accepts any URL format
- **XSS Protection**: Django's template escaping prevents XSS attacks
- **Iframe Security**: Videos are loaded in iframes with appropriate security attributes
- **Content Security Policy**: Consider adding CSP headers if needed

### 8. Performance Notes

- **Lazy Loading**: Videos only load when the modal is opened
- **Memory Management**: Video stops playing when modal is closed
- **Network Usage**: Videos stream from their original source
- **Caching**: Browser may cache video content

### 9. Browser Compatibility

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile Browsers**: iOS Safari, Chrome Mobile, Samsung Internet
- **Iframe Support**: Requires iframe support (most modern browsers)
- **JavaScript**: Requires JavaScript enabled

### 10. Testing Checklist

- [ ] Video URL is saved in Django admin
- [ ] Video button appears on the page
- [ ] Clicking button opens modal
- [ ] Video plays correctly
- [ ] Close button works
- [ ] Click outside closes modal
- [ ] Escape key closes modal
- [ ] Works on mobile devices
- [ ] No JavaScript errors in console
- [ ] Video stops when modal is closed
- [ ] Error handling works for failed videos
- [ ] "Open in new tab" link works

### 11. Troubleshooting Steps

If your video isn't working:

1. **Check URL Format**: Ensure it matches one of the supported formats
2. **Test Direct Access**: Open the URL directly in a browser
3. **Check Console Errors**: Look for error messages in browser developer tools
4. **Verify Platform Support**: Ensure the video platform allows embedding
5. **Check Privacy Settings**: Some videos may be private or restricted
6. **Try Alternative Format**: Use a different URL format for the same video
7. **Contact Support**: If issues persist, check the video platform's documentation

### 12. Platform-Specific Notes

**YouTube**: Most reliable, supports all features
**Facebook**: Requires public videos, may have domain restrictions
**Vimeo**: Requires embedding to be enabled by uploader
**Dailymotion**: Generally good support, check region restrictions
**Twitch**: Requires parent domain parameter for security
**TikTok**: Limited embedding support, may not work on all domains
**Instagram**: Limited embedding support, primarily for public posts
**LinkedIn**: Limited embedding support, primarily for public posts

---

**Note**: This feature now supports multiple video platforms with automatic URL conversion and error handling. Simply add a video URL in the Django admin panel and the popup will work automatically! 