def read_file_lines(filename):

    with open(filename, "r") as file:
        return file.readlines()
