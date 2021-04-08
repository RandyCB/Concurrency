import subprocess


"""
Description:
	The file shows the usage of subprocess module for scripting with python
	executing a linux command that displays  the ip address of the current machine

subprocess arguments:
        <subprocess variable>.<stdout|stderr|args|returncode>
        capture_output=True sets std(1,2) to the subprocess pipe instead of the shell
        text=True sets the std(1,2) text to be a string instead of a collection of bytes
        stdout=subprocess.PIPE redirects stdout 
        check=True shows if the external cmd failed into the python shell
        stderr=subprocess.DEVNULL ignores the errors for external cmds
        input=<subprocess variable>.stdout takes input from a different variable of type subprocess

Notes:
	for windows cmds the arg shell=True is mandatory since cmds are built in the shell and won't work otherwise
	the shell=True is not recommended when dealing with user input since it may cause harm to the OS 

"""



#subprocess.run('ls')
#subprocess.run('ls -la', shell=True)
#subprocess.run(['ls',' -la'])
#p = subprocess.run(['ls', '-la'], capture_output=True, text=True)
#print(p.stdout)


subprocess.run("ifconfig | grep broadcast | awk '{print $2}' ",shell=True)





