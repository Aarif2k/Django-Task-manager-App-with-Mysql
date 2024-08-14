from django.core.management.base import BaseCommand
from Tasks.models import Task

class Command(BaseCommand):
    help = 'Filter tasks by priority'

    def add_arguments(self, parser):
        parser.add_argument('priority', type=str, help='The priority to filter by (High/Medium/Low)')

    def handle(self, *args, **kwargs):
        priority = kwargs['priority'].title()

        tasks = Task.objects.filter(priority=priority)
        if tasks:
            for task in tasks:
                self.stdout.write(f"{task}")
        else:
            self.stdout.write(f'No tasks found with priority {priority}.')
