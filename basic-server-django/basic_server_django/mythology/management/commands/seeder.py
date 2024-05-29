from django.core.management.base import BaseCommand, CommandError
import json


class Command(BaseCommand):
    help = "Seed database with data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write("Seeding mythology app...")
        house = json.load(open("mythology/mock/house.json"))
        being_type = json.load(open("mythology/mock/being_type.json"))
        being = json.load(open("mythology/mock/being.json"))
        story = json.load(open("mythology/mock/story.json", encoding="utf-8"))
        try:
            from mythology.models import House, BeingType, Being, Story

            for house_data in house:
                house = House.objects.create(**house_data)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created house {house.name}")
                )
            for being_type_data in being_type:
                being_type = BeingType.objects.create(**being_type_data)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully created being_type {being_type.name}"
                    )
                )
            for story_data in story:
                story = Story.objects.create(**story_data)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created story {story.title}")
                )
            for being_data in being:
                being = Being.objects.create(**being_data)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created being {being.name}")
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
        self.stdout.write(self.style.SUCCESS("Successfully seeded mythology app"))
