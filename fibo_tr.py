#import turtle as tr 

#tr.bgcolor("purple")
#r.title("fibonatchi")

#pen =tr.Turtle()
#pen.color("yellow")
#pen.pensize(3)

def fibo (n):
    if n<=1 :
        return n 
    else :
        return fibo(n-1)+fibo(n-2)
n =int(input("please enter  n :"))
print(fibo(n))

import turtle

def shekle():
    a = turtle.Turtle()
    for i in range(fibo(n)):
        a.forward(2+i/4)
        a.left(30-i/12)
    
    turtle.done()

shekle()