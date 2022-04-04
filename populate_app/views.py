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

    for id_, row in enumerate(reader): # iterate through rows of csv assigning columns to variables and creating objects 

            # Athletes data
            id = row[0]  
            name = row[1]
            sex = row[2]
            height = row[4]
            weight = row[5]
            team = row[6]

            # Olympic games data
            year = row[9]
            season = row[10]
            city = row[11]

            # events data
            event_name = row[13]
            sport_name = row[12]

            # medals
            medal = row[14]
            athlete_age = row[3]
            if(athlete_age != 'NA'):
                athlete_age = float(row[3])
            else:
                athlete_age = None

            # save athlete object
            try:
                obj = Athlete.objects.get(pk=id)
            except Athlete.DoesNotExist:
                athlete = Athlete(id, name, sex, height, weight, team)  
                athlete.save()
                print("Successfully added athlete: ", name)
            
            # save Olympic games object 
            try:
                obj = Olympic.objects.get(year=year, city=city) # check if olympic game already exists 
            except Olympic.DoesNotExist:
                obj = Olympic(olympic_id, year, season, city) # create olympic object and increment Id, change for slug later
                olympic_id += 1
                obj.save()
                print("Successfully added olympic: " + city + year)

            get_olympic_obj = Olympic.objects.get(year=year, city=city) # get olympic game that the event took place in
            get_athlete_obj = Athlete.objects.get(pk = id) # Get athlete object to add as foreign key 
            try:
                obj = Event.objects.get(event_name=event_name, olympic_game=get_olympic_obj.id) # check if this event already exists
                obj.athletes.add(id) 
            except Event.DoesNotExist:
                obj = Event(event_id, event_name, sport_name, get_olympic_obj.id) # create event object and increment Id, change for slug later
                event_id += 1
                obj.save()
                obj.athletes.add(id)
                get_athlete_obj.events_count += 1
                get_athlete_obj.save()
                print("Successfully added event: ", event_name)

            # insert medals objs
            get_event_obj = Event.objects.get(event_name=event_name, olympic_game=get_olympic_obj.id) # Get event object to add as foreign key
            try:
                medal_exists = Medal.objects.get(event_name=get_event_obj.id, olympic_game=get_olympic_obj.id )
            except Medal.DoesNotExist:
                if(medal != "" and medal != 'NA'): # check if there's a medal for this athlete in this event. AND NOT NA
                    medal_obj = Medal(medal_id, get_event_obj.id, get_olympic_obj.id, medal, athlete_age)
                    medal_id += 1
                    medal_obj.save()
                    medal_obj.athlete.add(get_athlete_obj.id)
                    get_athlete_obj.medals_count += 1
                    get_athlete_obj.save()
                    print("Successfully inserted medal: " + medal + " for " + event_name + " event of " + str(get_olympic_obj.year))

# todo test full csv. 

    csv_file.close()
    fs.delete(tmp_file) # delete csv file after importing data 
    return Response(status=status.HTTP_200_OK, 
                data={
                    'message': 'Success', 
                    }) 
            