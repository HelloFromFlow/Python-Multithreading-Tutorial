import threading
import time


class Testament: # Класс, в котором будут содержатся далее используемые в программе функции

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


test = Testament() # Экземпляр / Переменная класса


mode = input('Do you want to execute the prints by Multithreading (=) / Basic (-) / Skip (_):   ')
if mode == '=':
    t1 = threading.Thread(target=test.potentially_third) # Создание отдельного от основного потока для функции
    t2 = threading.Thread(target=test.potentially_second)
    t3 = threading.Thread(target=test.potentially_first)
    t1.start() # Инициализация / Старт функции внутри своего потока
    t2.start()
    t3.start()
    print('this should print before the functions if you chose multithreading') # Проверка - так как для каждой функции поток отдельный от основного, этот принт должен вывестить до исполнения функций
    t1.join() # Функция для потоков, при которой основной поток не воспроизведётся пока функции не исполнятся до конца
    t2.join()
    t3.join()
elif mode == '-':
    test.potentially_third() # Стандартный вызов функции (Без многопоточности), занимает больше времени для исполнения т.к. каждая следующая функция исполняется после предыдущей
    test.potentially_second()
    test.potentially_first()
    print('this should print before the functions if you chose multithreading') # В данном случае, принт выведется только после всех функций, так как они все происходят в основном потоке
elif mode == '_':
    print('-')
else:
    print('unspecified mode')
mode2 = input('Do you want to execute the attribute tests by Multithreading (=) / Basic (-) / Skip (_):   ')
if mode2 == '=' or '-':
    i1 = input('Input 1:   ') # Ввод для использования его как аттрибут для функций далее
    i2 = input('Input 2:   ')
    i3 = input('Input 3:   ')
    if mode2 == '=':
        t1 = threading.Thread(target=test.attribute_3, args=(i3,)) # Создание потока для функции, в этот раз с передаваемым аргументом
        t1.start()
        t2 = threading.Thread(target=test.attribute_2, args=(i2,))
        t2.start()
        t3 = threading.Thread(target=test.attribute_1, args=(i1,))
        t3.start()
        print('this should print before the functions if you chose multithreading') # Проверка
        t1.join()
        t2.join()
        t3.join()
    elif mode2 == '-':
        test.attribute_3(i3) # Стандартный вызов функции с передаваемым аттрибутом
        test.attribute_2(i2)
        test.attribute_1(i1)
        print('this should print before the functions if you chose multithreading') # Проверка
elif mode == '_':
    print('-')
else:
    print('unspecified mode')