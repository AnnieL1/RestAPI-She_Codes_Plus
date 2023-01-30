from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'comments', StretchGoalsDetail, basename='comment')

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:project_pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pledge_pk>/', views.PledgeDetail.as_view()), #all pledges for a particular project can be found in Project Details
    path('stretch_goals/', views.StretchGoalsList.as_view()),
    path('stretch_goals/<int:sg_pk>', views.StretchGoalsDetail.as_view()), #all stretch goals for a particular project
    # path('stretch_goals/<int:sg_pk>', views.StretchGoalsDetail.as_view(), include(router.urls)), #all stretch goals for a particular project
    path('total_pledges/', views.TotalPledge.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
