# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
def tax():
  sales=int(input('What is your total sales amount for this month in dollars?'))
  ctax=sales*.025
  stax=sales*.05
  ttax=ctax+stax
  print('The county sales tax is $',format(ctax, '.2f'),'.')
  print('The state sales tax is $',format(stax,'.2f'),'.')
  print('The total tax is $',format(ttax,'.2f'),'.')

tax()
