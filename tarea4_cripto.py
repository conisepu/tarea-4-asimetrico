import os, sys, time
import subprocess
import hashlib


    
# #####################################################################
def leer_texto_claro(num):
    hash = list()
    texto_claro = list()
    file = open('C:/tarea4/cracked/crack_'+ num +'.txt', 'r')
    if(num == "1"):
        for hash_texto in file:
            texto_claro.append(hash_texto[33:len(hash_texto)-1])
        return (texto_claro)
    elif(num == "2"):
        for hash_texto in file:
            texto_claro.append(hash_texto[50:len(hash_texto)-1])
        return (texto_claro)
    elif(num == "3"):
        char = 0
        indice_dos_puntos  = 0 #auxiliar que observa : y espacios
        password = ""
        for hash_texto in file:
            while char < len(hash_texto):
                if (indice_dos_puntos  == 2):
                    password += hash_texto[char]
                if (hash_texto[char] == ":"):
                    indice_dos_puntos  += 1
                char += 1
            texto_claro.append(password)
            password = ""
            indice_dos_puntos  = 0
            char = 0
        return (texto_claro)
    elif(num == "4"):
        for hash_texto in file:
            texto_claro.append(hash_texto[33:len(hash_texto)-1])
        return (texto_claro)
    elif(num == "5"):
        for hash_texto in file:
            indice_dos_puntos = hash_texto.index(':')
            texto_claro.append(hash_texto[indice_dos_puntos+1:len(hash_texto)-1])
        return (texto_claro)

def sha512(txt_claro):
    s = hashlib.sha3_512()
    list_sha512 = list()
    for pwd in txt_claro:
        s.update(pwd.encode('utf-8'))
        list_sha512.append(s.hexdigest()) 
    return(list_sha512)



# ####################ARCHIVO 1#########################
# timeINIT_hash = time.time()
# os.system("hashcat.exe -m 0 -a 0 -D 2 -o C:/tarea4/cracked/crack_1.txt C:/tarea4/hash/archivo_1 C:/tarea4/diccionario_1.dict C:/tarea4/diccionario_2.dict --potfile-disable")
# timeEND_hash = time.time()
# tiempo_hash1= timeEND_hash - timeINIT_hash
# txt_claro_1 = leer_texto_claro("1")
# print("lista de password archivo 1",txt_claro_1)
# print("\n\n\n\ntiempo que se demoro en crackear el archivo 1 ", tiempo_hash1)

# timeINIT_sha512 = time.time()
# list_sha512_1 = sha512(txt_claro_1)
# timeEND_sha512 = time.time()
# tiempo_sha5121= timeEND_sha512 - timeINIT_sha512
# print(list_sha512_1)
# print("\n\n\n\ntiempo que se demoro en hashear con sha512 el archivo 1", tiempo_sha5121)


# #################ARCHIVO 2############################
# timeINIT_hash = time.time()
# os.system("hashcat.exe -m 10 -a 0 -D 2 -o C:/tarea4/cracked/crack_2.txt C:/tarea4/hash/archivo_2 C:/tarea4/diccionario_1.dict C:/tarea4/diccionario_2.dict --potfile-disable")
# timeEND_hash = time.time()
# tiempo_hash2= timeEND_hash - timeINIT_hash
# txt_claro_2 = leer_texto_claro("2")
# print("lista de password archivo 2",txt_claro_2)
# print("tiempo que se demoro en crackear el archivo 2", tiempo_hash2)

# timeINIT_sha512 = time.time()
# list_sha512_2 = sha512(txt_claro_2)
# timeEND_sha512 = time.time()
# tiempo_sha5122= timeEND_sha512 - timeINIT_sha512
# print(list_sha512_2)
# print("tiempo que se demoro en hashear con sha512 el archivo 2", tiempo_sha5122)


# ################ARCHIVO 3##############################
# timeINIT_hash = time.time()
# os.system("hashcat.exe -m 10 -a 0 -D 2 -o C:/tarea4/cracked/crack_3.txt C:/tarea4/hash/archivo_3 C:/tarea4/diccionario_1.dict C:/tarea4/diccionario_2.dict --potfile-disable")
# timeEND_hash = time.time()
# tiempo_hash3= timeEND_hash - timeINIT_hash
# txt_claro_3 = leer_texto_claro("3")
# print("lista de password archivo 3",txt_claro_3)
# print("tiempo que se demoro en crackear el archivo 3", tiempo_hash3)

# timeINIT_sha512 = time.time()
# list_sha512_3 = sha512(txt_claro_3)
# timeEND_sha512 = time.time()
# tiempo_sha5123= timeEND_sha512 - timeINIT_sha512
# print(list_sha512_3)
# print("tiempo que se demoro en hashear con sha512 el archivo 3", tiempo_sha5123)


# ###############ARCHIVO 4##############################
# timeINIT_hash = time.time()
# os.system("hashcat.exe -m 1000 -a 0 -D 2 -o C:/tarea4/cracked/crack_4.txt C:/tarea4/hash/archivo_4 C:/tarea4/diccionario_1.dict C:/tarea4/diccionario_2.dict --potfile-disable")
# timeEND_hash = time.time()
# tiempo_hash4= timeEND_hash - timeINIT_hash
# txt_claro_4 = leer_texto_claro("4")
# print("lista de password archivo 4",txt_claro_4)
# print("tiempo que se demoro en crackear el archivo 4", tiempo_hash4)

# timeINIT_sha512 = time.time()
# list_sha512_4 = sha512(txt_claro_4)
# timeEND_sha512 = time.time()
# tiempo_sha5124= timeEND_sha512 - timeINIT_sha512
# print(list_sha512_4)
# print("tiempo que se demoro en hashear con sha512 el archivo 4", tiempo_sha5124)


# ################ARCHIVO 5#############################
timeINIT_hash = time.time()
os.system("hashcat.exe -m 1800 -a 0 -D 2 -o C:/tarea4/cracked/crack_5.txt C:/tarea4/hash/archivo_5 C:/tarea4/diccionario_1.dict C:/tarea4/diccionario_2.dict --potfile-disable")
timeEND_hash = time.time()
tiempo_hash5= timeEND_hash - timeINIT_hash
txt_claro_5 = leer_texto_claro("5")
print("lista de password archivo 5",txt_claro_5)
print("tiempo que se demoro en crackear el archivo 5", tiempo_hash5)

timeINIT_sha512 = time.time()
list_sha512_5 = sha512(txt_claro_5)
timeEND_sha512 = time.time()
tiempo_sha5125 = timeEND_sha512 - timeINIT_sha512
print(list_sha512_5)
print("tiempo que se demoro en hashear con sha512 el archivo 5", tiempo_sha5125)


