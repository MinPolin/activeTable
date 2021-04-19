from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Data

def data_store(req):
    ret_dict = dict()
    get_data = req.POST
    base_id = get_data['base_id']
    fon_id = get_data['fon_id']
    new = Data(base_id=base_id, fon_id=fon_id)
    new.save()
    return JsonResponse(ret_dict)

def get_one(req):
    ret_dict = dict()
    data = Data.objects.first()
    if data:
        ret_dict['base_id'] = data.base_id
        ret_dict['fon_id'] = data.fon_id
        ret_dict['flag'] = True
        data.delete()
    else:
        ret_dict['flag'] = False

    return JsonResponse(ret_dict)