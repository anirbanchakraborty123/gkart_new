from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'info':'Welcome to the REST-API for GKART-Ecomm'})
    