A = int(input("Enter Alice's number:"))
B = int(input("Enter Bob's number:"))
g = int(input("Enter base value g:"))
p = int(input("Enter mod value p:"))

Xa = (g**A)%p
Xb = (g**B)%p

print("Xa is ",Xa)
print("Xb is ",Xb)

x1 = (g**Xb)%p
x2 = (g**Xa)%p

print(x1,x2)

