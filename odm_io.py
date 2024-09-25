import os
import shutil, errno
import json

def file_exists(path_file):
    return os.path.isfile(path_file)

def dir_exists(dirname):
    return os.path.isdir(dirname)

def related_file_path(input_file_path, prefix="", postfix="", replace_base=None):
    """
    For example: related_file_path("/path/to/file.ext", "a.", ".b")
     --> "/path/to/a.file.b.ext"
    """
    path, filename = os.path.split(input_file_path)

    # path = path/to
    # filename = file.ext

    basename, ext = os.path.splitext(filename)
    # basename = file
    # ext = .ext

    if replace_base is not None:
        basename = replace_base

    return os.path.join(path, "{}{}{}{}".format(prefix, basename, postfix, ext))

