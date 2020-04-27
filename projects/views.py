from django.http import Http404
from django.shortcuts import render, redirect
from datetime import datetime
from project import settings
from .models import Publication


def publication(request, number_id):
    try:
        pubs = Publication.objects.get(id=number_id)
    except:
        raise Http404('Статьи не найдено!')

    comments_list = pubs.comment_set.order_by('-id')[:10]

    return render(request, 'publication.html', {'publication': pubs, 'comments_list': comments_list})


def contact(request):
    return render(request, 'index_test.html')


def publications(request):
    context = Publication.objects.all()
    return render(request, 'publications.html', {
        'publication': context
    })


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']

    if secret != settings.SECRET_KEY:
        return render(request, 'publish.html', {
            'error': 'ключ не верный!'
        })
    if name == '':
        return render(request, 'publish.html', {
            'error': 'пустое имя!'
        })
    if text == '':
        return render(request, 'publish.html', {
            'error': 'пустое поле текста!'
        })

    Publication(
        pub_name=name,
        pub_text=text.replace('\n', '<br />'),
        pub_date=datetime.now()
    ).save()
    return redirect('/publications')


def comments(request, number_id):
    try:
        pubs = Publication.objects.get(id=number_id)
    except:
        raise Http404('Статьи не найдено!')

    pubs.comment_set.create(author=request.POST['name'], comment_text=request.POST['text'])

    return redirect('/publications')
