# to use md5() function, I need to import hashlib
# pip3 install hashlib
import hashlib

# "input" function
# https://linuxhint.com/python_user_input/
print("\n\n*------------------*--------------------*")
your_password = input("To complete the challenge, you must input the correct password: ")
 
password_check = True

# "len()" function
# https://www.tutorialspoint.com/find-length-of-a-string-in-python-3-ways
if(len(your_password) == 10):
	print("\nPassword length check: OK")
else:
	print("\nPassword length check: ERROR")
	password_check = False

print("\nYou submitted the following password:", your_password)

# the real password encrypted with md5 algorithm
real_password_md5 = "8bd4df69ed228fc6dea0e6d3012f478e"
# the submitted password, being encrypted with some misterious md5 magic you don't have to know
# please mr hacker, don't emulate this in your own code
# TODO: delete the sarcastic comment above, it could be an easy hint for hacker
your_password_md5 = hashlib.md5(your_password.encode('utf-8')).hexdigest()

# I'm so smart, and hackers are just brutes
# There's no way to find the real password
# There's no way to use a beginner method to crack it
# Hehehe good luck!
if(your_password_md5 == real_password_md5):
	print("\n<<Congratulations! You've found the correct password!>>")
	print("\n<<Feel free to brag about it!>>")
else:
	if (password_check):
		print("\n<<Developer Notes: Dear myself, looks like you forgot the password again.>>")
		print("\n<<Maybe check the code here: >>")
		print("\n<<TODO: remove this message later>>")
	else:
		print("\n<<Haha it will be years before you can face me!>>")
		print("\n<<Don't make me use my kill move!>>")
print("\n*------------------*--------------------*\n\n")