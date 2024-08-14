from django.core.management.base import BaseCommand
from Tasks.models import Task

class Command(BaseCommand):
    help = 'View all tasks'

    def handle(self, *args, **kwargs):
        tasks = Task.objects.all()
        if tasks:
            for task in tasks:
                self.stdout.write(f"{task}")
        else:
            self.stdout.write('No tasks found.')
