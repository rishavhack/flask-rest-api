import functools

def my_decorator(func):
	@functools.wraps(func)
	def function_that_runs():
		print "1st"
		func()
		print "3rd"

	return function_that_runs. #This return 1st,2nd,3rd and replace my_function()


@my_decorator
def my_function():
	print '2nd'

my_function()

##
##
##New Program

def decorator_with_arguments(number):
	def my_decorator(func):
		@functools.wraps(func)
		def function_that_run_func(*args,**kwargs):
			print '1st'
			if number == 56:
				print 'Nothing'
			else:
				func(*args,**kwargs)

			print '3rd'
		return function_that_run_func
	return my_decorator

@decorator_with_arguments(56)
def my_function_too(x,y):
	print x+y

my_function_too(57,67)
