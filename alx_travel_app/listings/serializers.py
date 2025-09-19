from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = Listing
        fields = [ "id", "title", "description", "price_per_night", "location", "host", "is_active", "created_at", "updated_at",]
       

class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.StringRelatedField(read_only=True)
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())

    class Meta:
        model = Booking
        fields = ["id", "listing", "guest", "check_in", "check_out", "total_price", "created_at",]
       
