from django.http import HttpResponse
from django.shortcuts import render
from users.models.countries import Country


def countries_list(request):
    countries = (
        {
            'id': 1,
            'country_name': 'Ukraine',
            'unique_users': 1,
        },

        {
            'id': 2,
            'country_name': 'Poland',
            'unique_users': 2,
        }
    )

    return render(request, 'users/countries.html', {'countries': countries})


def countries_add(requests):
    return HttpResponse('<h1>Country Add Form</h1>')


def countries_edit(requests, cid):
    return HttpResponse('<h1>Edit Country %s</h1>' % cid)


def countries_usage(request, cid):
    return HttpResponse('<h1>Usage For User %s</h1>' % cid)


def countries_delete(requests, cid):
    return HttpResponse('<h1>Delete Country %s</h1>' % cid)
