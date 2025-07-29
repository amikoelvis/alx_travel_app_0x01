from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit Listings.
    Provides GET, POST, PUT, DELETE automatically.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit Bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
