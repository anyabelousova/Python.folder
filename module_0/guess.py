import numpy as np

def game_core_v3(number):
    '''Сначала устанавливаем любое random число.
       Отслеживаем расстояние до загаданного числа.'''
    count = 1
    distance = 25
    predict = 50
    while number != predict:
        count+=1
        if distance == 0: #округлить в большую сторону на последнем шаге
            distance = 1 
        if number > predict: 
            predict += distance
        elif number < predict: 
            predict -= distance
        distance = distance//2 #делим отрезок пополам
        
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


#оцениваем нашу версию
score_game(game_core_v3) 
