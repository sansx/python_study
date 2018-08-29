def rang():
    for i in range(4):
        yield i

test = rang()

for i in test:
    print(i)


xl = [1,3,5] 
yl = [9,12,13] 
    
l  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]

d = {k: v for k,v in enumerate("Vamei") if v not in "Vi"}

for i in map(lambda x:x ,range(10)):


    print(i)