class Marvel:
    def __init__(self,name,movie):
        self.name=name
        self.movie=movie
h1=Marvel("Tony","Ironman")
h2=Marvel("Steve","First Avenger")
h3=Marvel("Natasha","Ironman 2")
print("First hero",h1.name,"was in",h1.movie)
print("Second hero",h2.name,"was in",h2.movie)
print("Third hero",h3.name,"was in",h3.movie)
del h2
del h1.movie
#print(h1.movie)
#print(h2)
