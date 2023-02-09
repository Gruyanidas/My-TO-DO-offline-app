FILEPATH = "to_dos.txt"


def get_to_dos(filepath=FILEPATH):  # defaulult argument
    with open(filepath, 'r') as file_local:  # to_dos.txt moze da se menja sa file path
        to_dos_local = file_local.readlines()  # ovde je dat kao default path
    return to_dos_local  # dobijamo listu


""" Read a text file and return the list of to-do items."""


def write_to_dos(to_dos_asarg, filepath=FILEPATH):  # file path je isti
    with open(filepath, 'w') as file_local:
        file_local.writelines(to_dos_asarg)  # procedura upisivanja na listu


""" Write the to-do items list in the text file."""
