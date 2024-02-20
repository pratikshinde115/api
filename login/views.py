from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import JsonResponse
import json
import requests

def home(request):
    # return provider_login_url 'google'
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect('/')    


def G_auth_api(request):
    try:
        if request.method == 'POST':
        # Assuming the POST data contains JSON
            data = json.loads(request.body)
            print(data)
            # Do something with the data
            # Example: Make a POST request to another API
            response = requests.post('https://example.com/api/', json=data)
            # Process the response from the external API
            if response.status_code == 200:
                return JsonResponse({'message': 'Success'})
            else:
                return JsonResponse({'message': 'Error'}, status=500)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON data'}, status=400)
        # else:
        #     return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)
    except Exception as e:
        print(e)  

