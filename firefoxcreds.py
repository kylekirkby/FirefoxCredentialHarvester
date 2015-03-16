import os, platform, sqlite3, getpass

#http://kb.mozillazine.org/Profile_folder_-_Firefox
#http://www.example-code.com/python/crypt2_3des.asp
#http://stackoverflow.com/questions/2435283/using-des-3des-with-python
#http://tipstrickshack.blogspot.co.uk/2013/09/extract-decrypt-passwords-from-firefox.html

PLATFORM = platform.system()
RELEASE  = platform.release()
VERSION  = platform.version()

if PLATFORM == "Windows":
    
    if RELEASE.lower() == "xp":
        pass
    else:
        username = getpass.getuser()
        base_profile_path  = "C:\\Users\\" + username +  "\\AppData\\Roaming\\Mozilla\\Firefox\\"
    
elif PLATFORM == "Linux":
    #Get the users current home folder path if using unix based system.
    base_path = os.path.expanduser("~")
    base_profile_path = base_path + "/.mozilla/firefox/"

#Get the users default profile folder
    
def getProfileFolder(path):
    
    directories  = os.listdir(path)
    
    for folder in directories:
        if os.path.isdir(folder):
            print(folder)



