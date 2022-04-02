import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from athletes.models import Athlete
from olympics.models import Olympic

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

    for id_, row in enumerate(reader):

            # Athletes data
            id = row[1] # change for -1 when changing csv file 
            name = row[2]
            sex = row[3]
            height = row[5]
            weight = row[6]
            team = row[7]

            # Olympic games data
            year = row[10]
            season = row[11]
            city = row[12]

            athlete = Athlete(id, name, sex, height, weight, team) # save athlete object 
            athlete.save()

            # save Olympic games object 
            try:
                obj = Olympic.objects.get(year=year, city=city) # check if olympic game already exists 
            except Olympic.DoesNotExist:
                obj = Olympic(olympic_id, year, season, city) # create olympic object and increment Id, change for slug later
                print(olympic_id)
                olympic_id += 1
                print(olympic_id)
                obj.save()


    csv_file.close()
    fs.delete(tmp_file) # delete csv file after importing data 
    return Response(status=status.HTTP_200_OK, 
                data={
                    'message': 'Success', 
                    }) 
            