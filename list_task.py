'''# Questions for list
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element available in list
7 . Try to extract all the value element form dict available in list '''
#---------------------------------#---------------------------------------#
'''for l2=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),
   {"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
#8. Try to extract dictionary entities
#9. Try to extract all tuple entities
#10. Try to extract all set entities
#11. Try to extract all the numerical data it may be the part of dict keys and values
#12. Try to give summation of all the numerical data extracted in Q#10
#13. Try to filter out all odd values out all numeric data which is a part of a list
#14. Try to extract "ineuron" out of given data
#15.Try to find out a number of occurrences of all the data
#16. Try to find of number of keys in dict element from given list
#17. Try to filter out all the string data from the given list
#18. Try to find out alphanumeric data from given list
#19. Try to find out multiplication of all numeric value in the individual collection inside dataset
#20. Try to unwrap all the collection inside the collection and create a flat list   '''

import logging
logging.basicConfig(filename="list_test.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class List_task:

#1 . Try to reverse a list
    def reverse_list(self,L):
        ''' This function is used to reverse the list'''
        logging.info("The list entered by user is :  %s",L)
        try:
           rev = L[::-1]
           logging.info("List is successfully reversed: %s",rev)
           return rev
        except Exception as e:
            #logging.critical("There is a error")
            logging.error(e)
            logging.exception(e)
            return e


# 2. try to access 234 out of this list
    def access_234(self,L):
        '''This function access 234 out of this list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==int:
                    if i==234:
                        l.append(i)
                elif type(i)==list or type(i)==tuple:
                    for j in i:
                        if j==234:
                            l.append(j)
                elif type(i)==dict:
                    k,v = i.items()
                    for p in k:
                        if p==234:
                            l.append(p)
                    for z in v:
                        if z==234:
                            l.append(z)
            logging.info("Accessed 234 out of given list : %s",l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

# 3 . try to access 456
    def access_456(self,L):
        ''' This function access 456 from given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==int:
                    if i==456:
                        l.append(i)
                elif type(i)==list or type(i)==tuple:
                    for j in i:
                        if j==456:
                            l.append(j)
                elif type(i)==dict:
                    k,v = i.items()
                    for p in k:
                        if p==456:
                            l.append(p)
                    for z in v:
                        if z==456:
                            l.append(z)
            logging.info("Accessed 456 out of given list : %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

# 4 . Try to extract only a list collection form list l
    def extract_list(self,L):
        '''This function extract only a list collection form the given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==list:
                    l.append(i)
            logging.info("Extracted only a list collection form given list : %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

# 5 . Try to extract "sudh"
    def extract_sudh(self,L):
        '''This function extract word 'sudh' from given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==str:
                    if i=="sudh":
                        l.append(i)
                elif type(i)==list or type(i)==tuple:
                    for j in i:
                        if j=="sudh":
                            l.append(j)
                elif type(i)==dict:
                    k,v = i.items()
                    for p in k:
                        if p=="sudh":
                            l.append(p)
                    for z in v:
                        if z == "sudh":
                            l.append(z)
            logging.info("Extracted the word 'sudh' from given list : %s",l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

# 6 . Try to list all the key in dict element available in list
    def extract_dict_keys(self,L):
        ''' This function lists out all the key in dict element available in given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==dict:
                    l.append(i.keys())
            logging.info("List of all the keys in dict elements available in given list : %s",l)
            return l

        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

# 7 . Try to extract all the value element form dict available in list
    def extract_dict_values(self,L):
        ''' This function extracts all the value element form dict available in given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==dict:
                    l.append(i.values())
            logging.info("List of all the values in dict elements available in given list : %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#8. Try to extract dictionary entities
    def extract_dict(self,L):
        ''' This function extract dictionary entities from the given list '''
        try:
            logging.info("The list entered by user is :  %s", L)
            for i in L:
                if type(i)==dict:
                    logging.info("Dictionary entities in the given list: %s", i)
                    print(i)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#9. Try to extract all tuple entities
    def extract_tuple(self,L):
        ''' This function extract all tuple entities from the given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==tuple:
                    l.append(i)
            logging.info("All tuple entities in the given list: %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#10. Try to extract all set entities
    def extract_set(self,L):
        ''' This function extract all set entities from the given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l=[]
            for i in L:
                if type(i)==set:
                    l.append(i)
            logging.info("All set entities in the given list: %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#11. Try to extract all the numerical data it may be the part of dict keys and values
    def extract_numeric(self,L):
        '''This function extract all the numerical data it may be the part of dict keys and values in the given list'''
        try:
            logging.info("The list entered by user for function 'extract_numeric' is :  %s", L)
            n=[]
            for i in L:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            n.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            n.append(k)
                        if type(v) == int:
                            n.append(v)
            logging.info("All the numerical data from the given list: %s", n)
            return n
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#12. Try to give summation of all the numerical data extracted from given list
    def sum_all_num(self,L):
        ''' This function gives summation of all the numerical data extracted from given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            sum1=sum(List_task.extract_numeric(self,L))
            logging.info("Summation of all the numerical data extracted from list: %s",sum1)
            return sum1
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#13. Try to filter out all odd values out all numeric data which is a part of a list
    def filter_odd_numeric(self,L):
        '''This function filters out all odd values out all numeric data which is a part of a given list '''
        try:
            logging.info("The list entered by user is :  %s", L)
            odd=[]
            l1=List_task.extract_numeric(self,L)
            for i in l1:
                if i%2!=0:
                    odd.append(i)
            logging.info("All odd values out all numeric data which is a part of a list : %s", odd)
            return odd
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#14. Try to extract "ineuron" out of given data
    def extract_ineuron(self,L):
        ''' This function extracts "ineuron" out of given data'''
        try:
            logging.info("The list entered by user is :  %s", L)
            n=[]
            for i in L:
                if type(i) == list:
                    for j in i:
                        if j == "ineuron":
                            n.append(j)
                if type(i) == dict:
                    for k in i:
                        if i[k] == "ineuron":
                            n.append(i[k])
            logging.info("Extracting 'ineuron' out of given list : %s", n)
            return n
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#15.Try to find out a number of occurrences of all the data.
    def extract_occurrence(self,L):
        '''This function finds out a number of occurrences of all the data'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l1 = []
            for i in L:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        l1.append(j)
                elif type(i) == dict:
                    for k,v in i.items():
                        l1.append(k)
                        l1.append(v)
                else:
                    l1.append(i)
            d={}
            for i in set(l1):
                d[i]=l1.count(i)
            logging.info("Number of occurrences of all the data: %s", d)
            return d
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#16. Try to find of number of keys in dict element from given list
    def no_of_keys(self,L):
        ''' This function finds of number of keys in dict element from given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            for i in L:
                if type(i) == dict:
                    logging.info("Number of keys in dict element %s from given list: %s", i, len(i))
                    print(len(i))
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#17. Try to filter out all the string data from the given list
    def extract_string(self,L):
        '''This functions filters out all the string data from the given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            s=[]
            for i in L:
                if type(i) == list:
                    for j in i:
                        if type(j) == str:
                            s.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str:
                            s.append(k)
                        if type(v) == str:
                            s.append(v)
                elif type(i)== str:
                    s.append(i)
            logging.info("Filtered out all the string data from the given list : %s",s)
            return s
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#18. Try to find out alphanumeric data from given list
    def extract_alphanum(self,L):
        '''This function finds out alphanumeric data from given list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            alpha_num=[]
            L = List_task.extract_string(self,L)
            for i in L:
                if i.isalnum():
                    alpha_num.append(i)
            logging.info("All Alphanumeric data from given list : %s", alpha_num)
            return alpha_num
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#19. Try to find out multiplication of all numeric value in the individual collection inside dataset
    def Mul(self,L):
        ''' This function finds out multiplication of all numeric value in the individual collection inside dataset '''
        try:
            logging.info("The list entered by user is :  %s", L)
            for i in L:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    mul = 1
                    for j in i:
                        if type(j) == int:
                            mul = mul * j
                    if mul > 1:
                        logging.info("Multiplication of all numeric value in the collection of %s : %s", i,mul)
                        print(mul)
                if type(i) == dict:
                    mul = 1
                    for k, v in i.items():
                        if type(k) == int:
                            mul = mul * k
                        if type(v) == int:
                            mul = mul * v
                    if mul > 1:
                        logging.info("Multiplication of all numeric value in the collection of %s : %s", i, mul)
                        print(mul)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#20. Try to unwrap all the collection inside the collection and create a flat list
    def unwrap(self,L):
        ''' This function unwraps all the collection inside the collection and create a flat list'''
        try:
            logging.info("The list entered by user is :  %s", L)
            l2 = []
            for i in L:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        l2.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        l2.append(k)
                        l2.append(v)
                else:
                    l2.append(i)
            logging.info("Unwrapping all the collection inside the collection: %s", l2)
            return l2

        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e
