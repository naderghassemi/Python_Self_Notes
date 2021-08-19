x='Hello World'
len() #length of a variable for example x="Hello World" and len(x)
type() #type of a variable
x.upper() #upper case the whole variable sentence
x.lower() #lower case the whole sentence
y=10*x
x+x
x='abcdefghij'
x[1]        # b
x[1:]		# bcdefghij
x[4:7]		# efg
x[::2]		# acegi jumps every other index
x[1:9:2]	# bdfh
x[-1:]		# j gives the last letter
x[::-1]		# jihgfedcba reverse the string

print('The {b} {g} {f}'.format(f='cute', b='fox',g='orange')) 	# The fox orange cute
result = 100/777 												# 0.1287001287001287  
print("The result is {r}".format(r=result))					    #The result is 0.12870					
print("The result is {r:1.5f}".format(r=result)) 				#	0.12870	float formating follows "{value:width.precision f}"
name=Jose
age= 10
print(f'Hello, his name is {name} and his age is {age}') 		# which is equivalent to adding it with .format but the f'' method and is only available after 3.7 version and similar to othe languages
my_list=['one','two', 'three']
second_list=['four','five']
new_list=my_list+second_list 									#   new_list= ['one', 'two', 'three', 'four', 'five']
new_list[1]='one all caps' 										# new_list=['one', 'one all caps', 'three', 'four', 'five']
new_list.append('six') 											# new_list=['one', 'one all caps', 'three', 'four', 'five', 'six']   .append() adds a new item to the end of the list. IT CHANGES THE LIST AND DOESN'T REQUIRE new_list=new_list.append('six')!!
new_list.pop() 													# new_list=['one', 'one all caps', 'three', 'four', 'five' ]   .pop() removes the last item to the end of the list. IT CHANGES THE LIST AND DOESN'T REQUIRE new_list=new_list.pop()!!
new_list.pop(0)													# new_list=[ 'one all caps', 'three', 'four', 'five' ]
new_list=['g','f','h','o','a', 'd','b', 'c']
num_list=[2,1,0,-3,10,19.2]
new_list.sort() 												# new_list= ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'o']
num_list.sort() 												# num_list= [-3, 0, 1, 2, 10, 19.2]
new_list.reverse() 												# ['o', 'h', 'g', 'f', 'd', 'c', 'b', 'a']
num_list.reverse() 												# [19.2, 10, -3, 0, 1, 2]