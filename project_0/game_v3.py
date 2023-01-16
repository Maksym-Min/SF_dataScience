import numpy as np

number = np.random.randint(1,101)
print(" Загадонное число number = ", number)

def random_predict_number(number:int) ->int:
    """" Функция угадывания числа

    Args:
        number (int): загаданное число случайно компьютером

    Returns:
        int: количество попыток через которое число было угаданно
    """
    n_from = 1
    n_to=101
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(n_from, n_to)# случайно угадываем число
        #print ('predict_number  = ', predict_number)
        if number > predict_number: # подсказываем что число больше 
            n_from = predict_number 
            #print ('Условие 1: n_from',n_from)
        elif number < predict_number: #   посказываем что число меньше
            n_to = predict_number
            #print ('Условие 2: n_to',n_to)
        elif number == predict_number:
            break # выход из цикла, если угадали
        
       
    print (f'программа угадывает число за {count}')
    return (count)  
    
#Run
random_predict_number(number)
            
            
    
