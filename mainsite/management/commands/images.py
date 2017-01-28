from django.core.management.base import BaseCommand, CommandError
from filer.models.filemodels import File


class Command(BaseCommand):
    help = 'Filer Images Utility'

    def add_arguments(self, parser):

        parser.add_argument(
            '--list',
            action='store_true',
            dest='list',
            default=False,
            help='List Files Known to Filer',
        )

        parser.add_argument(
            '--duplicates',
            action='store_true',
            dest='duplicates',
            default=False,
            help='List Duplicate Files in Filer',
        )

    def handle(self, *args, **options):
        images = File.objects.all()
        if options['list']:
            for image in images:
                buf = image.original_filename + "\t" + str(image.owner) + "\t" + str(image.size)
                self.stdout.write(buf)
        if options['duplicates']:
            j = 0
            for image in images:
                dups = image.duplicates
                if dups:
                    j += 1
                    buf = "\n" + str(j) + ". " + image.original_filename + " at " + image.path
                    self.stdout.write(buf)
                    i = 0
                    for dup in dups:
                        i += 1
                        buf = "\t" + str(i) + ". Relative URL: " + dup.url
                        self.stdout.write(buf)
                        buf = "\t" + str(i) + ". File Path:    " + dup.path
                        self.stdout.write(buf)
