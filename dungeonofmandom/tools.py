import os


def build_file_path(instance, filename):
    return "images/{modelname}/{filename}".format(
        modelname=instance.__class__.__name__,
        filename=build_filename_format(instance, filename)
    )


def build_filename_format(instance, filename):
    return "{id}-{name}{extension}".format(
        id=instance.id,
        name=instance.name,
        extension=os.path.splitext(filename)[1],
    )

