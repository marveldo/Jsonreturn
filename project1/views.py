from django.http import JsonResponse,HttpResponse
import json
import datetime


def home(request):
    return HttpResponse("welcome")

def slackview(request, slackname, track):
    current_date = datetime.date.today().strftime("%A")
    current_time = datetime.datetime.utcnow()
    showdict = {'slack_name': slackname,
                'current_day': current_date,
                'utc_time': current_time,
                'track' : track,
                }
    return JsonResponse(showdict, safe= True)

