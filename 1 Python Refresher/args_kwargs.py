 def additiona_simplified(*args):
 	return sum(args)


additiona_simplified(3,5,7,12,14,5)


def what_r_kwargs(*args,**kwargs):
	print args
	print kwargs

what_r_kwargs(12,34,56)


def what_r_kwarg(*args,**kwargs):
	print args
	print kwargs

what_r_kwarg(12,34,56,name="Jose",location="UK")