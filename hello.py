#python for beginner
print(2+10)
mystring = 'hhsdjsjdj'
print(mystring)
print(mystring[2])
print(mystring[2:])

print(mystring[2:5])
x = 'hello world'
print(x)
y = x.split('o')
print(y)

z = "Item One: {} Item  Two: {}". format("dog" , "cat")
#list

#mylist = [1,2,3,4]
mylist = ['stringgsd' , 1,2,3,4,5,5,6, True, 'fgh',[1,2,3,4,5]]
print(mylist)
print(len(mylist))
print(mylist[3])
wale = ['w', 'r', 'g']
print(wale[1])
wale.append("NEW ITEM")
print(wale)
print(wale.count)
listtwo =  ["qwew", "tgdf"]
wale.extend(listtwo)
print(wale)
item = wale.pop(0)
print(item)
wale.reverse()
print(wale)
guy = [4,5,6,1,2,3,7,8,9]
guy.sort()
print(guy)
matrix = [[1,2,3,], [5,6,7], [2,3,4]]
first_col = [row[0] for row in matrix]
print(first_col)

#dictionary. dictionary is python's version of hash table they are use to create a "mapping" with key value pairs
my_stuff  = {"key1": "value", 'key2': 'value2','key3': {'123':[1,2,'fgh']} }
print(my_stuff['key3']['123'][2].upper())

my_stuf = {'launch': 'pizza' , 'bfast': 'eggs' }
my_stuf['launch'] = 'burger'
my_stuf['dinner'] = 'pasta'
print(my_stuf['launch'])
print(my_stuf)

#tuples are immutable sequences
#sets are unordered collections of unique elements
#booleans are just True and False as before

#booleans

x = set()

x.add(1)
x.add(2)
x.add(0.2)
x.add(0.3)
x.add(7)
print(x)

converted = set([1,1,1,1,2,2,2,2,2,3,3,3,3])
print(converted)

#exercise

s = 'django'
print(s[0])
print(s[1:4])

l = [2,3,4,5,[5,6,'hello']]
#reassign helllo to godbye
l[4][2] = 'goodbye'
print(l)

#comparison
1<2
1>2
2>= 4
2 == 2

(1>2) and (2<4)

if 4<2:
    print('first block')
else:
    print('hello')
    if 20 < 3:
            print('second block')

#loops
#for loops
sew = [1,2,3,4,5,6]
for item in sew:
    print('hello')
    print(item)

d = {"sam":1 , "frank": 2 , "grh":3} #dictionary
for k in d:
    print(k)
    print(d[k])
    
    mypairs = [(1,2),(3,4),(5,6)]
    for (tup2, tup1) in mypairs:
        print(tup1)
        print(tup2)
        
        #while loops
        
        i = 1
        
        while i<6:
            print("i is: {}".format(i))
            i = i+1
            
            #list comprehension
            
            x = [1,2,3,4]
            
            out = [num**2    for num in x]
            print(out)
            
                

#function

def my_function(param1 = 'default'):
    print("my first python function! {}".format(param1))










