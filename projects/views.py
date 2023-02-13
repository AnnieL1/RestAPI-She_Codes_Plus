from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.mixins import DestroyModelMixin
from .models import Project, Pledge, StretchGoals
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer, PledgeDetailSerializer, StretchGoalsSerializer, StretchGoalsDetailSerializer
from django.http import Http404
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class ProjectList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        # a. Use the line below if not filtering out inactive projects
        projects = Project.objects.all()

        ## b. Use the line below when filtering for only active projects
        # projects = Project.objects.filter(is_active=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(   #better to put a catch all return after the if statement, rather than using a else statement, just in case if statement is really long and complicated. Don't want to make it hard to read because people will miss it.
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly        
    ]

    def get_object(self, project_pk):
        try: 
            #tells python what to do and will show the return statement if it works
            # canceling out to try is_active field. ####project = Project.objects.get(pk=pk)
            # use the following field for the 'is_active' field 
            project = Project.objects.get(pk=project_pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist: #native python language that gets released into the interpreter when something goes wrong
            raise Http404

    def get(self, request, project_pk):
        project = self.get_object(project_pk)
        serializer = ProjectDetailSerializer(project)  # Use ProjectDetailSerializer instead of ProjectSerializer so that the pledges show!
        return Response(serializer.data)

    def put(self, request, project_pk):
        project = self.get_object(project_pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance = project,
            data = data,
            partial = True 
        )
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)

    def delete(self, request, project_pk):
        project = self.get_object(project_pk)
        if project.owner == request.user:
            project.delete()
            return Response({"result":"project deleted"})
        return Response({"result":"project not authorised to be deleted"})


class PledgeList(generics.ListCreateAPIView):  #see Meta from serializer.py

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly       
    ]

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer): #make one comment per user here
        serializer.save(supporter=self.request.user)
    
    # def perform_destroy(self, serializer):
        #serializer.delete(supporter=self.request.user)
        
    ## all the code below this line and blocked out gets deleted because we have used the Meta method in serialize.py
    # def get(self, request):
    #     pledges = Pledge.objects.all()
    #     serializer = PledgeSerializer(pledges, many=True)
    #     return Response(serializer.data)

    # def post(self, request):  #make one comment per user here
    #     serializer = PledgeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_201_CREATED
    #         )
    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )

class PledgeDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,     
    ]     

    def get_object(self, pledge_pk):
        try: #tells python what to do and will show the return statement if it works
            pledge = Pledge.objects.get(pk=pledge_pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist: #native python language that gets released into the interpreter when something goes wrong
            raise Http404

    def get(self, request, pledge_pk):
        pledge = self.get_object(pledge_pk)
        serializer = PledgeDetailSerializer(pledge)  
        return Response(serializer.data)

    def put(self, request, pledge_pk):
        pledge = self.get_object(pledge_pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance = pledge,
            data = data,
            partial = True 
        )
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)

    def delete(self, request, pledge_pk):
        pledge = self.get_object(pledge_pk)
        if pledge.supporter == request.user:
            pledge.delete()
            return Response({"result":"pledge deleted"})
        return Response({"result":"pledge not authorised to be deleted"})


## attempting to use mixin-destroy class to delete a record in database

# class DeletePledge(DestroyModelMixin, APIView):
#     """
#     Destroy a model instance.
#     """
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     ]

#     def get_object(self, pk):
#         try: #tells python what to do and will show the return statement if it works
#             pledge = Pledge.objects.get(pk=pk)
#             self.check_object_permissions(self.request, pledge)
#             return pledge
#         except Pledge.DoesNotExist: #native python language that gets released into the interpreter when something goes wrong
#             raise Http404

#     def destroy(self, request, pk):
#         pledge = self.get_object()
#         if pledge.supporter == request.user:
#             self.perform_destroy(pledge)
#             return Response({"result":"pledge deleted"})
#         return Response({"result":"pledge not authorised to be deleted"})

class StretchGoalsList(generics.ListCreateAPIView):

    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly       
    # ]

    def get(self, request):
        # a. Use the line below if not filtering out inactive projects
        stretchgoals = StretchGoals.objects.all()

        ## b. Use the line below when filtering for only active projects
        # projects = Project.objects.filter(is_active=True)
        serializer = StretchGoalsSerializer(stretchgoals, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StretchGoalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(gamer = request.user)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(   #better to put a catch all return after the if statement, rather than using a else statement, just in case if statement is really long and complicated. Don't want to make it hard to read because people will miss it.
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class StretchGoalsDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,     
    ]  

    def get_object(self, sg_pk):
        try: #tells python what to do and will show the return statement if it works
            stretchgoals = StretchGoals.objects.get(pk=sg_pk)
            self.check_object_permissions(self.request, stretchgoals)
            return stretchgoals
        except stretchgoals.DoesNotExist: #native python language that gets released into the interpreter when something goes wrong
            raise Http404


    def get(self, request, sg_pk):
        stretchgoals = self.get_object(sg_pk)
        serializer = StretchGoalsDetailSerializer(stretchgoals)  
        if serializer.is_valid():
            return Response(serializer.data)
        return Response({"stretch goal does not exist"})

    def put(self, request, sg_pk):
        stretchgoals = self.get_object(sg_pk)
        data = request.data
        serializer = StretchGoalsDetailSerializer(
            instance = stretchgoals,
            data = data,
            partial = True 
        )
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)

    def delete(self, request, sg_pk):
        stretchgoals = self.get_object(sg_pk)
        if stretchgoals.gamer == request.user:
            stretchgoals.delete()
            return Response({"result":"stretch goal deleted"})
        return Response({"result":"stretch goals not authorised to be deleted"})