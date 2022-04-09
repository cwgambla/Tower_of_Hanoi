
A = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
B = []
C = []

def h(n,start,spare,end):
    if n == 1:
        pm(start,end)


    else:

        h(n-1,start,end,spare)
        pm(start,end)
        h(n-1,spare,start,end)

def pm(start,end):
    end.append(start.pop())
    print("A =",A)
    print("B =",B)
    print("C =",C)
h(16,A,B,C)
