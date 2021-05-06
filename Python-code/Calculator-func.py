"Nama   : Muhammad Aris Septanugroho"
"Kelas  : X SIJA 1"

# Make a function / method to perform simple calculator task

# Make sure you know, there is some parts when we create a function
# 1. Name function
# 2. Parameters (it's optional)
# 3. Function's body (here is your code will writen)

# how many number would you sum / distract / multiple / divide

# 'n' is parameter that presents how many number will be sumed / distracted / multipled / divided

def penjumlahan(n):
    result = int(input('Input first number will you sum : '))
    for _ in range(n-1):
        x = int(input('Input number will you sum : '))
        result += x
    print(result)

def pengurangan(n):
    result = int(input('Input first number will you distract : '))
    for _ in range(n-1):
        x = int(input('Input number will you distract : '))
        result -= x
    print(result)

def pembagian(n):
    result = int(input('Input first number will you divide : '))
    for _ in range(n-1):
        x = int(input('Input number will you divide : '))
        result /= x
    print(result)

def perkalian(n):
    result = int(input('Input first number will you multiple : '))
    for _ in range(n-1):
        x = int(input('Input number will you multiple : '))
        result *= x
    print(result)

def modulus(n):
    result = int(input('Input first number will you modulo : '))
    for _ in range(n-1):
        x = int(input('Input number will you modulo : '))
        result %= x
    print(result)

def exponential(n):
    result = int(input('Input first number will you exponenting : '))
    for _ in range(n-1):
        x = int(input('Input number will you exponenting : '))
        result **= x
    print(result)


def rounding(n):
    result = int(input('Input number will you rounding : '))
    for _ in range(n-1):
        x = int(input('Input number will you rounding : '))
        result //= x
    print(result)

def calculatorGenerator():
    try : 
        act = int(input('What will you do? \n1. Sum\n2. Distract\n3. Multiple\n4. Divide\n5. Modulo\n6. Exponents\n7. Rounding\n >> '))
    except : 
        print('Input Number, Don\'t string!' )
        return None
    
    if act == 1:
        second = int(input('Input how many number will you sum : '))
        penjumlahan(second)
    if act == 2:
        second = int(input('Input how many number will you Distract : '))
        pengurangan(second)
    if act == 3:
        second = int(input('Input how many number will you Multiple : '))
        perkalian(second)
    if act == 4:
        second = int(input('Input how many number will you Divide : '))
        pembagian(second)
    if act == 5:
        second = int(input('Input how many number will you Modulo : '))
        modulus(second)
    if act == 6:
        second = int(input('Input how many number will you Exponents : '))
        exponential(second)
    if act == 7:
        second = int(input('Input how many number will you Rounding : '))
        rounding(second)

calculatorGenerator()