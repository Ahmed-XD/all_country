import os, platform

 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        
 
 
 
elif bit == "32bit":
 
        from ET32 import void
 
 
        void()
 
