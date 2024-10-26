from django.shortcuts import render
from book.models import AuthorModel
from rest_framework.response import Response

def author_list_create():
    if reuqest.method == 'GET':
        authors = AuthorModel.objects.all()
        data = AuthorSerializer(authors, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = reuqest.body
        AuthorModel.objects.create(**json, loads(data))
        return JsonREsponse

