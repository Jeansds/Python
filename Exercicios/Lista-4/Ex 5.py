import random

    
Total=0
Vidas=6        
i=0
Final=[]
vetor = ["maca", "laranja", "banana", "cereja"]
palavra=random.choice(vetor)

def Jogo(Vogal,Final):
    Contador=0
    for i in range(len(palavra)):
        if(Vogal==palavra[i] and Final[i]!=Vogal):
            Final[i]=palavra[i]
            Contador=Contador+1
    return Contador

for i in range(len(palavra)):
    Final.append("_")
    
while(i<6):
   print(Final)
   print(Vidas)
   Vogal=str(input("digite uma letra "))
   Chama=Jogo(Vogal,Final)
   if(Chama==0):
       Vidas=Vidas-1
   else:
       Total=Chama+Total
   if(Total==len(palavra)):
       print("voce ganhou e este foi o resultado:")
       print(Final)
       print(Vidas)
       break
   elif(Vidas==0):
       print("voce perdeu")
       print(palavra)
       break
   