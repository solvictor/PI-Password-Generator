import itertools as it
import time  
import os
  
start_time = time.time()  
infos = {"Name": "", "Surname": "", "Birthday": ""}

def saveToTxt(liste: list, filepath: str, filename: str):
    """Save a list to a txt file

    Args:
        liste (list): list to be exported
        filepath (str): filepath of where you want the list to be saved
        filename (str): name of the file
    """
    with open(filepath + filename + ".txt", "w") as outfile:
        outfile.write("\n".join(liste))
        print(f"Passwords successfully exported to : {filepath}{filename}.txt")

def askInfos(liste: dict):
    """Ask all infos to the user

    Args:
        liste (dict): dictionnary containing the wanted infos
    """
    for info in liste:
        if info == "Birthday":
            givenInfo = input(f"Enter info : {info} (DD/MM/YYYY)\n")
        else:
            givenInfo = input(f"Enter info : {info}\n")
        liste[info] = givenInfo

def allStrings(string: str):
    """Generate a list of all possibilit of a given string

    Args:
        string (str): given string

    Returns:
        (list): list of all generated strings
    """
    lu_sequence = ((c.lower(), c.upper()) for c in string)
    return [''.join(x) for x in it.product(*lu_sequence)]

def birthdaySeparator(birthday: str):
    """Seperate infos from a birthday string

    Args:
        birthday (str): birthday string

    Returns:
        (list): day, month and year of birth
    """
    birthdayList = list(birthday)
    day = birthdayList[0] + birthdayList[1]
    month = birthdayList[3] + birthdayList[4]
    year = birthdayList[6] + birthdayList[7] + birthdayList[8] + birthdayList[9]
    return day, month, year

def passwords(infos: dict):
    """Generate passwords from the given infos

    Args:
        infos (dict): dictionnary containing the infos

    Returns:
        (list): list containing the passwords
    """
    passwordsList = []
    for info in infos:
        if not info == "Birthday":
            for x in range(len(allStrings(infos[info]))):
                passwordsList.append(allStrings(infos[info])[x])                    
        else:
            # Name + birthday
            for noms in allStrings(infos["Name"]):
                noms = noms + birthdaySeparator(infos[info])[2]
                passwordsList.append(noms)
            # Surname + birthday  
            for prenom in allStrings(infos["Surname"]):
                prenom = prenom + birthdaySeparator(infos[info])[2]
                passwordsList.append(prenom)    
                 
    return passwordsList        
            
#askInfos(infos)
print("""
    ____  ____     ____                  ______         
   / __ \/  _/    / __ \____ ___________/ ____/__  ____ 
  / /_/ // /_____/ /_/ / __ `/ ___/ ___/ / __/ _ \/ __ \\
 / ____// /_____/ ____/ /_/ (__  |__  ) /_/ /  __/ / / /
/_/   /___/    /_/    \__,_/____/____/\____/\___/_/ /_/ 
                                                        """)

print(passwords({"Name": "Name", "Surname": "Surname", "Birthday": "19/01/2000"}))

interval = time.time() - start_time  
print(f'\nTotal time in seconds: {interval}')

filename = input("Enter name of the output file :\n")
path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + "\\passLists\\"
if not os.path.exists(path):
    os.makedirs(path)

saveToTxt(passwords({"Name": "Name", "Surname": "Surname", "Birthday": "19/01/2000"}), path, filename)
