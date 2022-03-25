letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
llaves=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25]

#texto de prueba
plainText=(input("ingrese un mensaje: "))

# se convierte el string en arreglo
plainText = list(plainText)
cipherText = []
#for lectura de letras
textLength=len(plainText)

for x in range(0,textLength):
    for c in range(0,len(letras)):
        if plainText[x] == letras[c]:
            clave=llaves[c]
            if  c<clave : cipherText.insert(x,letras[c+clave]) 
            else:  cipherText.insert(x,letras[c-clave])

plainText="".join(plainText)
cipherText="".join(cipherText)

print("Plain text: ",plainText)
print("Cipher text: ",cipherText)
