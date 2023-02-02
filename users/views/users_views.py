from django.shortcuts import render
from django.http import HttpResponse


def users_list(request):
    users = (
        {
            'id': 1,
            'first_name': 'Taras',
            'last_name': 'Hevlich',
            'telegram_id': 441547155,
            'image': '/img/taras_hevlich.png'
        },

        {
            'id': 2,
            'first_name': 'Polak',
            'last_name': 'Clever',
            'telegram_id': 321453123,
            'image': '/img/default.png'
        },

        {
            'id': 3,
            'first_name': 'Mateusz',
            'last_name': 'Kieliszkowski',
            'telegram_id': 435123555,
            'image': '/img/mateusz_kieliszkowski.png'
        },
    )

    return render(request, 'users/users_list.html', {'users': users})


def users_add(request):
    return render(request, 'users/edit_user.html', {})


def users_edit(request, uid):
    return render(request, 'users/edit_user.html', {})


def users_usage(request, uid):
    return HttpResponse('<h1>Usage For User %s</h1>' % uid)


def users_delete(request, uid):
    return HttpResponse('<h1>Delete User %s</h1>' % uid)
