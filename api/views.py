# from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from api.models import User,Group
from api.serializers import GroupSerializer, UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a user instance
        
        list:
            Return all users,ordered by most recent joined
        
        create:
            Create a new user
        
        delete:
            Remove a existing user
        
        partial_update:
            Update one or more  feilds in a existing user
        
        update:
            update a user
    """
    queryset = User.objects.all()
    serializer_class=UserSerializer
class GroupviewSet(viewsets.ModelViewSet):
    """
           retrieve:
               Return a group instance

           list:
               Return all groups,ordered by most recent joined

           create:
               Create a new group

           delete:
               Remove a existing group

           partial_update:
               Update one or more  feilds in a existing group

           update:
               update a group
       """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
