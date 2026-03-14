#triangulo de asteriscos

n = 5

for i in range (1, n +1):

    print("*" * i) 

  # *
  # **
  # ***
  # ****
  # *****


  #triangulo invertido 
for i in range ( n, 0, -1):
    print ("*" * i)

#primaide centrada
for  i in range (1, n +1 ):
    espacios = " " * (n-1)
    estrellas = "*" * (2 * i -1)
    print (espacios + estrellas)  