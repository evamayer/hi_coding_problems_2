from statistics import mean

def mean_of_numbers(number_list):
    x = mean(number_list)
    return x

print("Please enter three numbers.")
a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

print("The mean of your three numbers is", round(mean_of_numbers([a, b, c]), 4))

