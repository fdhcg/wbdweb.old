from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from django.core import serializers

from django.http import JsonResponse

import json
import os

# Create your views here.

@require_http_methods(["GET"])

def add_label(request):
    # try:
    #     f=open('h1.json','r')
    #     logging.debug(f)
    #     load_dict=json.load(f)
    #     load_dict.label1+=1
    #     f.close()
    #     f=open('h1.json','w')
    #     json.dump(load_dict,f)
    #     f.close()

    # except  Exception as e:
    #     pass
    f=open(os.getcwd()+'/myapp/data/h1.json','r')

    load_dict=json.load(f)
    load_dict["label1"]+=1
    f.close()
    f=open(os.getcwd()+'/myapp/data/h1.json','w')
    json.dump(load_dict,f)
    f.close()
    return JsonResponse({"sig": 1},safe=False)
    
@require_http_methods(["GET"])

def show_label(request):
    f=open(os.getcwd()+'/myapp/data/h1.json','r')
    load_dict=json.load(f)
    f.close()
    return JsonResponse(load_dict,safe=False)

@require_http_methods(["POST"])
def pull_data(request):
    f=open(os.getcwd()+'/myapp/data/datalist.json','r')
    load_dict=json.load(f)
    f.close()
    target=json.loads(request.body)
    if target["target"]=='*':
        return JsonResponse(load_dict,safe=False)
    else:
        result_dict={}
        for key,value in load_dict.items():
            if target["target"] in key:
                item={key:value}
                result_dict.update(item)
        return JsonResponse(result_dict,safe=False)

