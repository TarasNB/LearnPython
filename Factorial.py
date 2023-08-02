num = int(input("Plaese enter a number "))
fact = 1 
for iterFact in range(2, num + 1):
    fact = fact * iterFact

print(num, "! = ", fact)
