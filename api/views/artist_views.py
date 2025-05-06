import random
from rest_framework import generics,status,filters
from music.models import Artist
from api.serializers.artist_serializers import *
from music.models import Artist
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from api.serializers.query_param_serializers import SizeSerializer
from rest_framework.response import Response


class ArtistDetailView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
    
    

class ArtistAlbumsView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistAlbumsSerializer
    

class ArtistSearchView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    
class ArtistShuffleView(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        querylist = list(queryset)
        random.shuffle(querylist)
        return querylist
        
    
    def list(self, request, *args, **kwargs):
        sizeSerializer = SizeSerializer(data = request.query_params)
        if sizeSerializer.is_valid():
            size  = sizeSerializer.validated_data.get('size')
            queryset = self.get_queryset()[:size]
            serializer = self.get_serializer(queryset,many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset,many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
    


# These classes are only use for Admin

class ArtistListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve and create artists.
    """
    permission_classes = [IsAdminUser]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
    
class ArtistRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete an artist.
    """
    permission_classes = [IsAdminUser]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer