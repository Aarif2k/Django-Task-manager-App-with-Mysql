from django.core.management.base import BaseCommand, CommandError
from Tasks.models import Task

class Command(BaseCommand):
    help = 'Delete a task'

    def add_arguments(self, parser):
        parser.add_argument('task_id', type=int, help='The ID of the task to delete')

    def handle(self, *args, **kwargs):
        task_id = kwargs['task_id']

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise CommandError('Task not found')

        task.delete()
        self.stdout.write(self.style.SUCCESS(f'Task "{task.title}" deleted successfully.'))
