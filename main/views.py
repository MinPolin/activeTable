from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Data

def data_store(req):
    print('pppp')
    ret_dict = dict()
    get_data = req.GET
    base_id = get_data['base_id']
    fon_id = get_data['fon_id']
    if base_id and fon_id:
        new = Data(base_id=base_id, fon_id=fon_id)
        new.save()
        ret_dict['flag'] = True
    else:
        ret_dict['flag'] = False
    return JsonResponse(ret_dict)

def get_one(req):
    ret_dict = dict()
    test = Data.objects.all()
    for item in test:
        print(item.base_id, item.status)
    data = Data.objects.filter(status='w').first()

    print(data)
    if data:
        ret_dict['base_id'] = data.base_id
        ret_dict['fon_id'] = data.fon_id
        ret_dict['flag'] = True
        data.status = 'd'
        data.save()

    else:
        ret_dict['flag'] = False

    return JsonResponse(ret_dict)

def set_status(req):
    ret_dict = dict()
    status = req.GET['status']

    error_text = req.GET['error_text']
    base_id = req.GET['base_id']
    data = Data.objects.get(base_id=base_id, status='d')
    data.status = status
    data.error_text=error_text
    data.save()
    return JsonResponse(ret_dict)

def get_status(req):
    ret_dict = dict()
    st='wd'

    STATUS = (
        ('w', "Ожидает отправки"),
        ('d', 'Отправлен'),
        ('s', 'Успешно сохранен'),
        ('e', 'Ошибка'),
    )
    data = Data.objects.all()
    for item in data:
        st+=item.status
    for k,v in STATUS:
        ret_dict[v]=st.count(k)

    return JsonResponse(ret_dict)






def index(req):
    return render(req,'index.html',locals())