# assignment2
A password cracker in Linux that will use a dictionary text file to check for the password of certain users.

Here is my shadow password cracker but let me help you use it.

First lets get started by placing the passcrack.py file and the dict.txt in the same place.
-The diction.txt file will be your dictionary file that you put a whole bunch of random words. You can also download this from online but I made mine.

Once they are in the same area you need to open up your handy dandy terminal and type the below commands (assuming these 2 files are in your documents folder)
cd Documents
sudo python passcrack.py -f /etc/shadow

Now it should be all good and based on what is in your dictionary file you will get the passwords for all users.
Enjoy cracking the passwords.

Also! I have included the dictionary.txt file just incase you need one quick!
