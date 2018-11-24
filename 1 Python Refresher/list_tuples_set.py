list_grades = [77,88,99,2,200,88]
tuples_grdades = (77,88,99,2,200,88) #immutable
set_grades = {77,88,99,2,200,88} #unique & unordered


print list_grades
print tuples_grdades
print set_grades


tuples_grdades = tuples_grdades + (100,)
print tuples_grdades

set_grades.add(78) # it will not add
print set_grades

one = {7,9,6,4}
two = {4,6,7,8,9,5}

print one.intersection(two)
print one.union(two)
print one.difference(two)