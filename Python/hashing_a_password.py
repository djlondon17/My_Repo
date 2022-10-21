from getpass import getpass as gp
from hashlib import md5

'''
password = gp("Enter your password: ")
encoded = password.encode("UTF-8")
hashed = md5(encoded)
hexed = hashed.hexdigest()
print(hexed)
'''

# password = md5(gp("Enter your password: ").encode("UTF-8")).hexdigest()
# print(password)

def passwd(prompt="Enter your password: "):
    return md5(gp(prompt).encode("UTF-8")).hexdigest()

pass1 = passwd()
pass2 = passwd("Confirm your password: ")
if pass1 == pass2:
    print(f"{pass1}\n{pass2}")
else:
    print("The passwords did not match.")