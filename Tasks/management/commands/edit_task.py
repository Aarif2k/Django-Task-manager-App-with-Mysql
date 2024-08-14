from django.core.management.base import BaseCommand, CommandError
from Tasks.models import Task

class Command(BaseCommand):
    help = 'Edit an existing task'

    def add_arguments(self, parser):
        parser.add_argument('task_id', type=int, help='The ID of the task to edit')

    def handle(self, *args, **kwargs):
        task_id = kwargs['task_id']

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise CommandError('Task not found')

        title = input(f"Enter new title (current: {task.title}): ") or task.title
        description = input(f"Enter new description (current: {task.description}): ") or task.description
        priority = input(f"Enter new priority (High/Medium/Low) (current: {task.priority}): ") or task.priority
        status = input(f"Enter new status (Pending/In Progress/Completed) (current: {task.status}): ") or task.status

        task.title = title
        task.description = description
        task.priority = priority
        task.status = status
        task.save()

        self.stdout.write(self.style.SUCCESS(f'Task "{task.title}" updated successfully.'))
