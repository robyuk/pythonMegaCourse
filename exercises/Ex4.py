''' Exercises for day 4'''

#Ex1
dollars=input("How many dollars? ")
eur=float(dollars)*0.95
print("The amount in euros is ", eur)

'Ex2'
ranking= ['John', 'Sen', 'Lisa']
i=int(input("Input rank number: "))
print(ranking[i-1])

'Ex3'
name=input("Enter a name: ")
i=0
for n in ranking:
    i+=1
    if n==name:
        print("Rank: ",i)

' Bug fixing Exercises'
elements = ['a', 'b', 'c']
print(elements[1])

new = 'x'
elements[1] = new
print(elements)
