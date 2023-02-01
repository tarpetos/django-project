from django.shortcuts import render
from django.http import HttpResponse


# Views for users
def users_list(request):
    return render(request, 'users/users_list.html', {})


def users_add(request):
    return HttpResponse('<h1>User Add Form</h1>')


def users_edit(request, uid):
    return HttpResponse('<h1>Edit User %s</h1>' % uid)


def users_usage(request, uid):
    return HttpResponse('<h1>Usage For User %s</h1>' % uid)


def users_delete(request, uid):
    return HttpResponse('<h1>Delete User %s</h1>' % uid)


# View for usage
def usage_table(request):
    return HttpResponse('<h1>Usage Table</h1>')


# Views for countries
def countries_list(request):
    return HttpResponse('<h1>Countries Listing</h1>')


def countries_add(requests):
    return HttpResponse('<h1>Country Add Form</h1>')


def countries_edit(requests, cid):
    return HttpResponse('<h1>Edit Country %s</h1>' % cid)


def countries_usage(request, cid):
    return HttpResponse('<h1>Usage For User %s</h1>' % cid)


def countries_delete(requests, cid):
    return HttpResponse('<h1>Country Add Form %s</h1>' % cid)
