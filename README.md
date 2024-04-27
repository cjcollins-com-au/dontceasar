Firstly - in case it isn't evident from the title, don't use Caesar ciphers.  This program demonstrates why.

I am also aware that I didn't spell Caesar correctly in the repo title.  Sorry.

Requires python.  Run in terminal window.

Usage:
encrypt.py - will encrypt the source/plaintext document Plaintext.txt to Ciphertext.txt, using Caesar cipher and
randomly selected shift amount.  Stats and example shown on screen.  A source Plaintext.txt document is provided
but you can also use Prep.py to create another - see below.

decrypt.py - will perform analysis on the document Ciphertext.txt, and then attempt decryption using the most 
likely shift amount it worked out based on frequency analysis of all the letters in the Ciphertext.  Assumes 
it's in English also (looks for 'E' as the most common letter).  Stats and information shown on screen also.

Prep.py - optional.  Creates the Plaintext.txt from any other text document, in this case I've used a text
from Project Gutenberg as an example.  This simply moves everything to upper case just for ease of explanation
in the other steps.


The point of this & why not to use other ciphers...

The decrypt.py process tends to make fairly short work of frequency analysis of any text; my tests on a 
moderately powered 5 year old PC tend to take about 4ms to analyse a text of 160,000 characters. 
There are of course only 26 (or 25...) combinations for a Caesar cipher (easy to brute force as well) 
but this just illustrates the ease with which a computer can analyse a cipher.  Obviously a more 
sophisticated cipher will take longer, and perhaps the length of text here makes it ideal for frequency
analysis but we can see how quick a simple analysis takes.  

(I have an example of using Vigenere cipher which I'll publish at a later stage, this takes longer but 
has a combination of brute-force and frequency analysis to crack so takes longer but still gets through 
an enormous number of attempts comparitively quickly, and there are much better algorithms than my 
approach).

Also - proper crypto is easy.  Most programming languages have libraries available to easily perform
AES and other crypto operations with only a few lines of code.  
