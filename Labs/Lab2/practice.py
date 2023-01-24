# import math

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "(" + str(self.x) + "," + str(self.y) +




# class Line:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2

#     def length(self):
#         return self.p1.distanceTo(self.p2)

# class Triangle:
#     def __init__(self):
    

#     def area(self):
#         a = self.p1.distanceTo(self.p2)

    


#     p = Point(0,0)
#     print (p)
#     q= Point(3,4)
#     r= Point (2,2)
#     t= Triangle(p,q,r)
#     print(t.area())

#     class LinkedList:
#         def __init__(self, value, rest):
#             self.first = value
#             se;f.rest = rest

#         def show(self):
#             if self.rest == None:
#                 return str(self.forst) + " . "
#             else:
#                 return str(self.first) + ' ' + self.rest.show()

# a= LinkedList("Christa", None)
# print ("starting with an empty list we add Christa", end="")
# print(a.show())
# a = LinkedList ("ahmed", a)
# print ("adding ahmed we get..", end='')
# print(a.show())

class BinaryTree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)

    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()
        return "(" + str(self.value) + "  " + str(left) + "  " + str(right)

    def add(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinaryTree(value, None, None)
            else:
                left = self.left.add(value)
        elif value > self.value:
            if self.right == None:
                self.right = BinaryTree(value, None, None)
            else:
                right = self.right.add(value)
        else:
            pass


a = BinaryTree(5, None, None)
node = 8
a.add(node)
print(a.show())
node2 = 3
a.add(node2)
print(a.show())

# left_leaf = BinaryTree(1, None, None)
# right_leaf = BinaryTree(9, None, None)

# myBT = BinaryTree(5, left_leaf, right_leaf)
# print (myBT.show())