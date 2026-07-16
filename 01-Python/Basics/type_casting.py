#basic
a = "1"
b = "2"
print(a + b) 


a = "1"
b = "2"
print(int(a) + int(b)) #string to int conversion


# 1. Explicit Typecasting
string = "15"
number = 7
string_number = int(string) # Explicitly converting string to integer
sum = number + string_number
print("The sum of both the number is:",sum)

# 2. Explicit Typecasting
string = "16.5"
numb = 9
string_numb = float(string) # Explicitly converting string to float
sum = numb + string_numb
print("the sum of both:" , sum)

# 3. Explicit Typecasting
string = "23"
number = 8
string_number = int(string)
sum = number + string_number
print("the sum of both:",sum)


# 1. Implicit Typecasting
c = 1.9
d = 8
print (c+d) # Implicitly converting integer to float and then adding

# 2.Implicit Typecasting
e = 5
print(type(e))

