from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Change all user passwords to password for local environment'

    def handle(self, *args, **options):
        try:
            from django.contrib.auth.models import User
            users = User.objects.all()
            for user in users:
                self.stdout.write("user: " + str(user.username))
                user.set_password('password')
                user.save()

        except Exception as e:
            raise CommandError("An error has occurred: {}".format(e))

        self.stdout.write("")
        self.stdout.write("Command executed successfully")
