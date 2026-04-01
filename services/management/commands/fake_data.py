import random
from django.core.management.base import BaseCommand
from faker import Faker
from services.models import Category, Service
from clients.models import Client

class Command(BaseCommand):
    help = 'Seeds initial data for Judicia Luxe'

    def handle(self, *args, **kwargs):
        fake = Faker(['fr_FR'])
        
        # Categories
        cat_names = [
            "Droit des Affaires", 
            "Patrimoine & Fortune", 
            "Immobilier de Prestige", 
            "Numérique & Innovation",
            "Pénal International"
        ]
        
        categories = []
        for name in cat_names:
            cat, created = Category.objects.get_or_create(name=name, description=fake.paragraph())
            categories.append(cat)
            self.stdout.write(self.style.SUCCESS(f'Catégorie crée: {name}'))

        # Services
        services_data = [
            ("Fusions et Acquisitions", categories[0], 2500),
            ("Gouvernance d'Entreprise", categories[0], 1800),
            ("Structuration de Fonds de Dotation", categories[1], 5000),
            ("Planification Successorale Complexe", categories[1], 4200),
            ("Acquisition de Propriétés d'Exception", categories[2], 12000),
            ("Contentieux de la Construction Haut de Gamme", categories[2], 3500),
            ("Protection de Brevets Stratégiques", categories[3], 4500),
            ("Litiges en Cybercriminalité", categories[3], 5500),
            ("Défense devant la Cour Pénale Internationale", categories[4], 15000),
            ("Criminalité en Col Blanc d'Envergure", categories[4], 8000),
        ]

        for name, category, price in services_data:
            Service.objects.get_or_create(
                name=name,
                category=category,
                price=price,
                description=fake.paragraph(nb_sentences=3)
            )
            self.stdout.write(self.style.SUCCESS(f'Service crée: {name}'))

        # Clients
        for _ in range(12):
            Client.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address().replace('\n', ', ')
            )
        self.stdout.write(self.style.SUCCESS('12 Clients crées avec succès!'))
