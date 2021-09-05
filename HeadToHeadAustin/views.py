from django.shortcuts import render

def matchup(request):
    return render(request, 'pickActivities/matchup.html')

def results(request):
    return render(request, 'pickActivities/results.html')