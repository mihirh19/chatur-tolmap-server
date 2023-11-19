from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Items
import json
# Create your views here.
def home(request, *args, **kwargs):
   return JsonResponse({
      "message" : "api is running",
   })

@csrf_exempt  
def fetch_items(request, *args, **kwargs):
   if request.method == "GET":
      data  = list(Items.objects.values())
      return JsonResponse({
         "data" : data,
      }, status=200)
      
@csrf_exempt     
def insert_items(request):
   if request.method == "POST":
      data = json.loads(request.body.decode("UTF-8"))
      item = Items.objects.create(**data)
      item.save()
      return JsonResponse({
         "message" : "Item added successfully",
         
      }, status=200)


@csrf_exempt
def update_items(request, id=0):
   if request.method == "PUT":
      data = json.loads(request.body.decode("UTF-8"))
      item = Items.objects.filter(id=id).update(**data)
      return JsonResponse({
         "message" : "Item updated successfully",
         
      }, status=200)

@csrf_exempt
def delete_items(request, id=0):
   if request.method == "DELETE":
      item = Items.objects.get(id=id)
      item.delete()
      return JsonResponse({
         "message" : "Item deleted successfully",
         
      }, status=200)