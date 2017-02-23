from django.core.management.base import BaseCommand, CommandError
from filer.models.filemodels import File
from shutil import copyfile
import os, errno


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

        parser.add_argument(
            '--transfer',
            action='store_true',
            dest='transfer',
            default=False,
            help='Transfer logical filer directories to physical directories [images/<filer-dir>/<img_name>]; NOTE: will replace any existing files',
        )

    def get_altered_path(self, p):
        p.lower()
        p.replace(" ", "_")
        return p

    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

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
        if options['transfer']:
            x=0
            docbase = "/vagrant/ubuntu/djangocms/website_content/media"
            imgbase = "/vagrant/ubuntu/djangocms/website_content/new_media"
            self.stdout.write("images: %s" % len(images))
            for image in images:
                x=x+1
                # self.stdout.write("***** original_file: %s" % image.original_filename)
                # self.stdout.write("***** file: %s" % image.file)
                f = image.file
                f = '/' + str(f).lower()
                p = '/' + "/".join([_f.name for _f in image.logical_path + [image]])

                # self.stdout.write("##### filename: %s" % image.name)
                # self.stdout.write("***** logical path: %s" % p)
                ap = p.lower().replace(" ", "_")
                # self.stdout.write("***** altered path: %s" % ap)
                if len(image.name) > 0:
                    pos = len(ap) - len(image.name)
                    if pos >= 1:
                        ap = ap[0:pos]
                # self.stdout.write("***** altered path after imagename: %s" % ap)
                # self.stdout.write("making directory if it doesn't exist: %s" % imgbase + ap)
                self.mkdir_p(imgbase + ap)
                nf = ap + image.original_filename.lower()
                # self.stdout.write("***** altered path: %s" % nf)
                # buf = image.path + "\t" + image.original_filename + "\t" + str(image.owner) + "\t" + str(image.size)
                self.stdout.write("%s -> %s [%s]" % (f, nf, image.size))
                # self.stdout.write("file: %s" % f)
                # src = docbase + image.file
                # dst = imgbase + nf
                # copyfile(src, dst)
                # for attr in image.__dict__:
                #     self.stdout.write("obj.%s = %s" % (attr, getattr(image, attr)))
                src = docbase + f
                dst = imgbase + nf
                # self.stdout.write("src: %s" % src)
                # self.stdout.write("dst: %s" % dst)
                copyfile(src, dst)

                if x>10:
                    break
