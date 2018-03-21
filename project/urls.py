from django.conf.urls import include, url

urlpatterns = [
    url(r'^calculator/', include('calculator.urls')),
    # url(r'^E/', include('calculator.urls')),

]
