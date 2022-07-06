''' Tuple tasks:
#1. Try to extract all tuple entities from given list
'''
import logging
logging.basicConfig(filename="tuple_test.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class Tuple_task:

#1. Try to extract all tuple entities from given list
    def extract_tuple(self,L):
        ''' This function extract all tuple entities from given list'''
        try:
            logging.info("List entered by user : %s", L)
            l=[]
            for i in L:
                if type(i)==tuple:
                    l.append(i)
            logging.info("Extracted tuple entities : %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e