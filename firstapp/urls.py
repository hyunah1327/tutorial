from django.urls import path
from . import views

urlpatterns = [
    path('template/', views.template),
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post),
    
    #ajax를 동작시키기 위한 프런트 페이지 보여주기
    path('req/ajax4/', views.req_ajax4),
    path('static/', views.static),
    path('tag/', views.tag),
    path('var/', views.var),
    path('filter/', views.filter),
    path('form/model/', views.form_model),
]