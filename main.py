"""
Authos: Felipe Duarte

Decrypting REMCOS RAT configuration

For this to work, you need to manually extract the SETTINGS data from the RAT's resources usign Resource Hacker or
any other tool, then use this tool to decrypt its contents.
"""

import rc4

with open('settings.bin', 'rb') as f:
    settings = f.read()

key_len = ord(settings[0])
key = rc4.convert_key(settings[1:key_len+1])
data = settings[key_len+1:]

keystream = rc4.RC4(key)
decrypted = ''

for item in data:
    decrypted += chr(ord(item) ^ keystream.next())

urls = decrypted.split('|')[:-1]

print("C2 Servers:")

for url in urls:
    print(url)
