from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
from decimal import Decimal
import random

User = get_user_model()

SAMPLE_LISTINGS = [
    {
        "title": "Beachfront Villa",
        "description": "A beautiful beachfront villa with ocean views.",
        "price_per_night": Decimal("150.00"),
        "location": "Mombasa, Kenya",
    },
    {
        "title": "Mountain Cabin",
        "description": "A cozy cabin in the mountains, perfect for hiking.",
        "price_per_night": Decimal("80.00"),
        "location": "Mount Kenya, Kenya",
    },
    {
        "title": "City Apartment",
        "description": "Modern apartment in the city center close to everything.",
        "price_per_night": Decimal("100.00"),
        "location": "Nairobi, Kenya",
    },
]


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Ensure there is at least one user to act as host
        host, created = User.objects.get_or_create(
            username="sample_host",
            defaults={"email": "host@example.com"}
        )
        if created:
            host.set_password("password123")
            host.save()
            self.stdout.write(self.style.SUCCESS("Created sample host user."))

        for data in SAMPLE_LISTINGS:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price_per_night": data["price_per_night"],
                    "location": data["location"],
                    "host": host,
                    "is_active": True,
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))
