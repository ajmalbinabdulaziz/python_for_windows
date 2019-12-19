import subprocess

#this file("path.txt") contains the ip address of the remote machine and the respected shared folder in it.
#The syntax of the shared path is "\\\\192.168.3.182\\SF32" where SF32 is the shared folder name with full access to everyone 
shared_path = "C:\\Users\\admin\\Desktop\\path.txt"

#the file which is to be deployed into the corresponding remote machines
file_path = "D:\\pscp.exe"   


#this code snipet loops into every remote machines and mounts the shared folder into the master machine then copies, unmounts.
with open(shared_path) as f:
    for line in f:
        addr = line.strip() 

        subprocess.run(["net", "use", "X:", addr], capture_output = True, shell=True)
        subprocess.run(["copy", file_path, "x:"], capture_output = True, shell=True)
        subprocess.run(["net","use", "x:", "/delete"], capture_output = True, shell=True)
        
