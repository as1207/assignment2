import os,sys,crypt,argparse 
os.system('clear')

def findPass(cryptPass,user):
	dictionFile = open ('diction.txt','r')
	ctype = cryptPass.split("$")[1]
	found = False
	salt = cryptPass.split ("$")[2]
	insalt= "$" + ctype + "$" + salt + "$"
	for word in dictionFile.readlines():
		word= word.strip('\n')
		cryptWord = crypt.crypt(word,insalt)
		if( cryptWord == cryptPass):
			found= True
				
			print "[*]YAY! Found password for: " + user + " || and the password is... " + word
			
	if ( found == False): 
		print "[*]DARN! Password not found in dictionary."

	print "--------------------------------------------------------------------"
			
			
exit	

def main(): 
	found = False
	userInput = argparse.ArgumentParser(description='Linux Password Cracker')
   	userInput.add_argument('-f', action='store', dest='path', help='Path to shadow file, \'/etc/shadow\'')
   	shadPath=userInput.parse_args()
   	if shadPath.path == None:
		userInput.print_help()
        
   	else:
		passFile = open (shadPath.path,'r')
         	for line in passFile.readlines():
			line = line.replace("\n","").split(":")
           	  	if  not line[1] in [ 'x', '*','!' ]:
          	 		user = line[0]
           	  		cryptPass = line[1]
				print "[*] Lets crack the password for " + user
           	  		findPass(cryptPass,user)
			if(found == None or user == None):
				print "[*] User does not exist or user does not have a password."	
if __name__ == "__main__" :
	main()
	
