n=5

#primaide centrada
#for  i in range (1, n +1 ):
#espacios = " " * (n-1)
#estrellas = "*" * (2 * i -1)
#print (espacios + estrellas)  

#diamante centrada completa (diamante simétrico en el eje x)
for i in range(1, n + 1):
    espacios = " " * (n - i)
    estrellas = "*" * (2 * i - 1)
    print(espacios + estrellas)

for i in range(n - 1, 0, -1): # en vez que sea una sumatoria se reduce para formar 
    espacios = " " * (n - i) # hasta que tienda a 1 formando asi el triangulo
    estrellas = "*" * (2 * i - 1)
    print(espacios + estrellas)