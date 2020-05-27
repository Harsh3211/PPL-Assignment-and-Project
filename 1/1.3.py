#Build an application that can be used to block certain websites from opening.


hosts_path =r"C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
websites = []


#Get websites to block
while True:
	if(int(input("Press 1 to add websites to list else enter 0:\t"))):
		website = str(input("Enter the website:\t"))
		websites.append(website)
	else:
		break
print("Websites in input are:")
for x in websites:
	print(x+",")


#Action you want to perform
print("Action you want to perform\n")
flag = str(input("Press 1. to block or Press 2. to unblock:\t"))
print('Flag is set to '+flag+'\n')


#Blocker
if flag == '1' :
    with open(hosts_path,'r+') as file:
        content = file.read()
        for website in websites:
            if website in content:
                pass
            else:
                file.write(redirect+' '+website+'\n')
#		print("Blocked Websites")

#Unblocker
elif flag == '2':
    with open(hosts_path,'r+') as file:
        content = file.readlines()
        file.seek(0)
		#print("Website Unblocked!!")
        for line in content:
            if not any(website  in line for website in websites):
                file.write(line)
            file.truncate()

else:
	print("Try Again! with proper input")

"""

# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost


"""
