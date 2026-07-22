# Intro to Dsa(data structure & algorithm)
Data -> information

Structure -> array
            stack
            queue
            tree
            graph

Algorithm -> set of instructions(how software is made)

# Time Complexity 
Time complexity-> To compare 2 programs/softwares we need to check the time complexity of both .

In a program -> focus -> on tht part of the code tht takes max time , its time complexity = final time complexity.
Lower order ignore , HIGHER order is carried further.

Comparison:
1< log log n < n < n^2 < n^3 < n^4 ....< 2^n
[smallest .......largest]
where, n = size of input 

Mathematical Equation:           dominating  factor
1) Constant Eqn: y = 5                  [1]

2) Linear Eqn: y = 2x + 5               [x]

3) Quadratic Eqn: y = 2x^2 + 3x - 5    [x^2]

4) Cubic Eqn: y = 2x^3 + 3x - 5        [x^3]

5) Logarithmic Eqn: y = log x + 2     [log x]

6) Exponential Eqn: y = 3^x + 3        [3^x]

Types of Analysis:       notation
1) Best case:             omega
2) average case:          theta
3) Worst case:            Big O (By default)


Determning Time Complexity:
1) Constant Time Complexity: 
x = 5 -> 1 unit
print(x) -> 1 unit
if (x==5):
  print("Hello")
  else:
  print("Welcome")

No loops , no recursion , it will take constant unit , Size of input same .
 1 + 1 = 2 , where DF : 1
So, TC : O(1)

2) Linear Time Complexity:
y = 2x + 10 = O(n)

 Eg 1:
 x = 5 
print (x)               O(1)
for i in range (0,x):    +
print(i)                O(n) 

So , TC : O(n) 


Eg 2:
n = 5            
print(n)                 O(1)
for i in range(0,n):      +
print(i)                 O(n)
for j in range(0,n):      +
print(j*j)               O(n)
for k in range(o,n/2)     +
print("hello")           O(n/2)

So, TC: 1 + n + n + n/2 = O(n) 

Why addition?
Coz loops are 1 after another.


3) Quadratic Time Complexity:
 2n^2 + 3n + 5 -> O(n^2)

Eg 1:
n = 5                       
m = 10                  
print(n+m)                  O(1)

for i in range (0,n):    O(n) 5 times
for j in range (0,m):    O(n) 10 times
print("hello")           50 times(5*10)

for k in range (0,n):
print("welcome");           O(n)


So,TC : 1 + (n*n) + (n) = O(n^2)

Why multiply?
Coz nested loop , one loop inside another loop -> multiplication takes place.


4) Cubic Time Complexity:
Eg 1:
n = 5                       
m = 10                      
print(n+m)                  O(1)

for i in range (0,n):    O(n) 5 times
for j in range (0,m):    O(n) 10 times
for k in range (0,n):    O(n)
print("welcome") :      O(n)* O(m)*O(n)

for l in range (0,n):
print("welcome");          O(n)

So,TC: 1 + (n*n*n) + n = O(n^3)


What will be the total time complexity?
n = 5
if(n==5):  O(n^2)

else : 
           O(n^3)

Here , most DF n^3 , So TC : O(n^3)


5) Logarithmic Time Complexity:
Eg 1:
 n=10 
 while (n>=1):
 print("Hello")    k times = O(k)
 n = n\\2

 O\P: 
 n=10   hello
 n=5    hello
 n=2    hello
 n=1    hello
 n=0      -
       
  n\2 , n\2^2 , n\2^3 ,......n\2^k = 1

  n = 2^k
  log n = log 2^k
  log n = klog2
  k = logn\log2
  So,TC: O(logn) 

  Note: If loop is getting divided by 2,3,4 , TC: log n 

  Eg 2:
  n=1
  while(i<10):
  print("hello")
  i = i*2

  O/P:
  i=1      hello
  i=2      hello
  i=4      hello
  i=8      hello

  So,TC : O(logn)

  Note: If loop is getting DOUBLED like 1->2->4->8 , TC:logn






