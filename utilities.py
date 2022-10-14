import os.path


def search_user(file_name, record):  # exist -> return record | not exist -> return False
    # if the record file exists:
    if os.path.isfile("{}.txt".format(file_name)):
        with open("{}.txt".format(file_name), 'r') as file:
            # start reading the file
            file.readline()
            next_line = file.readline()
            # check until the file reaches to its end
            while next_line != "":
                if record in next_line:
                    return next_line.strip().split(",")
                next_line = file.readline() # --> if record wasn't found, go to next line
        return False
    # if the file doesn't exist:
    raise TypeError("{} dose not existed".format(file_name))