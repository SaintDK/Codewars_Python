def check_coupon(entered_code, correct_code, current_date, expiration_date):
    answer = []  # Сделаем answer списком

    if entered_code == correct_code:
        current_date = current_date.replace(",", " ").split()
        answer = [int(i) for i in current_date if i.isdigit()]
        if current_date <= expiration_date:  # Проверьте, не истек ли купон
            print("Coupon is valid.")
        else:
            print("Coupon has expired.")
        print(answer)  # Печатаем только число

# Вызов функции
check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014')