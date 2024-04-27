# Caesar Cipher - Frequency Analysis & Decrypt

Note - don't use Caesar ciphers in real life.  This program demonstrates why.

I am also aware that I didn't spell Caesar correctly in the repo title.  Sorry.

## Requirements

Requires python. 
Install websockets: $pip install websockets

(Install pip first if you don't already have it, on Linux this would be: $sudo apt install python3-pip)

Run in terminal window on Windows / Linux / Mac.  Can also run within PyCharm or VS Code.

## Usage

**encrypt.py** - will encrypt the source/plaintext document Plaintext.txt to Ciphertext.txt, using Caesar cipher and
a randomly selected shift amount.  Statistics and example output are shown on screen.  A source Plaintext.txt 
document is provided but you can also use Prep.py to create another - see below.

**decrypt.py** - will perform analysis on the document Ciphertext.txt, and then attempt decryption using the most 
likely shift amount (worked out based on frequency analysis of all the letters in the Ciphertext).  Assumes 
it's in English also (looks for 'E' as the most common letter).  Statistics and example output are 
shown on screen also.

**Prep.py** - *optional*.  Creates the Plaintext.txt from any other text document, in this case I've used a text
from Project Gutenberg as an example.  This simply moves everything to upper case just for ease of explanation
in the other steps.


## The point of this & why not to use other ciphers...

The decrypt.py process tends to make fairly short work of frequency analysis of any text; my tests on a 
moderately powered 5 year old PC tend to take about 4ms to analyse a text of 160,000 characters. 
There are of course only 26 (or 25...) combinations for a Caesar cipher (easy to brute force as well) 
but this just illustrates the ease with which a computer can analyse a cipher.  Obviously a more 
sophisticated cipher will take longer, and perhaps the length of text here makes it ideal for frequency
analysis but we can see how quick a simple analysis takes.  

*(I have an example of using Vigenere cipher which I'll publish at a later stage, this takes longer but 
has a combination of brute-force and frequency analysis to crack so takes longer but still gets through 
an enormous number of attempts comparitively quickly, and there are much better algorithms than my 
approach).*

**Also - proper crypto is easy.  Most programming languages have libraries available to easily perform
AES and other crypto operations with only a few lines of code.  These libraries have (probably) 
been developed by well resourced teams, subject to significant QA processes and independently verified. 
They implement schemes like AES that were designed by VERY smart people and subject to ridiculous 
amounts of scrutiny over a vey long period of time (... by both friend and foe, and supercomputers), and
still stand up as secure.**  
