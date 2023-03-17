# simpleASM 
simpleASM is a assembly like programming language that i am developing to be much simpler and easy to code than assembly language for people who dont know ASM too well but stull want to program cpus on a low level. i will write a customisable compiler for it that will need you to add translations for different operations like JMP, ADD, LOD etc but the actual syntax for simpleASM won't just be the translations that the compiler needs
## main syntax
### contol words:
```
arithmetic:
ADD : arguments(A , B , RESULT) #adds A to B and puts the result in RESULT
SUB : arguments(A , B , RESULT) #subtracts B from A and puts the result in RESULT
MULT : arguments(A , B , RESULT) #multiplys A to B and puts the result in RESULT
DIV : arguments(A ,B , R ESULT) #divides A from B and puts the result in RESULT
MOD : arguments(A , B , RESULT) #does A modulus B and puts the result in RESULT
INC : arguments(A , RESULT) #increments A by 1 and puts the result in RESULT 
DEC : arguments(A , RESULT) #decrements A by 1 and puts the result in RESULT  
```
```
bitwise logic:
AND : arguments(A , B , RESULT) #does bitwise AND to A and B and puts the result in RESULT
OR : arguments(A , B , RESULT) #does bitwise OR to A and B and puts the result in RESULT
XOR : arguments(A , B , RESULT) #does bitwise XOR to A and B and puts the result in RESULT
NAND : arguments(A , B , RESULT) #does bitwise NAND to A and B and puts the result in RESULT
NOR : arguments(A , B , RESULT) #does bitwise NOR to A and B and puts the result in RESULT
XNOR : arguments(A , B , RESULT) #does bitwise XNOR to A and B and puts the result in RESULT
RSHF : arguments(A , AMOUNT , RESULT) # binarily right shifts by AMOUNT bits and puts the result in RESULT
LSHF : arguments(A , AMOUNT , RESULT) # binarily left shifts by AMOUNT bits and puts the result in RESULT
```
```
data management:
COPY : arguments(SOURCE , DESTINATION) #copies the value in SOURCE and puts it in DESTINATION
MOVE : arguments(SOURCE , DESTINATION) #moves the value in SOURCE and puts it in DESTINATION and clears the data in SOURCE
SWAP : arguments(SOURCE , DESTINATION) #swaps the values in SOURCE and puts it in DESTINATION
```
```
RAM management:
LOAD : arguments(RAM ADDRESS, DESTINATION) #takes the value from the ram address and copies it into DESTINATION 
STORE : arguments(SOURCE , RAM ADDRESS) #takes the data from SOURCE and copies it in the ram ADDRESS
RESET : arguments(RAM ADDRESS) #clears the data in the ram address
 ```
 ```
defines:
FUNC : arguments(NAME) #defines a function  
VAR : arguments(NAME , VALUE) #defines a variable and makes its value be VALUE
```
```
stack management:
PUSH : arguments(SOURCE) #pushes a value to the stack
POP : arguments(DESTINATION) #pops a value from the stack 
PEEK : arguments(POSITION , DESTINATION) #gets a value from the stack based off the POSITION
```
```
other:
IF : arguments(A , COMPARISON , B) #compares two values and if it returns true it will jump to the nearest THEN control word
THEN : arguments(none) #will be jumped to by a IF if it returns TRUE
ELSE : arguments(none) #will be jumped to by a IF if it returns FASLE
RUN : arguments(FUNCTION) #runs a fucntion 
END : arguments(none) #states the end of a fucntion
GOTO : arguments(LABEL) #a unconditional jump 
```
### syntax:
```
comparisons:
= : #A equal to B
> : #A greater than B
< : #A less than B
>= : #A greater than or equal to B (also the same as inverted less than )
<= : #A less than or equal to B (also the same as inverted greater than )
>< : #A less than or greater than B (also the same as inverted equal to)
```
```
other:
TRUE : #returns true no matter A or B
FASLE : #returns flase no matter A or B
LABEL : (@ , NAME) #a label for a GOTO to jump to
```
## compiler info
### general info
the main simpelASM compiler will be made custommizable so that you dont have to write a whole simpleASM compiler just for a diffrent cpu ISA or assembly language. in this repo tere will be a "core.txt", "basic.txt" and a "advanced.txt" text file which will be where the compiler will get the translations to compile the simpleASM to. 
### specifications
headers:
```
BITS : #returns the number of bits your cpu is
MAX : #returns the maximum posible value your can can have (unsigned) 
MAXCALL : #returns how deep the call stack is
MAXDATA : #returns how deep the data stack is
```
core reqirements:
```
(register 0 must always return 0)
BITS
MAXCALL
MAXDATA 
ADD 
NOR
LOAD
STORE
JUMP IF GREATER 
IMM
RIGHT SHIFT 
```
basic reqirements:
```
(register 0 must always return 0)
(immediates are used in instuctions that arent IMM)
(all of core)
AND
OR
XOR
SUB
JUMP IF LESS
JUMP IF EQUAL 
```







