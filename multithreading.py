import threading # The module that's used for multithreading, or creating threads in general
import time


class Testament: # The class that has the functions (methods) that will be used in the program later on

    def potentially_first(self):
        time.sleep(2)
        print('potent_1st finished')
    
    def potentially_second(self):
        time.sleep(3)
        print('potent_2nd finished')

    def potentially_third(self):
        time.sleep(4)
        print('potent_3rd finished')

    def attribute_1(self, in1):
        time.sleep(2)
        print(in1)

    def attribute_2(self, in1):
        time.sleep(3)
        print(in1)
    
    def attribute_3(self, in1):
        time.sleep(4)
        print(in1)


test = Testament() # Object


mode = input('Do you want to execute the prints by Multithreading (=) / Basic (-) / Skip (_):   ')
if mode == '=':
    t1 = threading.Thread(target=test.potentially_third) # Creating a thread different from the main one and assigning a function to it
    t2 = threading.Thread(target=test.potentially_second)
    t3 = threading.Thread(target=test.potentially_first)
    t1.start() # Initializing / Calling the function the function inside the thread it's assigned to
    t2.start()
    t3.start()
    print('this should print before the functions if you chose multithreading') # A test - since each function's thread is different from the main one, the string should print before the functions
    t1.join() # A way for threads to pause the main program before the functions inside the threads with ".join()" finish
    t2.join()
    t3.join()
elif mode == '-':
    test.potentially_third() # Standard function call (Without multithreading), takes more time to execute because each function only executes after the previous one
    test.potentially_second()
    test.potentially_first()
    print('this should print before the functions if you chose multithreading') # In this case, the string will only print out after all the functions, because they're all on the same thread
elif mode == '_':
    print('-')
else:
    print('unspecified mode')
mode2 = input('Do you want to execute the attribute tests by Multithreading (=) / Basic (-) / Skip (_):   ')
if mode2 == '=' or '-':
    i1 = input('Input 1:   ') # Input for using it as an attribute in the functions "attribute_ " later
    i2 = input('Input 2:   ')
    i3 = input('Input 3:   ')
    if mode2 == '=':
        t1 = threading.Thread(target=test.attribute_3, args=(i3,)) # Creating a thread for a function, now with an attribute
        t1.start()
        t2 = threading.Thread(target=test.attribute_2, args=(i2,))
        t2.start()
        t3 = threading.Thread(target=test.attribute_1, args=(i1,))
        t3.start()
        print('this should print before the functions if you chose multithreading') # Multithreading test
        t1.join()
        t2.join()
        t3.join()
    elif mode2 == '-':
        test.attribute_3(i3) # Standard function call, now with an attribute
        test.attribute_2(i2)
        test.attribute_1(i1)
        print('this should print before the functions if you chose multithreading') # Multithreading test
elif mode == '_':
    print('-')
else:
    print('unspecified mode')
