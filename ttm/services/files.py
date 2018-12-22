import os
import shutil


class FileInterface:

    def create_directory(name):
        if not os.path.isdir("./{}".format(name)):
            os.makedirs("./{}".format(name))

    def create_file_with_content(path, content):
        f = open(path, "w+")
        f.write(content)
        f.close()

    def copy_file(source, dest):
        shutil.copyfile(source, dest)
