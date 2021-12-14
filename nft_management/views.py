from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Nft
from .serializers import NFTSerializer


class NFTView(APIView):

    def get(self, request, pk):
        try:
            nft_object = Nft.objects.get(pk=pk)
            serializer = NFTSerializer(nft_object)
            return Response(serializer.data)
        except Nft.DoesNotExist:
            raise ValidationError("Nft does not exist")

    @swagger_auto_schema(
        request_body=NFTSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def put(self, request, pk):
        try:
            nft_object = Nft.objects.get(pk=pk)
            serializer = NFTSerializer(nft_object)
            return Response(serializer.data)
        except Nft.DoesNotExist:
            raise ValidationError("Nft does not exist")

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def delete(self, request, pk):
        try:
            nft = self.get_object(pk)
            nft.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Nft.DoesNotExist:
            raise ValidationError("Nft does not exist")

    def get_object(self, pk):
        try:
            return Nft.objects.get(pk=pk)
        except Nft.DoesNotExist:
            raise Http404


class NFTListView(APIView):

    @swagger_auto_schema(
        request_body=NFTSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        serializer = NFTSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def get(self, request, format=None):
        nft = Nft.objects.all()
        serializer = NFTSerializer(nft, many=True)
        return Response(serializer.data)
