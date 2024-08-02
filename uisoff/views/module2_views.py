from django.shortcuts import render, redirect, get_object_or_404
from table.models import lesson
from blogs.models import news
from school.models import infoschool


def tablesite(request):
    new = news.objects.all().order_by('-created_at')[:5]
    schools = infoschool.objects.values_list('title', flat=True)
    schools_top = infoschool.objects.values_list('title', flat=True).order_by()[:4]
    selected_school = request.GET.get('table')
    print(selected_school)
    if selected_school:
        table = lesson.objects.filter(wschool__title__icontains=selected_school).order_by('-created_at')
    else:
        table = lesson.objects.all().order_by('-created_at').order_by()[:11]
    context = {
        'table': table,
        'schools': schools,
        'selected_school': selected_school,
        'schools_top': schools_top,
        'new':new
    }
    return render(request, 'centui/pages/table.html', context)