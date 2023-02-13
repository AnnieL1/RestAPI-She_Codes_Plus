from rest_framework import serializers
from .models import Project, Pledge, StretchGoals

class StretchGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StretchGoals
        # fields = ["parent", "pledger", "player", "sg_description", "trigger"]
        # read_only_fields =["parent", "pledger", "player"] 
        fields = ['id', 'project', 'gamer', 'sg_description', 'trigger']
        read_only_fields = ['id', 'gamer']

    # id = serializers.ReadOnlyField()
    # project = serializers.ReadOnlyField()
    # user = serializers.ReadOnlyField()
    # sg_description = serializers.CharField ()
    # trigger = serializers.IntegerField()

    def create(self, validated_data):
        return StretchGoals.objects.create(**validated_data)
    

class StretchGoalsDetailSerializer(StretchGoalsSerializer):
    def update(self, instance,validated_data):
        instance.project = validated_data.get('project', instance.project)
        instance.gamer = validated_data.get('gamer', instance.gamer)
        instance.sg_description = validated_data.get('sg_description', instance.sg_description)
        instance.trigger = validated_data.get('trigger', instance.trigger)
        instance.save
        return instance


class PledgeSerializer(serializers.ModelSerializer):  #modelSerializer is programmed to look at the fields in the model and match up what it has been asked to serialise from models.py   
#if change to 'Meta' you also have to change, you also have to change views.py
    class Meta:
        model = Pledge
        # fields = ['id', 'amount', 'comment', 'anonymous', 'is_active', 'project', 'supporter']
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']
    # id = serializers.ReadOnlyField()
    # amount = serializers.IntegerField()
    # comment = serializers.CharField(max_length=200)
    # anonymous = serializers.BooleanField() #anon is in backend because when BE receives a list of pledges it's just going to contain a list of data from the database. Need to tell it to be anon so it doesn't display everyone's data or data a pledger doesn't want FE to show 
    # supporter = serializers.CharField(max_length=200)
    # project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

### insert something here for delete ??? 

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    is_active=serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    #can add another field in model, serializer to make non-active instead of 'delete'. If wnat to maek it visible again, use a PUT request 

    def create(self, validated_data):
        return Project.objects.create(**validated_data) # ** is an unpacking syntax ie. if you recieve a dictionary, unpack the dictionary and hand each key value pair over as a key arguement

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data): 
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        # instance.is_active=validated_data.get('is_active', instance.is_active)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance 


class PledgeDetailSerializer(PledgeSerializer):  #modelSerializer is programmed to look at the fields in the model and match up what it has been asked to serialise from models.py   
    # projects = ProjectSerializer (many = False, read_only=True)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        # instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance

# ## attempting to use mixin-destroy class to delete a record in database
# class DeletePledgeSerializer(serializers.ModelSerializer):  

#     class Meta:
#         model = Pledge
#         fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']

#     def perform_destroy(self, validated_data):
#         return Pledge.objects.delete(**validated_data)

