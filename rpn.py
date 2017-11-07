#!/usr/bin/env python3
import operator 


ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
	main()
