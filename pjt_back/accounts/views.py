from .models import User
from .serializers import UserListSerializer, UserSerializer, UserUpdateSerializer, UserUpdateSkillSerializer, UserUpdateLanguageSerializer, UserUpdateEtcSerializer
from objects.models import Campus

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def peoples(request):
    campus  = request.GET.get('campus')
    part    = request.GET.get('part')
    skills  = request.GET.get('skills')
    count   = request.GET.get('count')
    peoples = User.objects.filter(is_staff=False)
    
    if campus:
        campus = int(campus)
        nationwide = Campus.objects.get(title='전국').id
        if campus != nationwide:
            peoples = peoples.filter(campus=campus)

    if part:
        part = int(part)
        peoples = peoples.filter(part=part)

    if skills:
        skills = list(map(int, skills.split(','))) 
        temp_peoples = []
        for skill in skills:
            for people in peoples:
                if people.skill.all().filter(id=skill):
                    temp_peoples.append(people)
        peoples = temp_peoples

    filter_count = 20
    count = int(count)
    peoples = peoples[(count-1)*filter_count:count*filter_count]
    serializer = UserListSerializer(peoples, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def people_detail(request, username):
    user = request.user
    if request.method == 'GET':
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        skill = request.data.get('skill')
        language = request.data.get('language')

        if not skill and not language:
            serializer = UserUpdateEtcSerializer(user, data=request.data)
        elif not skill:
            serializer = UserUpdateLanguageSerializer(user, data=request.data)
        elif not language:
            serializer = UserUpdateSkillSerializer(user, data=request.data)
        else:
            serializer = UserUpdateSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
