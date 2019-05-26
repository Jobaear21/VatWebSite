from django.urls import path
from .views import homePageView,aboutPageView,servicePageView,trainingPageView,blogPageView,contactPageView,infoPageView,rulesPageView,completePageView
urlpatterns=[
	path('home',homePageView,name='home'),
	path('about',aboutPageView,name='about'),
	path('service',servicePageView,name='service'),
	path('training',trainingPageView,name='training'),
	path('contact',contactPageView,name='contact'),
	path('contact_complete',completePageView,name='contact_complete'),
	path('info',infoPageView,name='info'),
	path('rules',rulesPageView,name='rules'),
	path('law',lawPageView,name='law'),
]