from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from django.core import serializers

from django.http import JsonResponse

import json
import logging
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
    f=open('/Users/fdhcg/Desktop/wbdweb/myapp/record/h1.json','r')

    load_dict=json.load(f)
    load_dict["label1"]+=1
    f.close()
    f=open('/Users/fdhcg/Desktop/wbdweb/myapp/record/h1.json','w')
    json.dump(load_dict,f)
    f.close()
    return JsonResponse({"sig": 1},safe=False)
    
@require_http_methods(["GET"])

def show_label(request):

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
    response={}
    f=open('/Users/fdhcg/Desktop/wbdweb/myapp/record/h1.json','r')
    load_dict=json.load(f)
    f.close()
    return JsonResponse(load_dict,safe=False)

