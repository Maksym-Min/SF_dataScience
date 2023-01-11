import numpy as np


def random_predict(number: int = 1) -> int:
    """рандомно угадываем число
    argЖnumber -  загаданное число, по умодчанию 1
    return:
        int число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предпологаемо число
        if number == predict_number:
            break  # выход из цикла, если угадали
    return (count)
    print(f' Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """ за кокае количество попыток в среднем из 1000 проходов
    угадывает наш алгоритм

    arg:
    random_predic([type]): функция угадывания
    return:
    int: среднее число попыток"""
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводительности
    random_array = np.random.randint(1, 101, size=(1000))  # pfuflfkb список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))  # находит среднее число
    print(f' ваш алгоритм угадывает число в среднем за :{score} попыток')
    return (score)

#if __name__ in '_main_':
    # run
score_game(random_predict)