#with out lambda
def  getEven(x):
    if x%2==0:
        return True
    else:
        return False
li=[23,12,56,3,9,18,4]

l1=list(filter(getEven,li))
print(l1)


# with lambda``


l2=list(filter(lambda a:a%2==0,[2,121,57,32,92,181,47]))
print(l2)

#list of names  below 6 
# =>,->,lambda

l3=list(filter(lambda name:len(name)<6,['suresh','naresh','ramesh','rajesh','somesh','xyz','abc']))
print(l3)