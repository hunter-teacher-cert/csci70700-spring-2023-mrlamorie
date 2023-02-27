import random

# For the encrpting portion of the assignment I am making a substitution cipher
# this particular version will have all of the letters of the alphabet as well as
# most standard punctuation, space and numbers. It will randomize all of these
# things and return an output string. I am using all lower chars for this.

# basic test
tS0 = "123" 

# standard test
tS1 = "This is a readable test string"

# sanity check
tS2 = "11111 aaaaa bbbbb ccccc ddddd ,,,,, ..... !!!!!"

# the raw alphabet to be used
alpha = "abcdefghijklmnopqrstuvwxyz.,! 1234567890"

def makeCipher(alpha):
  
  # it didn't like shuffle, I'm not sure why, I think because of the numerics?
  # anyway, in this step I make my alphabet a list, then use sample and the length
  # of the alphabet to shuffle it
  cipher = random.sample(list(alpha), len(list(alpha)))

  # I don't have to do this, I am doing this so there can be a quick compare.
  # I undo it below in the next method. This isn't for production, it's for
  # class, so I wanted it to be clear at all steps. =) Anyway, this just turns
  # the key back into a string
  return ''.join(cipher)

key = makeCipher(alpha)
print("The Alphabet is: ")
print(alpha)
print("The key is: ")
print(key)

def encrypt(text, alpha, key):
  # text to lower
  alpha = list(alpha)
  key = list(key)
  text = text.lower()
  retText = ""
  # there are much better ways to do this, but hey, this does the job
  for char in text:
    i = alpha.index(char)
    retText += key[i]

  return retText

print("Test 1 - 123 numbers")
print(tS0)
print(encrypt(tS0, alpha, key))
print()

print("Test 2 - sanity check")
print(tS2)
print(encrypt(tS2, alpha, key))
print()

print("Test 3 - encrpt test text")
print(tS1)
print(encrypt(tS1, alpha, key))
