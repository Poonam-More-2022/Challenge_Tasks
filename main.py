import logging
logging.basicConfig(filename="task.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')
import list_task
import Dict_task
import tuple_task
import set_task
import string_task
import sys
import traceback


# List related task
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

obj=list_task.List_task()
try:
    print("\nOriginal list l :", l)
    print("#1. Reversing the given list l :", obj.reverse_list(l))                 #providing list
    #print(obj.reverse_list(4,1))              #trying to provide multiple arguments at a time instead of a list to check error
    #print(obj.reverse_list({'s':5, 'd': 7}))  #trying to provide dict instead of list to check error
    print("#2. Extracting 234 out of list l:", end="\t")
    obj.access_234(l)                          # Extracting 234
    print("#3. Extracting 456 out of list l:", end="\t")
    obj.access_456(l)                          # Extracting 456
    print("#4. Extracting list out of list l:", end="\t")
    obj.extract_list(l)                        # Extracting list out of list
    print("#5. Extracting 'sudh' out of list l:", end="\t")
    obj.extract_sudh(l)                        # Extracting "sudh"
    print("#6. Extracting Keys from Dictionary element out of list l:", end="\t")
    print(obj.extract_dict_keys(l))            # Extracting Keys from Dictionary element
    print("#7. Extracting Values from Dictionary element out of list l:", end="\t")
    print(obj.extract_dict_values(l))          # Extracting Values from Dictionary element
    print("#8. Extracting dict out of list l:", end="\t")
    obj.extract_dict(l)                        # Extracting dict out of list l

    l2 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
          {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
    print("\n Original list l2 :", l2)
    print("#9. Extracting dict out of list l2:", end="\t")
    obj.extract_dict(l2)                       # Extracting dict out of list l2
    print("#10. Extracting tuple out of list l2:")
    obj.extract_tuple(l2)                      # Extracting tuple out of list l2
    print("#11. Extracting set out of list l2:", obj.extract_set(l2))  # Extracting set out of list l2
    print("#12. Extracting all numeric out of list l2: ",obj.extract_numeric(l2))             # Extracting all numeric out of list l2
    print("#13. Summing all numeric out of list l2: ", obj.sum_all_num(l2))
    print("#14. Filtering all odd numbers from list l2: ", obj.filter_odd_numeric(l2))
    print("#15. Extracting 'ineuron' from list l2: ", obj.extract_ineuron(l2))
    print("#16. Finding out a number of occurrences of all the data.:")
    obj.extract_occurrence(l2)
    print("#17. Finding out of number of keys in dict element from given list: ", end=' ')
    obj.no_of_keys(l2)
    print("#18. Filtering out all the string data from the given list : ", obj.extract_string(l2))
    print("#19. Finding out alphanumeric data from given list : ", obj.extract_alphanum(l2))
    print("#20. Finding out multiplication of all numeric value in the individual collection inside dataset")
    obj.Mul(l2)
    print("#21. Unwrapping all the collection inside the collection and create a flat list: \n", obj.unwrap(l2))

except Exception as e:
    logging.exception(e)
    logging.error(e)
    print(e)


#Dictionary Related Tasks
print("\n #------------------Dictionary related Task output------------------#\n")
Avengers_power={'Shield':"Captain America", "Iron Man Suit": "Tony Stark", "More Powerful":{"Mjolnir":"Thor","Mind stone":"The Vision"}}
obj_dict=Dict_task.dict_task()
try:
    print("#1. Extracting all the values from given nested dictionary: ", obj_dict.dict_values(Avengers_power))
    print("#2. Finding out the number of keys in dict element from given dictionary: ", obj_dict.no_of_keys(Avengers_power))
    print("#3. Creating Dictionary with Squares and cubes for given numbers : ", obj_dict.sq_cube(3,5,7))
except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)

#Tuple Related Tasks:
print("\n #------------------Tuple related Task output------------------#\n")
obj_tuple= tuple_task.Tuple_task()
l2 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
          {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
try:
    print("#1. Extracting all tuple entities from given list: ", obj_tuple.extract_tuple(l2))
except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)

#Set Related Tasks:
print("\n #------------------Set related Task output------------------#\n")
obj_set=set_task.Set_task()
l2 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
          {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
try:
    print("#1. Extracting all tuple entities from given list: ", obj_set.extract_set(l2))
except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)

#String Related Tasks:
print("\n #------------------String related Task output------------------#\n")
obj_string=string_task.String_task()
str1='''Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]
Python consistently ranks as one of the most popular programming languages'''
try:
    print("1. Filtering out all the vowels form below text by using while loop : ", obj_string.extract_vowels(str1))
    print("#2. Return a len of it without using a inbuilt fun len : ", obj_string.string_length(str1))
except Exception as e:
    logging.error(e)
    logging.exception(e)
    print("\n error: ",e)


