# DehashEZ

Password dehasher using Python.

Support: https://discord.gg/HUgmXaPXSU


# Wordlist
You must put your wordlist file in the same directory as main.py

Example: https://i.postimg.cc/DzcV00XT/image.png

If you verified that the wordlist file is in place but the program is unable to detect it, remember that you must write the full name of the file, including the format (For example .txt)
"wordlist" = NO
"wordlist.txt" = YES

If the program still unable to detect the wordlist, verify that you are running the correct main.py in the correct path. 

You can check this in the title of the program window.

If you don't have a wordlist or you can't find any password with yours, join the Discord so we can give you a pretty good one.


# Hash

This program accepts SHA256 and SHA512 hashes, with an optional salt.
So, this includes, AuthMe hashes, DynamicBungeeAuth hashes, simple hashes. etc

When the program finds the original hash value, it will display it on the screen and automatically copy it to your clipboard.
Successful dehash example: https://i.postimg.cc/bwJtYCFY/image.png


# Salt

Salt is optional, if the hash you want to decrypt does not have a salt, do not fill in the "SALT" field in the program and simply press enter leaving it empty.
The format of hashes with salt is usually $ALGORITHM$SALT$HASH, so if you want to extract the salt from a hash, you can do it with that format.

For example: SHA256$3aa69d59fbe6fe5dadad25219d1ca6e3e$9fb8c7930484f69fd6dda1317553aa1cc7a01enc73044752574e6cf813a9a25
Type = SHA256
Salt = 3aa69d59fbe6fe5dadad25219d1ca6e3e
Hash = 9fb8c7930484f69fd6dda1317553aa1cc7a01enc73044752574e6cf813a9a25




Support: https://discord.gg/HUgmXaPXSU (Again) 
