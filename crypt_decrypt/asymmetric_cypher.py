# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEoQIBAAKCAQEApqKUhBZyo4zcBv/R1tB0W8whf/xe/wKcczD9XiyeWcX9FnKQ\nAbuFPx0YcWfiEv5ZE0pORzfCQL8zGwIMjmyHtWpPisok12LqOvE6HGKCycJwa2rL\nDEHjr19wWE5qc8HdmVnlHoKHnB5faaUwpmFxgXsmuEwbuSKMJMbREO75Iiht9mOa\noSG+KAq5DquP2svJir9L8fF9WE39rzxOg7ZRyj42qu+CZCJi/S7NqVJ0Qzl6xw/K\nhuR+yYi0wsG3DuUCQXNR/dYoulYQ/c8GgR9tmSQeQUVRaOcXiFx6GG+uOdiH+3gB\nQeO+nzTpvUqzHrZjCm3GQnqLOBjYPkCnlukq9wIDAQABAoH/D/J/RCTh08UnSYQy\nENziRebDTfxZGw6k6mFF3j1m6jCIiB1uqrvHhMLEFBZdDHRLEg2KcEZl0Mx7l5oa\nmYbJdhM2iZHO9M4CnKF5bj3/Rk/VcnJF/GZR4/a+SbU3etyS2JpB0ymq0MYXW4Tz\noviwZDPlAL5H6O/leZ+NYpF8Rkhwhcada8ZHMZ/MYzQG4uZz7Xz0Ltzy7xAcuWNl\nwz6TA0LjpTH9rdjpnqwgKSgjCx0HjU9w4DqGGPEKwZr6uhi8vzGwCARX6Longvcv\nZOZjNcXbZx/h7FnHnJngcS1NaqZhxnwDoj9Y1XkwVT7CJ2fDGEyNP/5ZVXl1IjCw\nZA7JAoGBALt9C8Gj5zKi0mEWpY2z7wcTPeGNNOqmda5/UWVS/rnLAq6lXcNTXaRq\nI/NBw+4aPg219Di/sgleXxd0ILElSmeeEjO3dYCzOhcE6Uxc9YLKwTuFeGhjWV0u\neeIkVjuouLu+gswbEJiVWFvAzKpPgMPE3eS27/+NvHLpXLy3RSj5AoGBAOOGxCAT\nSCNcceToVUUiZkbgnMalV+2iDBK3v9fwikbxRwEpQfSfhRe782P8HbMWsYV2C/hS\nfKZBunFxqQJwpW1A1L3g+XnHrZlvzsYOYHF+V7xTgMks6aXYhKxmeihyRnltX+WM\nlKfNC1aKPmKuJtODngWavcG2p7fLgoGJeF9vAoGAGRBBVxSLHqjHiPUXEpdgN8jp\nt9JBpbC1AKvCfNIYfUvXQvOWUjs9xHHv9l/vSlA1xW1yhXeS3E/CVIdQq325sZpf\nAoze52KOPG+KpIu0wlRKeqOAEixd0OgaoRGMeZM3htmT8KcZk9w7IKDoe0f/haw2\noZGXCcmvzIjHve6eDzkCgYEAj8jy2HJW/EHHmCla+b2rdM8tRDvpPTtS9eE5U3Wn\nbP29KXaxP64vpbgZL+57tll5BiZ7mgpGy6pt8JMrg2c8o7Z8uyIZhmQxyO1ndrJP\nMGnveAwtLvU7Epup/Gkmebj94G7GU4Jrzz89Ewt6MVJtJu3eRxxrHqgXhYcOil4d\nu/ECgYAd1dAEcV/E1AkGR6hL3A0R7L1D6V5cOTMhyS/u64xOgjj0vrWpKYIIiSqx\nM3eOY6WgoiMVC3VpyGfqTHRUiUH+0oj6ZPGe/cWZhItAQwEsKs83KKvBGef3/YJ6\nxo+vECGlbLFUXfng9RYce3qSsOz5YAVX1H4o5uS+lIqgOkmMNg==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwa26Gpjr9j3vMwutUpEI\njPvH1GrSJXozIROn6qLLuWVE4D81lhaiEJW0+CGlvsvaIAatBgWX2sRfLcR3t/Li\nCryWtGqJ683pDrLiW4ycQdbDJ/MBpv3MPxx+8FBZnFzgNOxVFUwDvYQQ+VpgIq47\nHd7Z714cBc8ZHKnBDJwxbR4JEGIGUcchkKco9MxH4dMUeOKpYmqXLqtAtmYA4VFS\nG22gE7KfMJfOY36nJheNYKV4P4Axe0pQd5oyRWUnEfupbr2R+A6t5Yks30kEewCT\nFfRpEaO/qM3SwPfPVF9lELYRTU7IbeDNI+CsL+LTSsBG+rNDGnTm0Rfi9Or6IvVx\n/QIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "Torneremo"
encrypted_message = encrypt_message(message, public_key)
encrypted_message = "I2qDhKmbI/U4OhH+XELx9xxbNtY6sz6rtZ8rxeu+pXvzDTFLwLfEqa7U9kCgeWukqzYQr87hCzR4/BFHp9vpruLupBBXOgmBw9L2feNPFWFWakA988mMhUSXRJygATXr5EPqo5wRzKgVcUtqxDJV9CF0IcOXQtX0+qi1Y/cAemzZFfejq1J/DAnZfIh+R7TqeJktvQ23/sInVGfIfYivc50psmmbfpI/VrMrKB82eb+nesl+vitCxjQfu9Q7QlwHxeMlC8kJgnasbchOWfwGGCYiKk/bh03Ou9F0iDutapUxkq0IyNu1KRjAtzN4CIAWOTZbS0BdGtE1b3JRyIt45A=="
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)