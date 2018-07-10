from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
	def handle(self, *args, **options):
		if not User.objects.filter(username="admin").exists():
			User.objects.create_superuser("hasime", "hardeepsinghmehradoodle@gmail.com", "Precio@108")
			User.objects.create_superuser("rajdeep", "rajdeep1008@gmail.com", "romeoalfa@1717")
			User.objects.create_superuser("raunaq", "raunaq.soni@gmail.com", "golfuniform@1717")
			User.objects.create_superuser("ashish", "ashishgulati71@gmail.com", "alfasierra@1717")
