import subprocess
from customlibs import PrintUtil
import random
import string

def test(data, expected):
    output, error = Execute('password2.py', input_data=data)
    output = removeInput(output).strip().split("\n")
    success = True
    for i in range(len(output)):
        if output[i] != expected[i]:
            if i == 0:
                print(f"\tUsername:  {data[i]:<20} Output:  {output[i]:<100} Expected: {expected[i]:<20}")
            else:
                print(f"\tPassword:  {data[i]:<20} Output:  {output[i]:<100} Expected: {expected[i]:<20}")
            success = False
    if success:
        print(f"✓\t\033[1mUsername\033[0m [{len(data[0])}]:\t{data[0]:<20} \033[1mPassword\033[0m [{len(data[1])}]:\t{data[1]:<30} \033[1mOutput:\033[0m [1] {output[0][:6]}...{output[0][-20:]}... [2] {output[1][:6]}...{output[1][-20:]}..")

def removeInput(output:str) -> str:
    return output.split(":")[2][1:]

def Execute(file, input_data:list) -> tuple[str, str]:
    # Call the other Python program and capture its output
    process = subprocess.Popen(['python3', 'password2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    

    process.stdin.write(input_data[0] + "\n")
    process.stdin.write(input_data[1] + "\n")
    process.stdin.flush()

    output, error = process.communicate()

    return [output, error]



expectedSuccess = [
    "Thank you for following the security policy for user name length", 
    "Thank you for following the security policy for password name length"
]

expectedFailureUser = [
    "Username cannot be shorter than 5 characters.", 
    "Username cannot be longer than 10 characters."
]
expectedFailurePass = [
    "Password cannot be shorter than 5 characters.", 
    "Password cannot be longer than 10 characters."
]

total = 0
tests = [
    [["123456", "123456"], expectedSuccess],
    [["Stryker", "supercool"], expectedSuccess],
    [["", ""], [expectedFailureUser[0], expectedFailurePass[0]]],
    # [["", ""], expectedSuccess],
]

print(PrintUtil.line(200))
print("Manual Input")
for i in range(len(tests)):
    test(tests[i][0], tests[i][1])
    total += 1


print(PrintUtil.line(200))
print("⋆ Valid Input")

for i in range(20):
    # Define the length of the random string
    length1 = random.randint(5, 10)
    length2 = random.randint(5, 10)

    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length1))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length2))
    
    test([username, password], expectedSuccess)
    total += 1

print(PrintUtil.line(200))
print("⋆ Invalid Username")

for i in range(5):
    # Define the length of the random string
    length1 = random.randint(0, 4)
    length2 = random.randint(5, 10)

    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length1))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length2))
    
    test([username, password], [expectedFailureUser[0], expectedSuccess[1]])
    total += 1

for i in range(5):
    # Define the length of the random string
    length1 = random.randint(11, 20)
    length2 = random.randint(5, 10)

    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length1))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length2))
    
    test([username, password], [expectedFailureUser[1], expectedSuccess[1]])
    total += 1


print(PrintUtil.line(200))
print("⋆ Invalid Password")

for i in range(5):
    # Define the length of the random string
    length2 = random.randint(0, 4)
    length1 = random.randint(5, 10)

    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length1))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length2))
    
    test([username, password], [expectedSuccess[0], expectedFailurePass[0]])
    total += 1

for i in range(5):
    # Define the length of the random string
    length2 = random.randint(11, 20)
    length1 = random.randint(5, 10)

    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length1))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length2))
    
    test([username, password], [expectedSuccess[0], expectedFailurePass[1]])
    total += 1
    
print(PrintUtil.line(200))
print("⋆ Invalid Username and Password")
    
for i in range(20):
    # Define the length of the random string
    length2 = random.randint(11, 20)
    length1 = random.randint(11, 20)

    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length1))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length2))
    
    test([username, password], [expectedFailureUser[1], expectedFailurePass[1]])
    total += 1


print(PrintUtil.line(200))
print(f"✔  {total} Tests Complete\n")
