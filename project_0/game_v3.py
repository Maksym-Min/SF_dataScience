import numpy as np

number = np.random.randint(1,101)
print(" Загадонное число number = ", number)

def game_score_v3(number:int=1) ->int:
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
        
       
    
    return (count)  
    

def score_game(game_score_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_score_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return (score)    
#run
score_game(game_score_v3)