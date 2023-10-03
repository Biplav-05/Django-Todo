from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='IndexView'),
    path('save/',views.save_data,name='save'),
    path('complete/<todo_id>',views.makeComplete,name='makecomplete'),
    path('pending/<todo_id>',views.makePending,name='makepending'),
    path('deletecompleted',views.deleteCompleted,name='deletecompleted'),
    path('deleteall',views.deleteAll,name='deleteall'),
]
