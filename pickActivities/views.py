from django.shortcuts import render
import ezsheets
import random
from PIL import Image
import matplotlib.pyplot as plt

def matchup(request):
    book = ezsheets.Spreadsheet('1Kdx1UyqB5MAltUPViK8Tsl3oB9i4KZXOFsZkvfu4om0')
    sheet = book['Sheet1']
    
    try:
        lastRoundWinnerRowNum = int(request.GET['winner'])       
        sheet.update(2,lastRoundWinnerRowNum, str(int(sheet.get(2,lastRoundWinnerRowNum))+1) )
    except:
        pass        

    optionNums = range(2,17)
    [option1RowNum,option2RowNum] = random.sample(optionNums,2)
    option1Title = sheet.get(1,option1RowNum)
    option2Title = sheet.get(1,option2RowNum)
    try:
        pic1 = Image.open('pickActivities/static/pickActivities/' + option1Title + '.PNG')
    except:
        pic1 = Image.open('pickActivities/static/pickActivities/' + option1Title + '.png')
    try:
        pic2 = Image.open('pickActivities/static/pickActivities/' + option2Title + '.PNG')
    except:
        pic2 = Image.open('pickActivities/static/pickActivities/' + option2Title + '.png')
    pic1.save('pickActivities/static/pickActivities/pic1.PNG')
    pic2.save('pickActivities/static/pickActivities/pic2.PNG')
    context = {'option1Title':option1Title, 'option2Title':option2Title, 'option1RowNum':option1RowNum, 'option2RowNum':option2RowNum}
    return render(request, 'pickActivities/matchup.html', context)



def results(request):
    book = ezsheets.Spreadsheet('1Kdx1UyqB5MAltUPViK8Tsl3oB9i4KZXOFsZkvfu4om0')
    sheet = book['Sheet1']
    plt.clf()

    optionTitles = []
    battlesWon = []
    for rowNum in range(2,17):
        optionTitles += [sheet.get(1,rowNum)]
        battlesWon += [int(sheet.get(2,rowNum))]

    fig, ax = plt.subplots(figsize = (8, 5))
    ax.barh(optionTitles,battlesWon)
    ax.invert_yaxis()
    ax.set_title('What Vacation Is Most Interesting?')
    plt.savefig('pickActivities/static/pickActivities/graph.PNG', bbox_inches="tight")

    return render(request, 'pickActivities/results.html')