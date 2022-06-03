from django.shortcuts import render
from django.http import HttpResponse


def tests(request, numb=None, string=None, path=None, id=None, slug=None, year_1=None, year_2=None, nested_numb=None):
    if numb:
        return HttpResponse(f'It is integer: {numb}')
    if string:
        return HttpResponse(f'It is string: {string}')
    if path:
        return HttpResponse(f'It is path: {path}')
    if id:
        return HttpResponse(f'It is UUID: {id}')
    if slug:
        return HttpResponse(f'It is slug: {slug}')
    if year_1:
        return HttpResponse(f'It is custom converter: {year_1}')
    if year_2:
        return HttpResponse(f'It is regular expression: {year_2}')
    if nested_numb:
        return HttpResponse(f'It url have nested arguments: {nested_numb}')
