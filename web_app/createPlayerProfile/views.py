from django.shortcuts import render
import pandas as pd

def createPlayerProfileView(request):

    try:
        playerName = request.POST['name']
        playerPosition = request.POST['position']
        playerHeight = request.POST['height']
        matchesYear1 = request.POST['matches-year1']
        goalsYear1 = request.POST['goals-year1']
        matchesYear2 = request.POST['matches-year2']
        goalsYear2 = request.POST['goals-year2']
    except:
        return render(request, 'createPlayerProfile.html', {"playerName": "", "playerPosition": "", "playerHeight":0,
                                "matchesYear1":0, "goalsYear1":0, "matchesYear2":0, "goalsYear2":0})

    print(request.POST)

    return render(request, 'createPlayerProfile.html', {"playerName": playerName, "playerPosition": playerPosition,
                    "playerHeight": playerHeight, "matchesYear1": matchesYear1, "goalsYear1": goalsYear1,
                    "matchesYear2": matchesYear2, "goalsYear2": goalsYear2})

