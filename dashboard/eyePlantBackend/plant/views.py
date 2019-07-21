from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Plant

def plant_details(request, plant_id):
    if request.method == "GET":
        response = {
            "status": 404,
            "response": {}
        }
        
        try:
            plant = Plant.objects.get(id=plant_id)
        except ObjectDoesNotExist:
            response['response'] = "The plant does not exist. OHNO :("
            return JsonResponse(response)
        
        response['status'] = 200
        response['response'] = plant.to_dict()
        return JsonResponse(response)
