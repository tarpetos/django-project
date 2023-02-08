from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from users.models.users import User


def users_list(request):
    users = User.objects.all()

    users_order = request.GET.get('order_by', 'last_name')

    if users_order in ('last_name', 'first_name', 'telegram_id'):
        users = users.order_by(users_order)
        if request.GET.get('reverse', '') == '1':
            users = users.reverse()

    paginator = Paginator(users, 4)
    current_page = request.GET.get('page')

    try:
        users = paginator.page(current_page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    return render(request, 'users/users_list.html', {'users': users})


def users_add(request):
    return render(request, 'users/edit_user.html', {})


def users_edit(request, uid):
    return render(request, 'users/edit_user.html', {})


def users_usage(request, uid):
    return HttpResponse('<h1>Usage For User %s</h1>' % uid)


def users_delete(request, uid):
    return HttpResponse('<h1>Delete User %s</h1>' % uid)
