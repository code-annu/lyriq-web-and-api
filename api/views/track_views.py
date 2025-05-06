from rest_framework import generics, permissions, filters
from api.serializers.track_serializers import *
from api.serializers.query_param_serializers import *
from rest_framework import status
from rest_framework.response import Response
from music.models import Track
import random


class TrackDetailView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrackShuffleView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        querylist = list(self.get_queryset())
        random.shuffle(querylist)
        sizeSerializer = SizeSerializer(data = request.query_params)
        if sizeSerializer.is_valid():
            size = sizeSerializer.validated_data.get('size')
            shuffledTrackList = querylist[:size]
            serializedData = self.get_serializer(shuffledTrackList,many=True)
            return Response(data=serializedData.data,status=status.HTTP_200_OK)
        else:
            return Response(data=sizeSerializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TrackSearchView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]


# These classes are only for admin uses

class TrackListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve and create tracks.
    """
    queryset = Track.objects.all()
    serializer_class = TrackListCreateSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    
class TrackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a track.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

   