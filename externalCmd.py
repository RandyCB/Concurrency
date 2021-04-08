import subprocess


"""
Description:



subprocess arguments:
        <subprocess var>.<stdout|stderr|args|returncode>
        capture_output=True sets std(1,2) to the subprocess pipe instead of the sheell
        text=True sets the std(1,2) text to be a string instead of a collection of bytes
        stdout=subprocess.PIPE redirects stdout 
        check=True shows if the external cmd failed into the python shell
        stderr=subprocess.DEVNULL ignores the errors for external cmds
        input=<subprocess var>.stdout takes input from a different variable of type subprocess

Notes:
	

"""



#subprocess.run('ls')
#subprocess.run('ls -la', shell=True)
#subprocess.run(['ls',' -la'])
#p = subprocess.run(['ls', '-la'], capture_output=True, text=True)
#print(p.stdout)


subprocess.run("ifconfig | grep broadcast | awk '{print $2}' ",shell=True)





