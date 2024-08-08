#======================================================================================================
#              Don't touch anything unless you know exactly what you're doing.
#======================================================================================================

import hashlib, time, os, shutil
import pyperclip as clipboard
from colorama import Fore

passwords = []

#======================================================================================================

logo = """
██████╗░███████╗██╗░░██╗░█████╗░░██████╗██╗░░██╗
██╔══██╗██╔════╝██║░░██║██╔══██╗██╔════╝██║░░██║
██║░░██║█████╗░░███████║███████║╚█████╗░███████║
██║░░██║██╔══╝░░██╔══██║██╔══██║░╚═══██╗██╔══██║
██████╔╝███████╗██║░░██║██║░░██║██████╔╝██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
"""


logo2 = """
║███████╗███████╗
║██╔════╝╚════██║
║█████╗░░░░███╔═╝
║██╔══╝░░██╔══╝░░
║███████╗███████╗
╚══════╝╚══════╝
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

def bruteforce(hash_str: str, salt: str = None):
    # SHA256
    if len(hash_str) == 64:
        for password in passwords:
            if hashlib.sha256(password.encode()).hexdigest() == hash_str:
                return password
            if salt is not None and (hashlib.sha256(password.encode() + salt.encode()).hexdigest() == hash_str or hashlib.sha256(hashlib.sha256(password.encode()).hexdigest().encode() + salt.encode()).hexdigest() == hash_str):
                return password
    # SHA512
    elif len(hash_str) == 128:
        for password in passwords:
            if hashlib.sha512(password.encode()).hexdigest() == hash_str:
                return password
            if salt is not None and (hashlib.sha512(password.encode() + salt.encode()).hexdigest() == hash_str or hashlib.sha512(hashlib.sha512(password.encode()).hexdigest().encode() + salt.encode()).hexdigest() == hash_str):
                return password
    return hash_str

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
        printcenter(f"{Fore.RED}ERROR: {Fore.RESET}File not found / invalid format.")
        printcenter(f"Read README.MD for help.")
        time.sleep(5)
        print()
        main()
    else:
        os.system("cls || clear")
        printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
        print()
        printcenter(f"{Fore.RESET}Valid file.")
        print()
        printcenter(f"{Fore.BLUE}Processing wordlist...")
        print()
        with open(wordlist, 'r', encoding="latin-1") as f:
            passwords.extend([password.strip() for password in f])
            printcenter(f"{Fore.LIGHTBLUE_EX}                    [LOG]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}{len(passwords)}{Fore.RESET} passwords have been uploaded from {Fore.LIGHTMAGENTA_EX}{wordlist}")
            print()
            print()
            while True:
                hash_str, salt = "", ""
                hash_str = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Enter hash: {Fore.RESET}")
                print()
                salt = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Enter salt{Fore.LIGHTBLACK_EX} (optional): {Fore.RESET}")
                print()
                printcenter(f"{Fore.LIGHTMAGENTA_EX}Decrypting...")
                startTime = time.time()
                final = bruteforce(hash_str, salt)
                endTime = time.time()
                totalTime = round((endTime - startTime), 3)

                if final == hash_str:
                    os.system("cls || clear")
                    printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.RESET} It was not possible to decrypt the hash.")
                    print()
                    printcenter(f"{Fore.LIGHTBLACK_EX}Response time: {totalTime} seconds.")
                    print()
                    print(f"{Fore.LIGHTBLUE_EX}(1) {Fore.RESET}Go back")
                    print(f"{Fore.LIGHTBLUE_EX}(2) {Fore.RESET}Leave")
                    print()
                    option = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Select an option: {Fore.RESET}")
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
                else:
                    os.system("cls || clear")
                    printcenter(f"{Fore.LIGHTBLUE_EX}{logo}")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.RESET} Hash successfully decrypted!\n\nResult → {Fore.LIGHTMAGENTA_EX}{final}")
                    clipboard.copy(final)
                    print()
                    printcenter(f"{Fore.LIGHTBLACK_EX}Result copied to clipboard.")
                    print()
                    printcenter(f"{Fore.LIGHTBLACK_EX}Dehash in {totalTime} seconds.")
                    print()
                    print()
                    print(f"{Fore.LIGHTBLUE_EX}(1) {Fore.RESET}Go back")
                    print(f"{Fore.LIGHTBLUE_EX}(2) {Fore.RESET}Leave")
                    print()
                    option = input(f"{Fore.LIGHTMAGENTA_EX} [»] {Fore.LIGHTBLUE_EX}Select an option: {Fore.RESET}")
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
