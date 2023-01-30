from rest_framework import serializers 
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):  # don't put pw here cos you never want pw to be pulled out of database

    ## attempting class Meta
    # class Meta:
    #     model = CustomUser
    #     fields = ['id', 'username', 'email', 'password']

    # def create(self, validated_data):
    #     return CustomUser.objects.create(**validated_data)

    # blocked out code below to try out class Meta
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):   #this part will either accept or reject the pw. PW is sent to db as hashes and if the hashes sent matches the hatches in db then pw is correct. Hashes are used since it's hard to read and translate to normal letters do it's hard to hack.
        return CustomUser.objects.create_user(**validated_data)


# attempting to add PUT for user detail
class CustomUserDetailSerializer(CustomUserSerializer):
    
    def update(self, instance, validated_data): 
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance 


# attempting to add DELETE for user detail
# class CustomUserDeleteSerializer(CustomUserSerializer):
    
#     def update(self, instance, validated_data): 
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.delete()
#         return instance 


# class CommentSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField()
#     user = serializers.CharField(read_only = True)
#     comment = serializers.CharField() 

