from rest_framework import generics,filters,status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from api.serializers.album_serializers import *
from api.serializers.query_param_serializers import *
from music.models import Album
import random



class AlbumDetailView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer


class AlbumShuffleView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    def list(self, request, *args, **kwargs):
        querylist = list(self.get_queryset())
        random.shuffle(querylist)
        sizeSerializer = SizeSerializer(data = request.query_params)
        if sizeSerializer.is_valid():
            size = sizeSerializer.validated_data.get('size')
            shuffledAlbumList = querylist[:size]
            serializedData = self.get_serializer(shuffledAlbumList,many = True)
            return Response(data=serializedData.data,status=status.HTTP_200_OK)
        else:
            return Response(data=sizeSerializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AlbumSearchView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    

# This is only for Admin use
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]


class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumListCreateSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    