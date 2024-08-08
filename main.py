#======================================================================================================


#              Don't touch anything unless you know exactly what you're doing.


#======================================================================================================

import hashlib, time, os, shutil
import pyperclip as clipboard
from colorama import Fore

words = set()

#======================================================================================================

logo = """
██████╗░███████╗██╗░░██╗░█████╗░░██████╗██╗░░██╗███████╗███████╗
██╔══██╗██╔════╝██║░░██║██╔══██╗██╔════╝██║░░██║██╔════╝╚════██║
██║░░██║█████╗░░███████║███████║╚█████╗░███████║█████╗░░░░███╔═╝
██║░░██║██╔══╝░░██╔══██║██╔══██║░╚═══██╗██╔══██║██╔══╝░░██╔══╝░░
██████╔╝███████╗██║░░██║██║░░██║██████╔╝██║░░██║███████╗███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝
"""
error = """
░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ 
░█▀▀▀ ░█▄▄▀ ░█▄▄▀ ░█──░█ ░█▄▄▀ 
░█▄▄▄ ░█─░█ ░█─░█ ░█▄▄▄█ ░█─░█
"""

#======================================================================================================

def printcenter(text):
    size = shutil.get_terminal_size().columns
    for line in text.split("\n"):
        print(' ' * (round((size/2)-len(line)/2)), line)

#======================================================================================================

def bruteforce(hash, salt):
    if len(hash) == 64:
        for password in words:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if password_hash == hash:
                return password
    elif len(hash) == 86 or len(hash) == 85:
        parts = hash.split("$")
        salt1 = parts[2]
        hash1 = parts[3]
        for word in words:
            var2 = hashlib.sha256(word.encode()).hexdigest()
            final = hashlib.sha256((var2 + salt1).encode()).hexdigest()
            if final == hash1:
                return word
    elif len(hash) == 128:
        for word in words:
            var2 = hashlib.sha512(word.encode()).hexdigest()
            final = hashlib.sha512((var2 + salt).encode()).hexdigest()
            if final == hash:
                return word
    elif "SHA256" in hash:
        parts = hash.split("$")
        salt = parts[1]
        wow = parts[2]
        for word in words:
            word_hash = hashlib.sha256(hashlib.sha256(word.encode()).hexdigest().encode() + salt.encode()).hexdigest()
            if word_hash == wow:
                return word
    elif "SHA512" in hash:
        parts = hash.split("$")
        salt = parts[1]
        wow = parts[2]
        for word in words:
            passenc = hashlib.sha512(word.encode()).hexdigest()
            word_hash = hashlib.sha512((passenc + salt).encode()).hexdigest()
            if word_hash == wow:
                return word
    return hash

#======================================================================================================

def main():
    os.system("cls || clear")
    print()
    printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
    print()
    wordlist = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Wordlist file name {Fore.LIGHTBLACK_EX}(Including format): {Fore.RESET}")
    if not os.path.isfile(wordlist):
        os.system("cls || clear")
        printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
        print()
        printcenter(f"{Fore.RED}ERROR: {Fore.RESET}File not found / invalid format.\n\nRead README.MD for help")
        time.sleep(5)
        print()
        main()
    else:
        os.system("cls || clear")
        printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
        print()
        printcenter(f"{Fore.RESET}Valid file.\n\n{Fore.BLUE}   Processing wordlist...")
        print()
        with open(wordlist, 'r', encoding="latin-1") as f:
            lines = f.read().splitlines()
            words.update(lines)
            print(f"{Fore.LIGHTBLUE_EX}                             [LOG]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}{len(words)}{Fore.RESET} passwords have been uploaded from {Fore.LIGHTMAGENTA_EX}",wordlist,"", end="\r")
            print()
            print()
            while True:
                hash, salt = "", ""
                hash = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Enter hash: {Fore.RESET}")
                print()
                salt = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Enter salt{Fore.LIGHTBLACK_EX} (optional): {Fore.RESET}")
                print()
                printcenter(f"{Fore.LIGHTMAGENTA_EX}Decrypting...")
                startTime = time.time()
                final = bruteforce(hash, salt)
                if final == hash:
                    endTime = time.time()
                    totalTime = (endTime - startTime)
                    totalTime = round(totalTime, 3)
                    os.system("cls || clear")
                    printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.RESET} It was not possible to decrypt the hash.")
                    print()
                    print(f"{Fore.LIGHTBLACK_EX}                                        Response time:",totalTime,"seconds.")
                    ####
                    print()
                    print(f"{Fore.LIGHTBLUE_EX}(1) {Fore.RESET}Go back")
                    print(f"{Fore.LIGHTBLUE_EX}(2) {Fore.RESET}Leave")
                    print()
                    option = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Select ant option: {Fore.RESET}")
                    if option == "1":
                        main()
                    elif option == "2":
                        os.system("cls || clear")
                        print("Closing terminal...")
                        time.sleep(2)
                        exit()
                    else:
                        os.system("cls || clear")
                        printcenter(f"{Fore.LIGHTMAGENTA_EX}{error}")
                        printcenter(f"{Fore.RESET}You must select a valid option!")
                        time.sleep(3)
                        main()
                    ####
                if final != hash:
                    endTime = time.time()
                    totalTime = (endTime - startTime)
                    totalTime = round(totalTime, 3)
                    os.system("cls || clear")
                    printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.RESET} Hash successfully decrypted!\n\nResult → {Fore.LIGHTMAGENTA_EX}{final}")
                    clipboard.copy(final)
                    print()
                    printcenter(f"{Fore.LIGHTBLACK_EX}Result copied to clipboard.")
                    print()
                    print(f"{Fore.LIGHTBLACK_EX}                                              Dehash in",totalTime,"seconds")
                    print()
                    print()
                    print(f"{Fore.LIGHTBLUE_EX}(1) {Fore.RESET}Go back")
                    print(f"{Fore.LIGHTBLUE_EX}(2) {Fore.RESET}Leave")
                    print()
                    option = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Select and option: {Fore.RESET}")
                    if option == "1":
                        main()
                    elif option == "2":
                        os.system("cls || clear")
                        print("Closing terminal...")
                        time.sleep(2)
                        exit()
                    else:
                        os.system("cls || clear")
                        printcenter(f"{Fore.LIGHTMAGENTA_EX}{error}")
                        printcenter(f"{Fore.RESET}You must select a valid option!")
                        time.sleep(3)
                        main()


#======================================================================================================

main()

#========================================       The end       =========================================
