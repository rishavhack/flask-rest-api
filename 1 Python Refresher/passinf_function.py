def methodaception(another):
	return another()

def add_two():
	return 35+77

print methodaception(add_two)

#print methodaception(lambda : 35 + 77)

my_list = [13,56,77,484]
print list((filter(lambda x: x != 13 , my_list)))


# (lambda x : x * 3)(5)
# Both are same
# def f(x):
#	return x * 3
# f(5)


print [x for x in my_list if x != 13]