the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this for loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#mixed list
#%r is used since we don't know what the element is
for i in change:
    print "I got %r" % i

#we can also build lists
elements = []

#use the range function to do 0 to 20 counts
for i in range(0,20):
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)

#now we can print out elements
for i in elements:
    print "Element was: %d" % i

































