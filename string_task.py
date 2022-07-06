'''
#1. Try to filter out all the vowels form given text by using while loop
#2. Try to write a fun which will take string and return a len of it without using a inbuilt fun len
'''
import logging
logging.basicConfig(filename="string_test.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class String_task:

# 1. Try to filter out all the vowels form given text by using while loop
    def extract_vowels(self, s):
        "This function filter out all the vowels form given text "
        try:
            logging.info("Text entered by user : %s", s)
            l=[]
            i=0
            while i < len(s):
                if s[i].lower() in 'aeiou':
                    l.append(s[i])
                i = i + 1
            logging.info("All the vowels form given text : %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


#2. Try to write a fun which will take string and return a len of it without using a inbuilt fun len
    def string_length(self, s):
        ''' This function returns a length of it without using a inbuilt fun len '''
        try:
            logging.info("String entered by user : %s",s)
            length = 0
            for i in s:
                length += 1
            logging.info("String length : %s",length)
            return length
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e
