[A] #MODULES & PIP

# Modules are files containing Python code. 
#They can define functions, classes, and variables that you can reuse in your programs. 
#You can create your own modules or use built-in modules provided by Python.

# Two Types:
1. Built_in Modules: No Need to install 
2. External Modules: Need to be installed 

# THE PIP COMMAND(a package manager)

import pandas 
# Read and work with a file named 'words.csv'
pandas.read_csv('words.csv')

# Comments,Escape Sequences & Print statements

1. Comments:Two Types

Single line comment: print("this is a school")

Multi_line Comment: ''' ''' or """ """  will be a multi line comment. 

2. Escape Sequence Characters 
To insert chracters that cannnot be directly used in a string , we use these escape sequence character. 

To insert chracter is a backslash \ followed by a character u want to insert. 

 Eg: Usage of \n(An escape sequence) for printing in a new line

eg : print("Hey I m a good girl \nand this viewer is also a gud boy or girl")

Eg: print("Hey I m a \"good girl\" \nand this viewer is also a gud boy or girl")
O\P:Good girl will be displayed in double quotes.

3. Separators : 
# default separator : Space

eg: print("Hey",6,7,sep="~",end="009\n")
print("Siya")
O/P: Hey~6~7009
Siya

# file: An object with a write method, Default is sys.stdout(optional)


[B] Variables & data types

 Variable is like a container that holds data. Creating a varaible is like creating a plceholder in memory and assigning some value. 

 eg : a = 1
      b = true
      C = "Harry"
      d = None
      (4 variables of diff data types)

Data Type specifies the type of value a variable holds. Diiferent types:

# 1. Numeric data: 
int: 3,-4 ,
float: 7.45,-9.0 ,
complex: 6 + 2i

# 2.Text data :
str : "Hello world"

# 3.Boolean data
Containes true or false

# 4. Sequenced data
list : Ordered collection of data with elements separated by a comma & enclosed within square brackets. Mutable and can be modified after creation.

eg: list1 = [9,2.3,[-4,5], ["apple", "banana"]]
print(list1)

Tuple: Ordered collection of data with elements separated by a comma and enclosed within parenthesis. Immutable amd cannot be modified after creation.

eg: tuple1 = (("parrot","sparrow")("lion","tiger"))
print(tuple1)


# 5. Mapped data
dict : Collection of data containing a  key value pair. {} are used. 

eg: dict1 = {"name":"sakshi" , "Age":20,"CanVote":True}
print(dict1)
