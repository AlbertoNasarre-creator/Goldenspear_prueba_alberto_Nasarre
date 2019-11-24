from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse
from mainapp.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mainapp.utils import *
import json

def index(request):
    
    return render_to_response('index.html')


@csrf_exempt
def process(request):

    if request.method == "POST":

        code = request.POST.get("code")
        crc = calculate_crc(code)

        
        shift = 0
        Mesagges = messages.objects.all()
        try:
            for item in Mesagges:
                shift += item.original_crc
        except:
            shift = 0

        cesar = encrypt_cesar(code,shift)
        message = messages(original=code,encripted=cesar,original_crc=crc)
        message.save()
    else:

        return JsonResponse({"status":"error","msg":"error"})


    return JsonResponse({"status":"ok","msg":code+" "+cesar+" "+str(crc)})

        
@csrf_exempt
def history(request):

    if request.method == "GET":
        Mesagges = messages.objects.all()

        
        history = []
        for item in Mesagges:
            history.append([item.original,item.encripted,item.original_crc])
    else:

        history = "error"


    return JsonResponse({"status":"ok","msg":history})

@csrf_exempt
def delete(request):

    if request.method == "GET":

        messages.objects.all().delete()

        return JsonResponse({"status":"ok"})
        
    else:

        return JsonResponse({"status":"error","msg":"error"})


    return JsonResponse({"status":"error","msg":"error"})

@csrf_exempt
def orthographic(request):

    if request.method == "POST":
        body = request.body.decode("utf8")
        json_data = json.loads(body)
        text = json_data.get("data")
        
        response = orthographic_corrector(text)

        return JsonResponse({"status":"error","msg":response})

    else:

        return JsonResponse({"status":"error","msg":"error"})