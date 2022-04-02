import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Models import
from athletes.models import Athlete
from medals.models import Medal
from olympics.models import Olympic
from events.models import Event 

fs = FileSystemStorage(location='tmp/')

@csrf_exempt
@api_view(['POST'])
def upload_data(request):
    file = request.FILES["file"]

    content = file.read()
    file_content = ContentFile(content)
    file_name = fs.save(
        "_tmp.csv", file_content
    )
    tmp_file = fs.path(file_name)

    csv_file = open(tmp_file, errors = "ignore")
    reader = csv.reader(csv_file)
    next(reader) # Ignore column names 
    olympic_id = 0
    event_id = 0
    medal_id = 0
    athletes_list = []

    for id_, row in enumerate(reader):

            # Athletes data
            id = row[1] # change all for -1 when changing csv file 
            name = row[2]
            sex = row[3]
            height = row[5]
            weight = row[6]
            team = row[7]

            # Olympic games data
            year = row[10]
            season = row[11]
            city = row[12]

            # events data
            event_name = row[14]
            sport_name = row[13]

            # medals
            medal = row[15]
            athlete_age = float(row[4])

            athlete = Athlete(id, name, sex, height, weight, team) # save athlete object 
            athletes_list.append(id)
            athlete.save()
            
            # save Olympic games object 
            try:
                obj = Olympic.objects.get(year=year, city=city) # check if olympic game already exists 
            except Olympic.DoesNotExist:
                obj = Olympic(olympic_id, year, season, city) # create olympic object and increment Id, change for slug later
                olympic_id += 1
                obj.save()

            get_olympic_obj = Olympic.objects.get(year=year, city = city) # get olympic game that the event took place in
            try:
                obj = Event.objects.get(event_name=event_name, olympic_game = get_olympic_obj.id) # check if this event already exists 
            except Olympic.DoesNotExist:
                obj = Event(event_id, event_name, sport_name, get_olympic_obj.id) # create event object and increment Id, change for slug later
                event_id += 1
                obj.save()
                obj.athletes.add(id)

            # insert medals objs
            get_event_obj = Event.objects.get(event_name=event_name, olympic_game = get_olympic_obj.id)
            get_athlete_obj = Athlete.objects.get(name=name)
            print(get_athlete_obj)
            if(medal != ""): # check if there's a medal for this athlete in this event. 
                medal_obj = Medal(medal_id, get_event_obj.id, get_olympic_obj.id, get_athlete_obj.id, medal, athlete_age)
                medal_id += 1
                medal_obj.save()

# todo test full csv. 

    csv_file.close()
    fs.delete(tmp_file) # delete csv file after importing data 
    return Response(status=status.HTTP_200_OK, 
                data={
                    'message': 'Success', 
                    }) 
            