import pyautogui
from getpass import getpass
from os import system
from time import sleep

#getting info from the user

MICROSOFT_AND_GOOGLE_BROWSERS = ["chrome","google","edge","microsoft edge","opera","opera gx"]
browser_list = ["firefox","chrome","edge","google","microsoft edge, opera, opera gx"]
user = "N"

while user.upper() != "Y":
    system("cls")

    print("This program works mainly on windows, so keep that in mind.\n")
    browser_name = input("Insert you browser name (firefox, chrome, edge, opera):")

    if browser_name.lower() not in browser_list:
        system("cls")
        print("Insert a valid browser.\n")
        continue

    unimestre_name = input("\nInsert your registration number from unimestre:")
    unimestre_password = getpass("Insert you password from unimestre:")

    system("cls")

    institutional_email = input("\nInsert your institutional e-mail:")
    institutional_email_password = getpass("Insert your institutional e-mail password:")

    system("cls")

    personal_email = input("\nInsert your personal e-mail:")
    personal_email_password = getpass("Insert your personal e-mail password:")
    
    system("cls")

    github_email = input("\nInsert your github e-mail:")
    github_password = getpass("Insert your github password:")

    system("cls")
    print("This program works mainly on windows, so keep that in mind.\n")
    print(f"\nYour browser is {browser_name}\nUnimestre info: {unimestre_name},{unimestre_password}\nInstitutional email info: {institutional_email},{institutional_email_password}\nPersonal email info: {personal_email},{personal_email_password}\nGithub info: {github_email}")

    user = input("Is that info correct? (Y) or (N)")

system("cls")

pyautogui.alert("Please, don't touch in your keyboard and mouse while the program is running.")

pyautogui.PAUSE = 0.5

pyautogui.press("winleft")
pyautogui.write(browser_name)
pyautogui.press("enter")
sleep(1.5)

#Login into cesusc

#Open the right anonymous tab from each browser
if browser_name.lower() in MICROSOFT_AND_GOOGLE_BROWSERS:
    pyautogui.hotkey("ctrl","shift","n")

if browser_name.lower() == "firefox":
    pyautogui.hotkey("ctrl","shift","p")

sleep(1)
pyautogui.write("https://graduacao.cesusc.edu.br/projetos/nucleo/uteis/login.php?&tid=0&lid=0&pid=24&arq_ret=R5QT1WSRQBMCVQVPFFQSF99MCT5RT44Q9WRW0RBM0FMM5QQ4R4CV59RWRF1F5SWCW0")
pyautogui.press("enter")
sleep(2)
pyautogui.press("tab")
pyautogui.write(unimestre_name)
pyautogui.press("tab")
pyautogui.write(unimestre_password)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

#Open gmail
pyautogui.hotkey("ctrl","t")
pyautogui.write("gmail.com")
pyautogui.press("enter")
sleep(5)
pyautogui.write(institutional_email)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(2)
pyautogui.write(institutional_email_password)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(10)

pyautogui.PAUSE = 0.2

for i in range(0,11):
    pyautogui.press("tab")

pyautogui.PAUSE = 0.5

pyautogui.press("enter")

pyautogui.PAUSE = 0.2

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.PAUSE = 0.5

pyautogui.press("enter")

sleep(5)

pyautogui.PAUSE = 0.2

for i in range(0,21):
    pyautogui.press("tab")

pyautogui.PAUSE = 0.5

pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

sleep(3)

pyautogui.write(personal_email)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(1.5)
pyautogui.write(personal_email_password)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.hotkey("ctrl","t")
pyautogui.write("https://github.com/")
pyautogui.press("enter")
sleep(2)

pyautogui.PAUSE = 0.2
for i in range(0,8):
    pyautogui.press("tab")
pyautogui.PAUSE = 0.5

pyautogui.press("enter")
pyautogui.write(github_email)
pyautogui.press("tab")
pyautogui.write(github_password)
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.alert("You are good to go :)")

sleep(2)