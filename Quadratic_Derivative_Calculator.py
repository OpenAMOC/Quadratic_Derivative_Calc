##This script finds the derivative of quadratic equations and has basic graphing capabilities
#here we import relevant libraries
import numpy as np
import scipy as sp
import time
#import sympy for symbolic derivation
import sympy as smp
import matplotlib.pyplot as plt
from scipy.misc import derivative

#define symbols, where a b and c are constants, x is what we will take the derivative of
#always good to make clear these are real numbers using real=True
x, a, b, c = smp.symbols('x a b c', real=True)

#outline the equation with constants and x
f = ((a)*(x**2)+(b)*(x)+(c))

#compute derivatives using smp.diff(f, x) where f is the function you want to take the derivative of and
#x is the variable you are taking the derivative with respect to
dfdx = smp.diff(f, x)

#allow the user to input the values and decide what type of derivation to use using input and if statements
print("This program finds the derivative of a quadratic equation formatted as ax^2+bx+c")
xknown = str(input("Do you know the value of x? Y/N "))
if xknown == ("yes") or xknown == ("Y") or xknown == ("y"):
	print("\nOk, please input the 4 known values:")
	xsub = float(input("What is x? "))
	asub = float(input("What is a? "))
	bsub = float(input("What is b? "))
	csub = float(input("What is c? "))
	#you will need to sub in the values provided and evaluate as below
	print("\nThe derived number is ", dfdx.subs([(x,xsub),(a,asub),(b,bsub),(c,csub)]).evalf())
	#the program ends automatically after some time
	time.sleep(10)
	print("\nClosing Program")
	time.sleep(1)
	exit()
else:
	#this section starts much as before
	print("\nOk, please input the 3 known values:")
	asub = float(input("What is a? "))
	bsub = float(input("What is b? "))
	csub = float(input("What is c? "))
	print("\nThe derived equation is ", dfdx.subs([(a,asub),(b,bsub),(c,csub)]).evalf())
	time.sleep(1)
	#but now there is the option to plot these equations, so another input and if statements are required
	graph_it = str(input("\nWould you like both equations (the original quadratic and derived linear) graphed? Y/N "))
	if graph_it == ("yes") or graph_it == ("Y") or graph_it == ("y"):
		print("\nNow Preparing Graph...")
		time.sleep(5)
		dfdx_f = smp.lambdify((x,a,b,c), dfdx)
		#set the size of the x-axis
		x = np.linspace(-5,5,100)
		#write the equations for the original quadratic and derivation (here shown as y and z)
		y =((asub)*(x**2)+(bsub)*(x)+(csub))
		z = dfdx_f(x, a=asub, b=bsub, c=csub)
		#create the axis
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		ax.spines['left'].set_position('center')
		ax.spines['bottom'].set_position('center')
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		#plot with a legend
		plt.plot(x,y, 'b', label="Original_Equation")
		plt.plot(x,z, 'c', label="Derived_Equation")
		plt.legend(loc='upper left')
		plt.show()
	else:
		print("\nClosing Program")
		time.sleep(1)
		exit()
