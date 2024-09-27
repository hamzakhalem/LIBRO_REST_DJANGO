from django.http import JsonResponse

def handler404(request, exp):
    message = 'path not foundl'
    response = JsonResponse(data={'data': message})
    response.status_code = 404 
    return response

def handler500(request):
    message = 'internal erro'
    response = JsonResponse(data={'data': message})
    response.status_code = 500
    return response