"""
Takes our "plaintext" file and encypts (... badly ...) the alphabetic characters
With a Caesar cipher for a randomly generated shift amount.
Note - not much error or i/o handling here.
Note - use the Prep.py to create the initial "Plaintext.txt" file
(all uppercase for simplicity)
"""

import timeit
import random

def main():
    starttime1 = timeit.default_timer()

    plaintextbook = "Plaintext.txt"             # input file
    ciphertextbook = "Ciphertext.txt"           # output file
    outstring = ""

    # work out our random shift amount
    caesarshiftamount = random.randint(1, 26)

    print("\n\n")
    print("Creating encrypted file of : ".ljust(50), plaintextbook)

    # open the file and obtain contents
    filehandle = open(plaintextbook, "r", encoding="utf-8")
    filestring = filehandle.read()
    filehandle.close()

    # go through string, get ascii value of each char and then 'shift'
    # this value using the random shift amount established above
    for char in filestring:
        outchar = ord(char)                     # get ascii value of char
        if 65 <= outchar <= 90:
            outchar += caesarshiftamount        # shift value

            # wrap around if past 90 (Z)
            # wrap around if less than 65 (A)
            if outchar > 90: outchar -= 26
            if outchar < 65: outchar += 26       # shouldn't happen...

        # add the shifted character to our output string
        outstring += chr(outchar)

    # and write it out to file
    filehandle = open(ciphertextbook, "w", encoding="utf-8")
    filehandle.write(outstring)
    filehandle.close()

    print("Encrypted file has been created : ".ljust(50), ciphertextbook)
    print("Time taken for encryption (seconds) : ".ljust(50), "%.4f" % (timeit.default_timer() - starttime1))
    print("\n\n")
    print("Example from encrypted file:\n")
    print(outstring[0:400].strip())
    print("\n\n")

if __name__ == "__main__":
    main()
