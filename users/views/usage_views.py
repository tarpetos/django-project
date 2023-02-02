from django.shortcuts import render
from django.http import HttpResponse
from django import template

register = template.Library()


def usage_table(request):
    users_statistics = (
        {
            'id': 1,
            'username': 'Taras Hevlich',
        },

        {
            'id': 2,
            'username': 'Polak Clever',
        },

        {
            'id': 3,
            'username': 'Mateusz Kieliszkowski',
        },
    )

    return render(request, 'users/generator_usage.html', {'users_statistics': users_statistics})
