from django.db import models
# from django import forms    
from django.contrib.auth import get_user_model

User = get_user_model() 

# Create your models here.
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    # is_active=models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,  #if you delete project, automatically delete all the pledges associated with the project so there are no floating pledges in the database 
        ## there's also on_update.CASCADE - this let's the pledges ID change if the project ID changes. ID shouldn't be sequential because hackers will be able to scrap people's data based on order of user's ID
        related_name='pledges', #tells Project to look for the Pledges model because it needs all the data from a certain row within Pledges database
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    # total_pledged = models.IntegerField()

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()  #hard to store in database because there's a lot of 0s and 1s, hence we're using a URL to redirect to image
    is_open = models.BooleanField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True) #auto_now_add tells the backend to just auto record whatever time the command was run, rather than having to GET the time from the db and then POST the same time back to the DB
    ## owner=models.CharField(max_length=200) #need to change to Primary or Foriegn Key in future so the tables can talk to each other. The CharField class won't allow tables to talk to each other 
    owner = models.ForeignKey(
        User,   # we're saying there is a relo between users and projects
        on_delete=models.CASCADE,  # when user is deleted, delete all their projects as well so user PK always has projects to correspond to
        related_name='owner_projects'   # eg. ask computer to look for user1 projects and then all the projects will be shown 
    )
    

    # total_pledged = models.ForeignKey(
    #     Pledge.objects.aggregate(Sum('amount')),
    #     on_delete=models.CASCADE,
    #     related_name = 'total'
    # )



class StretchGoals(models.Model):
    sg_description = models.TextField()
    trigger = models.IntegerField()
    # total_pledged = models.IntegerField()
    pledge = models.ForeignKey(
        'Pledge',
        on_delete=models.CASCADE,
        related_name = 'stretch_goals'
    )

    gamer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='player_stretch_goals'
    )
    
   