class parabola:
    
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None):
        if(tipo=="param"):
            self.__a = int(p1)  
            self.__b = int(p2)
            self.__c = int(p3)
  
        elif(tipo == "fuocoDiret"):
            self.__p1 = int(p1)
            self.__p2 = int(p2)  #xf
            self.__p3 = int(p3)
            
            self.__a = 1/(2*self.__p2 - 2*self.__p3)
            self.__b = -2*self.__a * self.__p1
            self.__c = (4*self.__p2*self.__a + self.__b*self.__b - 1)/(4*self.__a)

        
        
    def GetA(self):
        return self.__a
 
    def GetB(self):
        return self.__b

    def GetC(self):
        return self.__c

    def fuoco(self, asse_simmetria = "x"):
        if (asse_simmetria == "x"):
           x = (1) -pow((self.__b),2)+ (self.__a)*(self.__c)*4/4*(self.__a)
           y =  (-self.__b)/(self.__a)*2
          
           print("le coordinate del fuoco con asse parallelo all'asse x sono:")
           return round(x, 2), round(y, 2)

        elif (asse_simmetria == "y"):
            x = (-self.__b)/(self.__a)*2  
            y = (1) -pow((self.__b),2)+ (self.__a)*(self.__c)*4/4*(self.__a)
            print("le coordinate del fuoco con asse parallelo all'asse x sono:")
            return round(x, 2), round(y, 2)


    def direttrice(self, asse_simmetria = "x"):
        if (asse_simmetria=="x"):
           x = -1 -(self.__b)**2 + 4*(self.__a)*(self.__c)/4*(self.__a)
           return f'l equazione della retta direttrice di una parabola con asse parallelo all asse x è:  x = {x}'

        elif (asse_simmetria=="y"):
           y = -1 -(self.__b)**2 + 4*(self.__a)*(self.__c)/4*(self.__a)
           return f'l equazione della retta direttrice di una parabola con asse parallelo all asse y è:  y = {y}'
    
    
    
    def asse(self, asse_simmetria ="x"):
        if (asse_simmetria=="x"): 
           y = -(self.__b)/(self.__a)*2
           return f'l equazione dell asse parallelo allasse x è:  y = {y}'
        
        elif (asse_simmetria=="y"):
          x = -(self.__b)/(self.__a)*2
          return f'l equazione dell asse di una parabola con asse parallelo all asse y è x = {x}'
    

  


a_b_c = parabola(input('tipo: '),input('val 1: '), input('val 2: '), input('val 3: '))


print(a_b_c.fuoco(input("inserire l'asse parallelo a quello della parabola per ottenere le coordinate del fuoco:")))
print(a_b_c.direttrice(input("inserire l'asse parallelo a quello della parabola per ottenere l'equazione della retta direttrice: ")))
print(a_b_c.asse(input("inserire l'asse parallelo a quello della parabola per ottenere l'equazione dell'asse:")))