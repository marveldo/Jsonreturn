from django.http import JsonResponse,HttpResponse
import json
import datetime


def home(request):
    return HttpResponse("welcome")

def slackview(request):
    current_date = datetime.date.today().strftime("%A")
    current_time = datetime.datetime.utcnow()
    slackname = request.GET.get('slackname')
    track = request.GET.get('track')
    showdict = {'slack_name': slackname,
                'current_day': current_date,
                'utc_time': current_time,
                'track' : track,
                'github_file_url': 
                "https://github.com/marveldo/Jsonreturn/blob/main/project1/views.py",
                'github_repo_url': 
                "https://github.com/marveldo/Jsonreturn",
                "status_code" : 200
                }
    return JsonResponse(showdict, safe= True)

