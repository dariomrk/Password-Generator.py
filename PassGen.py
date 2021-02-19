#Import
from ast import literal_eval
from secrets import choice
from string import ascii_lowercase, ascii_uppercase,digits,punctuation
from time import sleep    

#Logo
def Logo():

    """Print ASCII art logo."""

    print("""
 ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗        ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
 ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗      ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
 ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║█████╗██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
 ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
 ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝      ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                                                        dariomrk@github - Version {}
    """.format(version))

def LogoMainMenu():

    """Print ASCII art main menu logo."""

    print("""
  __  __        _         __  __                 
 |  \/  | __ _ (_) _ _   |  \/  | ___  _ _  _  _ 
 | |\/| |/ _` || || ' \  | |\/| |/ -_)| ' \| || |
 |_|  |_|\__,_||_||_||_| |_|  |_|\___||_||_|\_,_|
                                                        
    """)

def LogoQuickPassword():

    """Print ASCII art quick password logo."""

    print("""
   ___         _      _     ___                                     _ 
  / _ \  _  _ (_) __ | |__ | _ \ __ _  ___ _____ __ __ ___  _ _  __| |
 | (_) || || || |/ _|| / / |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` |
  \__\_\ \_,_||_|\__||_\_\ |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|
                                                                      
    """)

def LogoPasswordGenerator():
    
    """Print ASCII art password generator logo"""

    print("""
  ___                                     _    ___                             _             
 | _ \ __ _  ___ _____ __ __ ___  _ _  __| |  / __| ___  _ _   ___  _ _  __ _ | |_  ___  _ _ 
 |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` | | (_ |/ -_)| ' \ / -_)| '_|/ _` ||  _|/ _ \| '_|
 |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|  \___|\___||_||_|\___||_|  \__,_| \__|\___/|_|  
                                                                                             
    """)

def LogoSettings():

    """Print ASCII art settings logo"""

    print("""
  ___       _    _    _                 
 / __| ___ | |_ | |_ (_) _ _   __ _  ___
 \__ \/ -_)|  _||  _|| || ' \ / _` |(_-<
 |___/\___| \__| \__||_||_||_|\__, |/__/
                              |___/     

    """)

def LogoAbout():

    """Print ASCII art about logo"""

    print("""
    _    _                _   
   /_\  | |__  ___  _  _ | |_ 
  / _ \ | '_ \/ _ \| || ||  _|
 /_/ \_\|_.__/\___/ \_,_| \__|
                              
    """)

#Options - Main Menu
def OptionsMainMenu():

    """Print Main Menu options"""

    print("Press 1 - Quick Password\nPress 2 - Password Generator\nPress 3 - Settings\nPress 4 - About\nPress 5 - Exit\n")

#Generates a password based on the provided parameters
def PassGen(Lenght, SettingLower, SettingUpper, SettingDigits, SettingSpecial):

    """Generates password based on the provided parameters"""

    # Lenght: int - Lenght of the generated password.
    # SettingLower: bool - Use lowercase ASCII letters.
    # SettingUpper: bool - Use uppercase ASCII letters.
    # SettingDigits: bool - Use digits.
    # SettingSpecial: bool - Use special characters.

    chars = ""
    password = ""

    if SettingLower:

        chars += ascii_lowercase

    if SettingUpper:

        chars += ascii_uppercase
        
    if SettingDigits:

        chars += digits

    if SettingSpecial:

        chars += punctuation
    
    for i in range(Lenght):

        password += choice(chars)
    
    return(password)

#Clear out the shell window
def ClearShell():

    """Clear out the shell window"""

    print("\n"*256)

#Check if file exists in the directory
def FileCheck(filename):

    """Check if file exists in the directory"""

    try:

        file = open(filename)
        flag = True

    except:

        flag = False
    
    return flag

#Get key value from a file
def GetValue(key,filename):

    """Get key value from a file"""

    file = open(filename,"r")
    content = file.read()
    content_dict = literal_eval(content)
    value = content_dict[key]
    file.close()
    return value

