from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:project_pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pledge_pk>/', views.PledgeDetail.as_view()), #all pledges for a particular project can be found in Project Details
    path('stretch_goals/', views.StretchGoalsList.as_view()),
    path('stretch_goals/<int:sg_pk>', views.StretchGoalsDetail.as_view()) #all stretch goals for a particular project
]

urlpatterns = format_suffix_patterns(urlpatterns)