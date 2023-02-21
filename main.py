price_all = 0 # заводим счетчик итоговой суммы.
while True:
    try:
        number_of_tickets = input('Сколько билетов на онлайн-конференцию вы хотите купить? ') # ввод количества билетов.
        number_of_tickets = int(number_of_tickets)# переводим строчное значение в числовое.
        if type(number_of_tickets) == int: # проверка ввода целого числа.
            break
    except ValueError: # вводим исключение
        print('Введите целое число')

for i in range(number_of_tickets):
    i += 1 # добавляем +1, чтобы отсчет шел с 1, а не с нуля
    while True:
        try:
            age_for_ticket = input(f'Введите возраст посетителя - билет №{i}? ') # используем f – строку для введения значения переменной
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if number_of_tickets > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'Сумма к оплате {price_all} руб.')