#Save key value to file
def WriteValue(key,value,filename):

    """Save key value to a file"""
    
    file = open(filename,"r")
    content = file.read()
    content_dict = literal_eval(content)
    file.close()
    content_dict[key] = value
    file = open(filename,"w")
    file.write(str(content_dict))
    file.close()     

#Main
main = True
while main:

    #Check for Settings.conf
    if FileCheck("Settings.conf"):

        print("Settings.conf is present.")
        print("Loading...")
        ClearShell()

    #Settings.conf missing error
    else:

        ClearShell()
        settings_error = {"Version":0.0,"CustomSettings":False,"SettingLower":True,"SettingUpper":True,"SettingDigits":True,"SettingSpecial":False,"Lenght":10,}
        file = open("Settings.conf","w")
        file.write( str(settings_error) )
        file.close()
        print("Error! No Settings.conf is present!\nProgram will be reset to default settings.\nContinuing in 3 seconds...")
        sleep(3)
        ClearShell()

    version = GetValue("Version","Settings.conf")

    #Menu
    while True:

        Logo()
        LogoMainMenu()
        OptionsMainMenu()
        MainMenuOption = input("Input here >>> ")

        #EasterEgg
        if MainMenuOption == "<3":

            print("""
            def love(name):
                if name == 'dario':
                    return 'Börk❤️'
            """)

        elif MainMenuOption == "5":

            main = False
            print("Exiting...")
            ClearShell()

            break

        #Check for multiple choices
        elif len(MainMenuOption) > 1:

            print("\nError: You can choose only 1 option! Continuing in 3 seconds...")
            sleep(3)
            ClearShell()
        
        #Check for invalid choice
        elif MainMenuOption not in "12345":

            print("\nError: This option is not specified! Continuing in 3 seconds...")
            sleep(3)
            ClearShell()
        
        else:

            print("\nSuccessfully selected option {}. Continuing...".format(MainMenuOption))
            sleep(1)
            ClearShell()

            break
    
    #Quick Password
    if MainMenuOption == "1":

        while True:
            
            #First use prompt
            if GetValue("CustomSettings","Settings.conf") == False:

                LogoQuickPassword()
                print("Notice!\nQuick Password has not been set up yet.\nYou can continue using default settings or quickly set up manual generation settings.\nDefault settings: Lenght: 10 >>> Lowercase ASCII, Uppercase ASCII, Digits.")
                print("\nPress 1 to use default settings\nPress 2 to setup Quick Password\nPress 3 to return to the Main Menu")
                QuickPasswordMenu = input("\nInput here >>> ")
                ClearShell()

                if len(QuickPasswordMenu) > 1:

                    print("\nError: You can choose only 1 option! Continuing in 3 seconds...")
                    sleep(3)
                    ClearShell()
                
                if QuickPasswordMenu not in "123":
                    
                    print("\nError: This option is not specified! Continuing in 3 seconds...")
                    sleep(3)
                    ClearShell()
                
                #Generate Password
                elif QuickPasswordMenu == "1":

                    LogoQuickPassword()
                    print("Quick Generation using default settings...")
                    print("\nGenerated password: ",PassGen(10,True,True,True,False))
                    input("\nPress any key to continue >>> ")
                    ClearShell()

                    break
                
                #Quick Password setup
                elif QuickPasswordMenu == "2":

                    while True:

                        while True:

                            ClearShell()
                            LogoQuickPassword()
                            Lenght = input("\nInput desired password lenght >>> ")
                            flag = True

                            for char in Lenght:

                                if char not in digits:

                                    flag = False
                            
                            if flag:

                                WriteValue("Lenght",int(Lenght),"Settings.conf")

                                break

                            else:

                                print("Error: Lenght can only be an integer! Continuing in 3 seconds...")
                                sleep(3)

                        while True:

                            ClearShell()
                            LogoQuickPassword()
                            Lower = input("\nLowercase:\nPress 1 to enable or press 2 to disable >>> ")

                            if len(Lower) > 1 or Lower not in "12":

                                print("Error: Invalid input! Continuing in 3 seconds...")
                                sleep(3)

                            else:

                                if Lower == "1":

                                    SettingLower = True

                                else:

                                    SettingLower = False

                                WriteValue("SettingLower",SettingLower,"Settings.conf")

                                break

                        while True:

                            ClearShell()
                            LogoQuickPassword()
                            Upper = input("\nUppercase:\nPress 1 to enable or press 2 to disable >>> ")

                            if len(Upper) > 1 or Upper not in "12":

                                print("Error: Invalid input! Continuing in 3 seconds...")
                                sleep(3)

                            else:

                                if Upper == "1":

                                    SettingUpper = True

                                else:

                                    SettingUpper = False

                                WriteValue("SettingUpper",SettingUpper,"Settings.conf")

                                break

                        while True:

                            ClearShell()
                            LogoQuickPassword()
                            Digits = input("\nDigits:\nPress 1 to enable or press 2 to disable >>> ")

                            if len(Digits) > 1 or Digits not in "12":

                                print("Error: Invalid input! Continuing in 3 seconds...")
                                sleep(3)

                            else:

                                if Digits == "1":

                                    SettingDigits = True

                                else:

                                    SettingDigits = False

                                WriteValue("SettingDigits",SettingDigits,"Settings.conf")

                                break

                        while True:

                            ClearShell()
                            LogoQuickPassword()
                            Special = input("\nSpecial:\nPress 1 to enable or press 2 to disable >>> ")

                            if len(Special) > 1 or Special not in "12":

                                print("Error: Invalid input! Continuing in 3 seconds...")
                                sleep(3)

                            else:

                                if Special == "1":

                                    SettingSpecial = True

                                else:

                                    SettingSpecial = False

                                WriteValue("SettingSpecial",SettingSpecial,"Settings.conf")

                                break

                        print("\nSaving Settings...")
                        WriteValue("CustomSettings",True,"Settings.conf")
                        sleep(3)

                        break

                #Return to Main Menu
                elif QuickPasswordMenu == "3":

                    print("Returning...")
                    sleep(1)

                    break

            else:

                #After Settings.conf have been written by the user
                ClearShell()
                LogoQuickPassword()
                print("Quick Generation using your personal settings...")
                Lenght = GetValue("Lenght","Settings.conf")
                SettingLower = GetValue("SettingLower","Settings.conf")
                SettingUpper = GetValue("SettingUpper","Settings.conf")
                SettingDigits = GetValue("SettingDigits","Settings.conf")
                SettingSpecial = GetValue("SettingSpecial","Settings.conf")
                print("\nGenerated password: ",PassGen(int(Lenght),SettingLower,SettingUpper,SettingDigits,SettingSpecial))
                input("\nPress any key to continue >>> ")

                break

            break

    #Password Generator
    elif MainMenuOption == "2":

        while True:

            LogoPasswordGenerator()
            Lenght = input("\nInput desired password lenght >>> ")

            flag = False

            for char in Lenght:

                if char not in digits:

                    flag = True
                
            if flag:

                print("Error: Lenght can only be an integer! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            else:

                break
        
        ClearShell()
        
        while True:

            LogoPasswordGenerator()
            Lower = input("\nLowercase:\nPress 1 to enable or press 2 to disable >>> ")

            if len(Lower) > 1 or Lower not in "12":

                print("Error: Invalid input! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            else:

                if Lower == "1":

                    SettingLower = True
                    break

                else:

                    SettingLower = False
                    break
        
        ClearShell()
            
        while True:

            LogoPasswordGenerator()
            Upper = input("\nUppercase:\nPress 1 to enable or press 2 to disable >>> ")

            if len(Upper) > 1 or Upper not in "12":

                print("Error: Invalid input! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            else:

                if Upper == "1":

                    SettingUpper = True
                    break

                else:

                    SettingUpper = False
                    break
        
        ClearShell()
        
        while True:

            LogoPasswordGenerator()
            Digits = input("\nDigits:\nPress 1 to enable or press 2 to disable >>> ")

            if len(Digits) > 1 or Digits not in "12":

                print("Error: Invalid input! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            else:

                if Digits == "1":

                    SettingDigits = True
                    break

                else:

                    SettingDigits = False
                    break
        
        ClearShell()
        
        while True:

            LogoPasswordGenerator()
            Special = input("\nSpecial:\nPress 1 to enable or press 2 to disable >>> ")

            if len(Special) > 1 or Special not in "12":

                print("Error: Invalid input! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            else:

                if Special == "1":

                    SettingSpecial = True
                    break

                else:

                    SettingSpecial = False
                    break
        
        ClearShell()
        LogoPasswordGenerator()
        print("\nGenerated password: ",PassGen(int(Lenght),SettingLower,SettingUpper,SettingDigits,SettingSpecial))
        input("\nPress any key to continue >>> ")

    #Settings
    elif MainMenuOption == "3":

        while True:

            ClearShell()
            
            LogoSettings()
            print("\nPress 1 to show current Quick Password settings\nPress 2 to reset Quick Password settings\nPress 3 to return to the Main Menu")
            SettingsMenu = input("\nInput here >>> ")

            if len(SettingsMenu) > 1:

                print("\nError: You can choose only 1 option! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            elif SettingsMenu not in "123":

                print("\nError: This option is not specified! Continuing in 3 seconds...")
                sleep(3)
                ClearShell()

            elif SettingsMenu == "1":
                
                ClearShell()
                LogoSettings()
                print("\nCurrent Quick Password settings are:")
                print("\nPassword Lenght: ", GetValue("Lenght","Settings.conf"))
                print("Lowercase characters: ",GetValue("SettingLower","Settings.conf"))
                print("Uppercase characters: ",GetValue("SettingUpper","Settings.conf"))
                print("Digits: ",GetValue("SettingDigits","Settings.conf"))
                print("Special characters: ",GetValue("SettingSpecial","Settings.conf"))
                input("\nPress any key to continue >>> ")
                continue

            elif SettingsMenu == "2":

                while True:

                    ClearShell()
                    LogoSettings()
                    print("\nWarning! Resetting the Quick Password settings cannot be undone\n\nPress 1 to reset Quick Password settings\nPress 2 to Cancel")
                    
                    ResetMenu = input("\nInput here >>> ")

                    if len(ResetMenu) > 1:
                        print("\nError: You can choose only 1 option! Continuing in 3 seconds...")
                        sleep(3)
                        ClearShell()
                        continue

                    elif ResetMenu not in "12":
                        print("\nError: This option is not specified! Continuing in 3 seconds...")
                        sleep(3)
                        ClearShell()
                        continue
                    
                    break

                if ResetMenu == "1":

                    ClearShell()
                    LogoSettings()
                    print("\nResetting! Continuing in 3 seconds...")
                    settings_reset = {"Version":version,"CustomSettings":False,"SettingLower":True,"SettingUpper":True,"SettingDigits":True,"SettingSpecial":False,"Lenght":10,}
                    file = open("Settings.conf","w")
                    file.write( str(settings_reset) )
                    file.close()
                    sleep(3)

                elif ResetMenu == "2":

                    ClearShell()
                    continue
                
                break

            elif SettingsMenu == "3":

                print("Returning...")
                sleep(1)
                break

    #About
    elif MainMenuOption == "4":

        LogoAbout()
        print("\nVersion: {}\nAuthor: dariomrk@github\nGithub link: https://github.com/dariomrk/Password-Generator".format(version))
        input("\nPress any key to continue >>> ")
