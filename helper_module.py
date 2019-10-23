import shutil
import os
import glob


#SOURCE: https://stackoverflow.com/questions/41826868/moving-all-files-from-one-directory-to-another-using-python

"""This is the one. Works like a charm!"""
def move_png(dir_name):

    source_dir = '/home/danw32/PyCharmProjects/TestProjectVEnv/Screenshots/' #Path where your files are at the moment

    try:
        dst = '/home/danw32/PyCharmProjects/TestProjectVEnv/Screenshots/row_' + str(dir_name)
        os.makedirs(dst)
    except:
        pass

    #dst = '/home/danw32/PyCharmProjects/TestProjectVEnv/Screenshots/' + str(dir_name) #Path you want to move your files to

    files = glob.iglob(os.path.join(source_dir, "*.png"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dst)