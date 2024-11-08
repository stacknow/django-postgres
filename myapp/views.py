from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json

def get_users(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(name=data['name'], email=data['email'])
        return JsonResponse({'message': 'User created', 'user': {'name': user.name, 'email': user.email}}, status=201)
