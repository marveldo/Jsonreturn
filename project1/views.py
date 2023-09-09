from django.http import JsonResponse,HttpResponse
import json
import datetime


def home(request):
    return HttpResponse("welcome")

def slackview(request, param1, param2):
    current_date = datetime.date.today().strftime("%A")
    current_time = datetime.datetime.utcnow()
    showdict = {'slack_name': param1 ,
                'current_day': current_date,
                'utc_time': current_time,
                'track' : param2,
                
                }
    return JsonResponse(showdict, safe= True)

