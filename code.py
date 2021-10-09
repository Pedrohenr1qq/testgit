def Fatorial(number,show=False):
   fact = 1
   for Cont in range(number,0,-1):
     if show == True:
       print (f"{Cont} x" ,end='')
     fact  *= Cont
   return fact 


n = int(input("Digite um numero para calcular o fatorial:"))
show = int(input("Quer mostar o calculo?Digite 0 para sim e 1 para nao: "))
if show == 0:
  print(Fatorial(n,True))
else:
 print(Fatorial(n))
