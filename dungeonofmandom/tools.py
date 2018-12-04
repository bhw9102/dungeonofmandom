import os
import datetime


def build_file_path(instance, filename):
    return "images/{modelname}/{filename}".format(
        modelname=instance.__class__.__name__,
        filename=build_filename_format(instance, filename)
    )


def build_filename_format(instance, filename):
    now = datetime.datetime.now()
    return "{name}-{now}{extension}".format(
        name=instance.name,
        now=str(now.date()),
        extension=os.path.splitext(filename)[1],
    )

