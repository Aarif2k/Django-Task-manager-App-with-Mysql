from django.core.management.base import BaseCommand
from Tasks.models import Task

class Command(BaseCommand):
    help = 'Add a new task'

    def handle(self, *args, **kwargs):
        title = input("Enter title: ")
        description = input("Enter description: ")
        priority = input("Enter priority (High/Medium/Low): ")
        status = input("Enter status (Pending/In Progress/Completed): ")

        task = Task.objects.create(title=title, description=description, priority=priority, status=status)
        self.stdout.write(self.style.SUCCESS(f'Task "{task.title}" added successfully.'))
