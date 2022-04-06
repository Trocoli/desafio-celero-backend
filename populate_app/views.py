import csv
from shutil import ExecError
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
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
    """
    Função de popular app, recebe o CSV '120 years of olympics' que pode ser baixado através do link
    https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
    é necessário mandar um request através do postman pelo endpoint "http://localhost:8000/populate"
    na aba body é necessário enviar um método de POST através do form data 
    com a key de nome e tipo 'file' e inserindo o arquivo CSV,
    a função salva o arquivo no projeto temporariamente 
    e itera por cada Row associando os dados ás suas respectitivas colunas e cria os objetos não criados ou adiciona chaves estrangeiras.
    """
    file = request.FILES["file"] # recebe csv pelo file, salva na memória e salva no projeto e depois lê o arquivo

    content = file.read() 
    file_content = ContentFile(content)
    file_name = fs.save(
        "_tmp.csv", file_content
    )
    tmp_file = fs.path(file_name)

    csv_file = open(tmp_file, errors = "ignore") # errors = ignore troca o nome do arquivo '_temp' caso ja exista um csv com esse nome inserido 
    reader = csv.reader(csv_file)
    next(reader) # Ignore column names 
    olympic_id = 0 # ID's para criação de objeto, eventualmente trocar por função de criar slug 
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
            athlete_age = row[3] # só recebe idade quando ela estiver inserida, idade está relacionada a medalhas pois o aruivo não mostra a idade do atleta
            if(athlete_age != 'NA'): # mas a idade que ele tinha ao ganhar a medalha
                athlete_age = float(row[3])
            else:
                athlete_age = None

            # save athlete object
            try:
                athlete_obj = Athlete.objects.get(pk=id)
            except Athlete.DoesNotExist:
                athlete_obj = Athlete(id, name, sex, height, weight, team)  
                athlete_obj.save()
                print("Successfully added athlete: ", name)
            
            # save Olympic games object 
            try:
                olympic_obj = Olympic.objects.get(year=year, city=city) # check if olympic game already exists 
            except Olympic.DoesNotExist:
                olympic_obj = Olympic(olympic_id, year, season, city) # create olympic object and increment Id, change for slug later
                olympic_id += 1
                olympic_obj.save()
                print("Successfully added olympic: " + city + year)

        #    get_olympic_obj = Olympic.objects.get(year=year, city=city) # get olympic game that the event took place in
        #   get_athlete_obj = Athlete.objects.get(pk = id) # Get athlete object to add as foreign key


            # it's good up to this point, and obj creationg is good, the problem is only when adding athletes, 
            # need to find a way to check the whole line if the medal needs to be added and event needs to be added 

            try:
                obj = Event.objects.get(event_name=event_name, olympic_game=olympic_obj.id)
                obj.athletes.add(athlete_obj.id)
            except Event.DoesNotExist:
                obj = Event(event_id, event_name, sport_name, olympic_obj.id) # create event object and increment Id, change for slug later
                event_id += 1
                obj.save()
                obj.athletes.add(athlete_obj.id)
                print("Successfully added event: ", event_name)

            # insert medals objs
            try:
                Medal.objects.get(event_name=obj.id, olympic_game=olympic_obj.id, medal_type=medal )
            except Medal.DoesNotExist:
                if(medal != "" and medal != 'NA'): # check if there's a medal for this athlete in this event. AND NOT NA
                    medal_obj = Medal(medal_id, obj.id, olympic_obj.id, medal, athlete_age)
                    medal_id += 1
                    medal_obj.save()
                    medal_obj.athlete.add(athlete_obj.id)
                    athlete_obj.medals_count += 1
                    athlete_obj.save()
                    print("Successfully inserted medal: " + medal + " for " + event_name + " event of " + str(olympic_obj.year)) 

# todo test full csv. 

    csv_file.close()
    fs.delete(tmp_file) # delete csv file after importing data 
    return Response(status=status.HTTP_200_OK, 
                data={
                    'message': 'Success', 
                    }) 
            