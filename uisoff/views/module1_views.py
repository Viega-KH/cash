from django.shortcuts import render, redirect, get_object_or_404
from employ.models import leadership
from blogs.models import news, category
from django.core.paginator import Paginator
from table.models import lesson
from school.models import infoschool
from slevel.models import infolevel
from django.http import JsonResponse
from statest.models import statestic
from contact.models import contact
# Create your views here.
def home(request):
    new = news.objects.all().order_by('-created_at')[:3]
    newfooter = news.objects.all().order_by('-created_at')[:2]
    school = infoschool.objects.all()
    slevel = infolevel.objects.all()
    statest = statestic.objects.get()
    context = {
        'new':new,
        'newfooter':newfooter,
        'school':school,
        'slevel':slevel,
        'statest':statest
    }
    return render(request, 'centui/pages/home.html', context)


def homeselekt(request):
    if request.method == 'POST':
        school = request.POST.get('school') 
        slevel = request.POST.get('slevel') 
        
        if slevel:
            try:
                slevelget = infolevel.objects.get(id=slevel)
                response_data = {
                    'id': slevelget.id,
                    'title': slevelget.title,
                    'number_ch': slevelget.number_ch,
                    'number_ep': slevelget.number_ep,
                }
                return JsonResponse(response_data)
            except infolevel.DoesNotExist:
                return JsonResponse({'error': 'Level not found'}, status=404)

        if school:
            try:
                schoolget = infoschool.objects.get(id=school)
                response_data = {
                    'id': schoolget.id,
                    'title': schoolget.title,
                    'number_pt': schoolget.number_pt,
                    'number_s': schoolget.number_s,
                }
                return JsonResponse(response_data)
            except infoschool.DoesNotExist:
                return JsonResponse({'error': 'School not found'}, status=404)

        return JsonResponse({'error': 'No school or slevel ID provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




def about(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    school = infoschool.objects.all()
    slevel = infolevel.objects.all()
    statest = statestic.objects.get()
    context = {
        'school':school,
        'slevel':slevel,
        'statest':statest,
        'newfooter':newfooter
    }
    statest = statestic.objects.get()
    return render(request, 'centui/pages/about.html', context)


def leader(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    lists = leadership.objects.all()
    new = news.objects.all().order_by('-created_at')[:5]
    return render(request, 'centui/pages/leader.html', { 'list':lists, 'new':new, 'newfooter':newfooter })


def new(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    categorys = get_object_or_404(category, name='Yangilik')
    news_list = news.objects.filter(category=categorys).order_by('-created_at')
    paginator = Paginator(news_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'centui/pages/news.html', {'page_obj': page_obj, 'newfooter':newfooter})

def newad(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    categorys = get_object_or_404(category, name='E`lon')
    news_list = news.objects.filter(category=categorys).order_by('-created_at')
    paginator = Paginator(news_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'centui/pages/ad.html', {'page_obj': page_obj, 'newfooter':newfooter})

def newdet(request, id):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    news_list = news.objects.all().order_by('-created_at')[:5]
    new = news.objects.get(id=id)
    return render(request, 'centui/include/news.html', {'news_list':news_list, 'new':new, 'newfooter':newfooter})


def contactsite(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    if request.method == 'POST':
        full_name = request.POST.get('name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact.objects.create(
            name=full_name,
            subject=subject,
            phone=phone,
            message=message
        )
        return redirect('contactsite')
    return render(request, 'centui/pages/contact.html', { 'newfooter':newfooter })
