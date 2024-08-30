![image](https://github.com/user-attachments/assets/7ed820c9-580a-40a4-b84c-f2b92a0fc9df)


# DehashEZ

Password dehasher using Python.

[Support Discord server](https://discord.gg/sn7JX2VQgT)

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

![image](https://github.com/user-attachments/assets/3d803b83-1098-4305-b56d-1fdb6b89e31d)





# Wordlist 📃
You can choose a wordlist with the name (Must be in the same directory as dehashez.py) like in the photo, or
![image](https://github.com/user-attachments/assets/93f1779c-ca10-43cc-9f94-f95e2b1df013)

You can select a wordlist using the path, or you can add a default wordlist to the code so you don't have to write it every time.
(Line 11)
![image](https://github.com/user-attachments/assets/b439a4c0-8396-4482-85e5-6921fe6f09ee)



If you verified that the wordlist file is in place but the program is unable to detect it, remember that you must write the full name of the file, including the format (For example .txt)

"wordlist" = ❌

"wordlist.txt" = ✅

If the program still unable to detect the wordlist, join the [Support Discord server](https://discord.gg/sn7JX2VQgT). 

If you don't have a wordlist or you can't find any password with yours, join the Discord so we can give you a pretty good one.


# Salt 🧂

Salt is optional, if the hash you want to decrypt does not have a salt, do not fill in the "SALT" field in the program and simply press enter leaving it empty.
The format of hashes with salt is usually $ALGORITHM$SALT$HASH, so if you want to extract the salt from a hash, you can do it with that format.

# Images 📷
![image](https://github.com/user-attachments/assets/364d2b12-27aa-45d9-83e5-96721033321e)

![image](https://github.com/user-attachments/assets/fbed0822-ae6d-4e69-b338-fb895c01d969)

![image](https://github.com/user-attachments/assets/c09a298a-33c9-4a21-8b52-bf0a80b3ffd8)






# Additional information
- Obviously you must have python installed on your system to be able to run this program [Download Python](https://www.python.org/downloads/)
- Credits: Some parts of this code from zNotDev, LiptomAlex Zen-kun04 and Srdhash11
- Support: https://discord.gg/sn7JX2VQgT (Again)
- By ryzzu

