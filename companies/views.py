from django.http import JsonResponse
from django.shortcuts import render
from .models import Company

def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all().values()  # Query all Company objects
        return JsonResponse(list(companies), safe=False)  # Return JSON response
    return JsonResponse({'error': 'Invalid request method'}, status=405)
