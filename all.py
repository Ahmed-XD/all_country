import os, platform
os.system('git pull')
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        os.system('chmod 777 a64');os.system('/a64')
 
 
 
elif bit == "32bit":
 
        print('32 bit not support')
 
