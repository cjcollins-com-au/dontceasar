"""
Takes our source book and creates the 'plaintext' version to work with... 
this is really just a conversion to upper case of the content to simplify
the explanation of the caesar encrypt/decrypt and analysis (otherwise we'll
get too bogged down in code detail rather than the point of the exercise...).
"""

import os


def main():
    sourcebook = "Alice_Original.txt"
    plaintextbook = "Plaintext.txt"

    # open the file and obtain contents
    filehandle = open(sourcebook, "r", encoding="utf-8")
    filestring = filehandle.read()
    filehandle.close()

    # convert to upper case
    filestring = filestring.upper()

    # and write it out
    filehandle = open(plaintextbook, "w", encoding="utf-8")
    filehandle.write(filestring)
    filehandle.close()


if __name__ == "__main__":
    main()
