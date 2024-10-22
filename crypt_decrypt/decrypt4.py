import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import itertools

ciphertext_base64 = "OgJuOYJZT0FDb47DBOkNgA=="

possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

all_combinations = []
for p1 in possible_chars:
    for p2 in possible_chars:
        for p3 in possible_chars:
            for p4 in possible_chars:
                key= p1 + p2 + p3 + p4 + "IsASecretKey"
                
print (key)
        