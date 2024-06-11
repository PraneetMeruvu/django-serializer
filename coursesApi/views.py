# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from bs4 import BeautifulSoup
import requests
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

@api_view(['GET']) 
def CourseListView(request):
        if request.method == 'GET':
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return JsonResponse(serializer.data, safe=False)

        

@api_view(['GET', 'PUT', 'DELETE'])
def CourseDetailView(request, course_program, course_code):
    try:
        courses = Course.objects.get(course_program=course_program, course_code=course_code)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(courses)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(courses, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        courses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def CourseByElectiveView(request):
    elective_value = request.GET.get('elective', '').lower()
    if elective_value not in ['true', 'false', 'yes', 'no']:
        return Response({'error': 'Invalid elective value'}, status=status.HTTP_400_BAD_REQUEST)

    is_elective = elective_value in ['true', 'yes']
    courses = Course.objects.filter(elective=is_elective)
    serializer = CourseSerializer(courses, many=True)
    return Response({'courses': serializer.data})

        
@api_view(['POST'])
def LoadCoursesView(request):
    try:
        # Fetching data from the website
        url = 'https://sysrev.cs.binghamton.edu/'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            courses_data = []

            # Extracting mandatory courses from the HTML structure
            mandatory_courses_list = soup.find('ul', id='mandatory-courses')
            if mandatory_courses_list:
                for course_element in mandatory_courses_list.find_all('li'):
                    course_data = extract_course_data(course_element.text.strip())
                    courses_data.append(course_data)

            # Extracting elective courses from the HTML structure
            elective_courses_list = soup.find('ul', id='elective-courses')
            if elective_courses_list:
                for course_element in elective_courses_list.find_all('li'):
                    course_data = extract_course_data(course_element.text.strip(), elective=True)
                    courses_data.append(course_data)

            # Populating courses in the database
            for course_data in courses_data:
                Course.objects.get_or_create(**course_data)

            return Response({"message": "Courses loaded successfully."}, status=status.HTTP_201_CREATED)

        else:
            return Response({"error": "Failed to fetch data from the website"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def extract_course_data(course_info, elective=False): 
    parts = course_info.split(' ', 1)
    course_program = parts[0]

    # Extract course_code and course_name
    course_code, course_name = parts[1].split(' ', 1)

    return {
        'course_program': course_program,
        'course_code': course_code,
        'course_name': course_name.strip(),
        'elective': elective,
    }

        