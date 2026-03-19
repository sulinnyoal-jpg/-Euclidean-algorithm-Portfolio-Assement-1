#take user input to find greatest common
first_input = int(input('Enter first number: '))
second_input = int(input('Enter second number: '))

if second_input > first_input:
    first_input , second_input = second_input , first_input

#initialse temporary number to give while loop condition
remainder = 1

#finds the greatest common divisor by dividing the greater
#number of the pair under either one reaches 0
while remainder !=0:
    remainder = first_input % second_input
    quotient = first_input // second_input
    (first_input, second_input) = (second_input,remainder)

print("The GCD=", first_input)