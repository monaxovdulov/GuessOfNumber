"""
Игра УГАДАЙ ЧИСЛО 
1. Поздороваться с игроком, спросить его имя, если игрок не ввёл имя задать ему имя ‘анонимус’. 

2. Объяснить игроку правила игры.

3. Задать случайное число из выбранного диапазона. Например от 1 до 100.

4. Попросить у игрока ввести число и если число не в заданном нами диапазоне, то просить ввести игрока число до тех пор пока, он не введёт корректное значение.

5. Если игрок не угадал, информировать его, является ли его число больше или меньше загаданного.

6. Если игрок угадал, поздравить с победой и написать количество попыток за которое он справился.

7. Спросить хочет ли игрок сыграть ещё раз, если “да”, то перейдём снова к пункту 3, если нет, то попрощатся с игроком, иначе добиться ответа да или нет🙂
"""

import random

print("Привет, это игра Угадай Число ")
name_player = input("Как тебя зовут?\nВводить сюда:>")

if name_player == "":
  name_player = "АНОНИМУС"
  
print("Итак",name_player)

print("""правила игры: я загадываю число от 1 до 100,
а ты угадываешь,
я буду тебе подсказывать,
больше или меньше твое число по сравнению с загаданным 
""")

game = True

while game:
  guess_number = random.randint(1, 100)
  player_number = None
  attempts = 0
  while guess_number != player_number:
    player_number = int(input("Угадай число из диапазона от 1 до 100\nВводить сюда:>"))
    attempts += 1
    while player_number < 1 or player_number > 100:
      print("число",player_number, "не в диапазоне от 1 до 100")
      player_number = int(input("Угадай число из диапазона от 1 до 100\nВводить сюда:>"))
    
    if guess_number != player_number:
    
      if guess_number < player_number:
        print("Загаданное число меньше числа ", player_number)
      else: 
         print("Загаданное число больше числа ", player_number)
    else: 
      print(name_player.capitalize() ,"поздравляю с победой! Вы отгадали, было загадано", guess_number)
      print("Ваше количество попыток", attempts)
  
      player_answer = input("Хотите ли вы сыграть ещё раз, (да/нет)\nВводить сюда:>").lower()
      while player_answer not in ("да", "нет"):
        print("Некорректный ввод!")
        player_answer = input("Хотите ли вы сыграть ещё раз, (да/нет)\nВводить сюда:>").lower()
      if player_answer == "да":
        print("Вы выбрали начать снова!")
      else:
        print("До свидания!")
        game = False
        
      
    
    