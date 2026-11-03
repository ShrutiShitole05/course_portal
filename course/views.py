from django.shortcuts import render
from .mock_data import COURSES


def course_list_view(request):
    query = request.GET.get('search', '')
    course_dict = dict()

    if query:
        for code,course in COURSES.items():
            if query.lower() in course['meta']['title'].lower():
                course_dict[code] = course
    else:
        course_dict = COURSES

    context = {
        'courses' : course_dict,
    }
    
    return render(request, 'course-list.html', context)


def course_details_view(request, course_code):
    course_dict = None

    for code, course in COURSES.items():
        if code == course_code:
            course_dict = course
            break
        
    context = {
        'course' : course_dict
    }

    return render(request, 'course-details.html', context)
    
