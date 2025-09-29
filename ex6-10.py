import math
"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
costOfMeal=float(input("What is the cost of your meal?"))
tax=costOfMeal*(0.078)
tax=round(tax,2)
tip=costOfMeal*(0.18)
tip=round(tip,2)
print("The tax of your meal is", tax, "and the tip of your meal is", tip)

"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
n=float(input("Enter a positive integer: "))
sum=(n*(n+1))/2
print("The sum of all the integers from 1 to n is", sum)

"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)
"""
numberOfGizmos=int(input("Enter the number of gizmos: "))
numberOfWidgets=int(input("Enter the number of widgets: "))
print("The number of gizmos in the order is", numberOfGizmos)
print("The number of widgets in the order is", numberOfWidgets)
totalWeightGizmos=numberOfGizmos*112
totalWeightWidgets=numberOfWidgets*75
totalWeight=totalWeightGizmos+totalWeightWidgets
print("The total weight of the order is", totalWeight)

"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
moneyDeposited=float(input("What is the amount of money deposited? "))
oneYear=moneyDeposited+(moneyDeposited*0.04)
oneYear=round(oneYear,2)
twoYears=oneYear+(oneYear*0.04)
twoYears=round(twoYears,2)
threeYears=twoYears+(twoYears*0.04)
threeYears=round(threeYears,2)
print("The amount in the savings account after 1 year is", oneYear)
print("The amount in the savings account after 2 years is", twoYears)
print("The amount in the savings account after 3 years is", threeYears)

"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
a=float(input("What is integer a?"))
b=float(input("What is integer b?"))
sum=a+b
print("The sum of a and b is", sum)
difference=a-b
print("The difference when b is subtracted from a is",difference)
product=a*b
print("The produce of a and b is",product)
quotient=a/b
print("The quotient when a is divided by b is", quotient)
remainder=a%b
print("The remainder when a is divided by b is",remainder)
log=math.log10(a)
print("The result of log10 a is", log)
power=a**b
print("The result of a to the power of b is",power)