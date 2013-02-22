"""
Example program to demonstrate a quantum class of list/set
"""
import cat

class HeisenSetList(cat.Box):
    box = [list, set]


hsl1 = HeisenSetList([1, 2, 3])
hsl2 = HeisenSetList([1, 2, 3])

print isinstance(hsl1, list) # True
print isinstance(hsl1, set)  # Also True
print hsl1.union # bound method
print hsl1.index # bound method
print hsl.index(3) # 2
try:
    print hsl1.union
except AttributeError:
    print 'Not A set'
    print isinstance(hsl1, list) # True
    print isinstance(hsl1, set) # False
