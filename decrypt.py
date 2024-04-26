"""
Takes our "ciphertext" file, performs a simple frequency analysis on the
characters in use, works out the likely (caesar cipher) shift amount
and decrypts.
"""

import timeit
import string

def main():
    ciphertextbook = "Ciphertext.txt"
    decrypttextbook = "Decryptedtext.txt"
    filestring = ""
    outstring = ""

    print("\n\n")
    starttime0 = timeit.default_timer()
    print("Decrypting file : ".ljust(50), ciphertextbook)

    # open the file and obtain contents
    filehandle = open(ciphertextbook, "r", encoding="utf-8")
    filestring = filehandle.read()
    filehandle.close()
    print("Time taken to read file (seconds) : ".ljust(50), "%.4f" % (timeit.default_timer() - starttime0))

    # for all uppercase alpha characters (our starting point was a book
    # of only uppercase chars), get the number of matching instances
    # for that character within the book, and build up key:value pairs

    starttime1 = timeit.default_timer()
    charcountsdict = {}

    for char in string.ascii_uppercase:
        _count = filestring[0:1000000].count(char)
        #_count = filestring.count(char)
        charcountsdict[char] = _count

    # convert our dictionary to list, and sort in (reverse) order
    # of the values (i.e. letter with highest count goes first)
    charcountslist = list(charcountsdict.items())
    charcountslist.sort(key=lambda a: a[1], reverse = True)

    # get the most common char from the list and work out the likely shift amount
    # compared to E (AscII 69) (... the most likely common letter in any text)
    mostcommonchar = ord(charcountslist[0][0])
    likelyshiftamount = mostcommonchar - ord("E")

    # for letters 'less' then E it'll go negative, so wrap the shift amount
    if likelyshiftamount < 0:
        likelyshiftamount += 26

    print("")
    print("Finished Analysis...".ljust(50))
    print("5 Most common characters : ".ljust(50), charcountslist[0:5])
    print("Most common character (Encrypted 'E') : ".ljust(50), charcountslist[0][0])
    print("Likely Shift Amount (diff. from above to E) : ".ljust(50), likelyshiftamount)
    print("Time taken for analysis (seconds) : ".ljust(50), "%.4f" % (timeit.default_timer() - starttime1))
    print("Number of characters in book : ".ljust(50), len(filestring))

    # 'decrypt' using likely shift amount
    starttime2 = timeit.default_timer()

    outstring = ""
    for char in filestring:
        outchar = ord(char)
        if 65 <= outchar <= 90:
            outchar += (likelyshiftamount * -1)

            # wrap around if past 90 (Z)
            # wrap around if less than 65 (A)
            if outchar > 90: outchar -= 26
            if outchar < 65: outchar += 26

        # append the decrypted character to the full decryption string
        outstring += chr(outchar)

    # write the finalised string out to file
    filehandle = open(decrypttextbook, "w", encoding="utf-8")
    filehandle.write(outstring)
    filehandle.close()

    print("")
    print("Decrypted file has been created : ".ljust(50), decrypttextbook)
    print("Time taken for decrypt/write (seconds) : ".ljust(50), "%.4f" % (timeit.default_timer() - starttime2))

    print("")
    print("Total Time (seconds) : ".ljust(50), "%.4f" % (timeit.default_timer() - starttime0))

    print("\n\n")
    print("Example from decrypted file:\n")
    print(outstring[0:400].strip())
    print("\n\n")

if __name__ == "__main__":
    main()
