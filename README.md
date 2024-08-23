![image](https://github.com/user-attachments/assets/445aa3b4-decc-4003-a023-4db7dfd36fe8)

# DehashEZ

Password dehasher using Python.

Support: https://discord.gg/HUgmXaPXSU

# UPDATE - 27/08/2024
Improvements: 

**Timeout**
- Dehashing timeout set to 40 seconds.
- You can change this in the code (Line 13)

**Default wordlist path**
- You can add the path of a default wordlist, so you don't have to write it every time.
- Paste your wordlist path in the code, line 11.

**Optimization in the bruteforce function**
- Dehashing time has been reduced by approximately 40-80 seconds.
- The simplest passwords can be cracked in less than 1 second (Before, in 20).
  
**Optimized wordlist upload**
- Wordlist processing time was reduced by 2-3 seconds.

**Optimized interface**
- New successful dehash screen.
- Simplified error handling and menu options.
- Total dehashing time is calculated more accurately and presented in a more readable manner.
- The hash result is automatically copied to the clipboard.


# Hash 🔒

This program accepts SHA256 and SHA512 hashes, with an optional salt.
So, this includes, AuthMe hashes, DynamicBungeeAuth hashes, etc.

When the program finds the original hash value, it will display it on the screen and automatically copy it to your clipboard.

![image](https://github.com/user-attachments/assets/a49f0be6-b889-4135-a56b-2ab504bd1d4c)



# Wordlist 📃
You must put your wordlist file in the same directory as main.py

![image](https://github.com/user-attachments/assets/93f1779c-ca10-43cc-9f94-f95e2b1df013)


If you verified that the wordlist file is in place but the program is unable to detect it, remember that you must write the full name of the file, including the format (For example .txt)

"wordlist" = ❌

"wordlist.txt" = ✅

If the program still unable to detect the wordlist, verify that you are running the correct main.py in the correct path. 

You can check this in the title of the program window.

If you don't have a wordlist or you can't find any password with yours, join the Discord so we can give you a pretty good one.


# Salt 🧂

Salt is optional, if the hash you want to decrypt does not have a salt, do not fill in the "SALT" field in the program and simply press enter leaving it empty.
The format of hashes with salt is usually $ALGORITHM$SALT$HASH, so if you want to extract the salt from a hash, you can do it with that format.


# Additional information
- Obviously you must have python installed on your system to be able to run this program [Download Python](https://www.python.org/downloads/)
- Credits: Some parts of this code from zNotDev, LiptomAlex Zen-kun04 and Srdhash11
- Support: https://discord.gg/HUgmXaPXSU (Again)
- By ryzzu

