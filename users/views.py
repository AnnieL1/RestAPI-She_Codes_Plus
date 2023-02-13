from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from .serializer import CustomUserSerializer, CustomUserDetailSerializer

class CustomUserList(APIView):
    ## attempting class Meta
    # queryset = CustomUser.objects.all()
    # serializer_class = CustomUserSerializer

    # def perform_create(self, serializer):
    #     serializer.save(username=self.request.user)
    
    # blocked out code below to try out class Meta
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):
    def get_object(self, pk): #pk is given in the FE from the user's URL
        try:
            return CustomUser.objects.get(pk=pk, is_active =True)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    # attempting to add PUT for user detail
    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance = user,
            data = data,
            partial = True 
        )

        if pk == request.user.id & serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response({"result":"user not authorised"})
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        if pk == request.user.id:
            user.delete()
            return Response({"result":"user delete"})
        return Response({"result":"user not authorised"})


# attempting to add DELETE for user detail
# class CustomUserDelete(APIView):
#     def get_object(self, pk): #pk is given in the FE from the user's URL
#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             raise Http404

#     def delete(self, request, *args, **kwargs):
#         user=self.request.user
#         user.delete()

#         return Response({"result":"user delete"})
