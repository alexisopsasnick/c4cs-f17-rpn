#!/usr/bin/env python3
import operator 
import readline
import logging 
import sys
from termcolor import colored, cprint

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
	'//': operator.floordiv,
}


def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
			print(token, ' ')
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			# token = colored(token, on_cyan)
			cprint(token, 'white', 'on_cyan')
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	logger.debug(stack)
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		if result < 0:
			result = "Result: " + str(result)
			cprint(result, 'red')
		else:
			print("Result: ", result)

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
	main()
