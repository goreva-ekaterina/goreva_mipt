# Не помню, лучшее ли это решение, но самое напрашивающееся. Делим отрезки пополам, пока не найдем
import math
def predict_number(number):
  # раз загадывают от 1 до 100, берем сразу среднее
  x = 50
  highest = 100
  count = 0
  while True:
    # мы уже предположили, что икс чему-то равен, значит первая попытка пошла
    count +=1
    if x == number:
      break
    if x > number:
      # нет уверенности, что это необходимо - округлять куда-нибудь. Но нечетные числа дадут дроби и тут надо думать. Интуитивно может помочь,
      # а там на практике проверим будут ли ошибки. Округляем в большую сторону. Кажется, что тут и round справился бы, десятичная часть то будет
      # всегда 0 или 5.
      # Переназначаем верхнюю границу.
      highest = x
      x = math.ceil(x/2)
    if x < number:
      x = math.ceil((x + highest)/2)
  return count

def score_game(predict_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    # в данном случае нет необходимости - количество попыток не превысит 20 штук
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    # выводим их на экран, потому что черный ящик нервирует меня
    print(random_array[0:5])

    for number in random_array:
        count_ls.append(predict_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


score_game(predict_number)