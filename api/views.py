from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Zones, Plantes, Diagnostics, Recommandations
from .serializers import UsersSerializer, ZonesSerializer, PlantesSerializer, DiagnosticsSerializer, RecommandationsSerializer

# Users
class UsersList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Zones
class ZonesList(APIView):
    def get(self, request):
        zones = Zones.objects.all()
        serializer = ZonesSerializer(zones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ZonesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Plantes
class PlantesList(APIView):
    def get(self, request):
        plantes = Plantes.objects.all()
        serializer = PlantesSerializer(plantes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Diagnostics
class DiagnosticsList(APIView):
    def get(self, request):
        diagnostics = Diagnostics.objects.all()
        serializer = DiagnosticsSerializer(diagnostics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiagnosticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Recommandations
class RecommandationsList(APIView):
    def get(self, request):
        recommandations = Recommandations.objects.all()
        serializer = RecommandationsSerializer(recommandations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommandationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


