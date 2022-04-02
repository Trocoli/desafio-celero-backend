import csv
import pandas as pd 
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

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
    next(reader)
    for id_, row in enumerate(reader):
            id = row[1]
            name = row[2]
            sex = row[3]
            height = row[5]
            weight = row[6]
            team = row[7]
            print(id, name, sex, height, weight, team )
    return Response(status=status.HTTP_200_OK, 
      data={
        'message': 'Success', 
      }  
    ) 