from django.urls import path, re_path, register_converter

from . import views, converters

# registering custom converter as second param giving name we will use in path()
register_converter(converters.FourDigitYearConverter, 'yyyy')


app_name = 'url_test'
urlpatterns = [
    # takes zero and any positive integer
    path('int/<int:numb>/', views.tests, name='int'),
    # matches any non-empty string, except '/'
    path('str/<str:string>/', views.tests, name='str'),
    # matches any non-empty string including '/'
    path('path/<path:path>/', views.tests, name='path'),
    # matches a UUID(dashes must be included and letters must be lowercase)
    path('uuid/<uuid:id>/', views.tests, name='uuid'),
    # matches any slug string consisting of ASCII
    path('slug/<slug:slug>/', views.tests, name='slug'),

    # custom converter
    path('converter/<yyyy:year_1>', views.tests, name='converter'),

    # regular expressions
    re_path(r'^reg_exp/(?P<year_2>[0-9]{4})/$', views.tests, name='reg_exp'),

    # nested argument
    re_path(r'^nested/(?:page-(?P<nested_numb>\d+)/)?$', views.tests, name='nested'),
]
