import os


def rename_files():
    # 1 - get file names from a folder. the r in the path means interpret literally
    file_list = os.listdir(r"/Users/jasonsimpson/Dropbox/Dev/python_intro_course/prank")
    print(file_list)
    # 2 - for each file, rename filename
    # change directory to what we want first, but first get the current working dir
    saved_path = os.getcwd()
    os.chdir(r"/Users/jasonsimpson/Dropbox/Dev/python_intro_course/prank")
    for file_name in file_list:
        # .translate takes in a table (not using atm) and what you want to strip out
        os.rename(file_name, file_name.translate(None, "0123456789"))
    # now change directory back
    os.chdir(saved_path)

rename_files()
