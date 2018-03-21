from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CalculatorView().calc, name='calculator'),
    url(r'^(?P<calculator><command>[0-9]*)/$', views.CalculatorView().calc,
        name='command'),
    url(r'^(?P<calculator>[-]*[0-9]*)/$', views.CalculatorView().calc, name='result'),
    url(r'^(?P<calculator>[E]*)/$', views.CalculatorView().calc,
        name='error'),

]