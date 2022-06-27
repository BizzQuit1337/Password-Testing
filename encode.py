import random, sympy

prime1 = sympy.randprime(1, 100)
prime2 = sympy.randprime(1, 100)

shift2 = prime1 * prime2

def key_store(prime, file):
    file = file[:-4]
    file = file + '_key.txt'
    with open(file, 'w') as f:
        f.write(str(prime))

def listy(file, shift):
    listy.list = []
    with open(file, 'r') as f:
        for line in f:
            for charecter in line:
                listy.list.append((ord(charecter) + shift))

def lister(list):
    lister.new = []
    for charecter in list:
        lister.new.append(chr(charecter))
    

def save(file, list):
    encoded = []
    with open (file, 'a') as f:
        for charecter in list:
            ef = charecter.encode('utf-8')
            f.write(str(ef))

            
        
    
            

listy('passwords.txt', shift2)
lister(listy.list)
save('encoded_passwords.txt' , lister.new)
key_store(prime1, 'encoded_passwords.txt')