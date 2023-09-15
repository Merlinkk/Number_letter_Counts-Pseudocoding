numbers = {
	'1':"ONE",
    '2':"TWO" ,
    '3':"THREE", 
    '4':"FOUR" ,
    '5':"FIVE",
    '6':"SIX" ,
    '7':"SEVEN",
    '8':"EIGHT",
    '9':"NINE",
    '0':"ZERO"
}

# x = numbers[5]
# print(len(x))  877

N = int(input("Enter Number: "))

N= str(N)
sum=0
for i in N :
    sum += len(numbers[i])
    print(numbers.get(i))
    
print(sum)