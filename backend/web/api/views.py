from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Administrator, Moderator
from .serializers import AdministratorSerializer, AdministratorSerializerCreate, ModeratorSerializer, ModeratorSerializerCreate
from utils import constants
from utils.permissions import is_administrator
# Create your views here.
# administrators
class AdministratorView(APIView):

    @staticmethod
    def get(request):
        """
        List administrators
        """

        administrators = Administrator.objects.all()
        return Response(AdministratorSerializer(administrators, many=True).data)

    @staticmethod
    def post(request):
        """
        Create administrator
        Remove user as moderator if appointed
        """

        serializer = AdministratorSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            administrator = serializer.save()
            Moderator.objects.filter(user=administrator.user).delete()
            return Response(AdministratorSerializer(administrator).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# moderators
class ModeratorView(APIView):

    @staticmethod
    def get(request):
        """
        List moderators
        """

        moderators = Moderator.objects.all()
        return Response(ModeratorSerializer(moderators, many=True).data)

    @staticmethod
    def post(request):
        """
        Create moderator
        """

        serializer = ModeratorSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(ModeratorSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# moderators/{moderator_id}
class ModeratorDetail(APIView):

    @staticmethod
    def delete(request, moderator_id):
        """
        Delete moderator
        """

        moderator = get_object_or_404(Moderator, pk=moderator_id)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_403_FORBIDDEN)
        moderator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
