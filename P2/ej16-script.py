import fileinput, sys, subprocess

inputfile = fileinput.FileInput("/etc/ssh/sshd_config", inplace = True)

for line in inputfile:

	sys.stdout.write(line.replace("PasswordAuthentication no", 
				      "PasswordAuthentication yes"))

inputfile.close()

subprocess.call(["sudo", "service", "ssh", "restart"])
print "Password access enabled"
subprocess.call(["sleep", "10"])

inputfile = fileinput.FileInput("/etc/ssh/sshd_config", inplace = True)

for line in inputfile:

	sys.stdout.write(line.replace("PasswordAuthentication yes", 
				      "PasswordAuthentication no"))

inputfile.close()

subprocess.call(["sudo", "service", "ssh", "restart"])
print "Password access disabled"