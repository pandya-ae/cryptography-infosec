# -*- coding: utf-8 -*-
"""product-cipher.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B93be8bht_1aGyHuk-ocQeZ28BnYk2pW

Caesar -> Transpose -> Caesar
"""

x = [3,1,4,5,2]
y = [2,5,1,3,4]
shift = 3
alpha = 'abcdefghijklmnopqrstuvwxyz'
msg = input("Input Message: ").lower()
msg1 = ""
msg1 = msg
enc = ""

###Encryption###

#Append padding letters
while len(msg)%5 != 0 :
   msg = msg + "x"
   
#Caesar Cipher encryption

#First Caesar Cipher encryption
for i in msg :
  if i != ' ' :
   enc = enc + alpha[(alpha.find(i)+shift)%26]
  elif i == ' ' :
    enc = enc + ' '
print("First Caesar Cipher:",enc.upper())
msg = enc
enc = ""

#Transposition matrix encryption
mat = [["x" for i in range(5)] for j in range(int(len(msg)/5))]
print("Transposition Matrix: ")
for i in range(int(len(msg)/5)) :
   for j in range(5):
       print(msg[i*5+j], end=" ")
   print()
for i in range(5) :
   for j in range(int(len(msg)/5)) :
       if j*5+x[i]-1 < len(msg) :
           mat[j][i] = msg[j*5+x[i]-1]
enc = ""
for i in range(5) :
   for j in range(int(len(msg)/5)) :
       enc = enc + mat[j][i]
msg = enc
enc = ""

#Second Caesar Cipher encryption
for j in msg :
  if j != ' ' :
   enc = enc + alpha[(alpha.find(j)+shift)%26]
  elif j == ' ' :
    enc = enc + ' '
print("Encrypted Message:",enc.upper())

###Decryption###
dec = ""

#First Caesar Cipher decryption
for i in enc :
  if i != ' ' :
    dec = dec + alpha[(alpha.find(i)-shift)%26]
  elif i == ' ' :
    dec = dec + ' '
print("First Caesar Decrypted Message:",dec.upper())
enc = dec
dec = ""

#Transposition matrix decryption
for i in range(5) :
   for j in range(int(len(enc)/5)) :
       mat[j][i] = enc[i*(int(len(enc)/5))+j]
enc= "" 
for i in range(int(len(msg)/5)) :
   for j in range(5) :
       enc = enc + mat[i][y[j]-1]
print("Transposition Decrypted Message:",enc.upper())

#Second Caesar Cipher decryption
for j in enc :
  if j != ' ' :
    dec = dec + alpha[(alpha.find(j)-shift)%26]
  elif j == ' ' :
    dec = dec + ' '

#Padding letter removal
rem = len(dec)-len(msg1)
remove = dec[:-rem]
if len(remove) == 0 :
  print("Final Message:",dec.upper())
else :
  print("Final Message:",remove.upper())

"""2x Caesar -> Transpose"""

x = [3,1,4,5,2]
y = [2,5,1,3,4]
shift = 3
alpha = 'abcdefghijklmnopqrstuvwxyz'
msg = input("Input message: ").lower()
msg1 = ""
msg1 = msg
enc = ""

###Encryption###

#Append padding letters
while len(msg)%5 != 0 :
   msg = msg + "x"
   
#Caesar cipher encryption

#First encryption
for i in msg :
  if i != ' ' :
   enc = enc + alpha[(alpha.find(i)+shift)%26]
  elif i == ' ' :
    enc = enc + ' '
print("First Caesar cipher:",enc.upper())
msg = enc
enc = ""

#Second encryption
for j in msg :
  if j != ' ' :
   enc = enc + alpha[(alpha.find(j)+shift)%26]
  elif j == ' ' :
    enc = enc + ' '
print("Second Caesar cipher:",enc.upper())
msg = enc
enc =""

#Transposition matrix encryption
mat = [["x" for i in range(5)] for j in range(int(len(msg)/5))]
print("Transposition Matrix: ")
for i in range(int(len(msg)/5)) :
   for j in range(5):
       print(msg[i*5+j], end=" ")
   print()
for i in range(5) :
   for j in range(int(len(msg)/5)) :
       if j*5+x[i]-1 < len(msg) :
           mat[j][i] = msg[j*5+x[i]-1]
enc = ""
for i in range(5) :
   for j in range(int(len(msg)/5)) :
       enc = enc + mat[j][i]
print("Encrypted Message:",enc.upper())

###Decryption###
dec = ""

#Transposition matrix decryption
for i in range(5) :
   for j in range(int(len(enc)/5)) :
       mat[j][i] = enc[i*(int(len(enc)/5))+j]
enc= "" 
for i in range(int(len(msg)/5)) :
   for j in range(5) :
       enc = enc + mat[i][y[j]-1]
print("Transposition Decrypted: ", enc.upper())

#Caesar cipher decryption

#First decryption
for i in enc :
  if i != ' ' :
    dec = dec + alpha[(alpha.find(i)-shift)%26]
  elif i == ' ' :
    dec = dec + ' '
print("First Decrypted Message:",dec.upper())
enc = dec
dec = ""

#Second decryption
for j in enc :
  if j != ' ' :
    dec = dec + alpha[(alpha.find(j)-shift)%26]
  elif j == ' ' :
    dec = dec + ' '
print("Second Decrypted Message:",dec.upper())

#Padding letter removal
rem = len(dec)-len(msg1)
remove = dec[:-rem]
if len(remove) == 0 :
  print("Final Message:",dec.upper())
else :
  print("Final Message:",remove.upper())