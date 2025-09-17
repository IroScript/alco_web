from main.models import CompanyInfo

def company(request):
    try:
        company = CompanyInfo.objects.first()
    except Exception:
        company = None
    return {'company': company} 