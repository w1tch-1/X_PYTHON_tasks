result = 0
convert_choosing = input('1. дюйми\n'
                         '2. ярди\n'
                         '3. милі\n'
                         'Виберіть, що ви хочете конвертувати:')


if convert_choosing == '1':
    feet = float(input("Введіть відстань у футах: "))
    inches = feet * 12
    result = f"{feet} футів = {inches} дюймів"
elif convert_choosing == '2':
    feet = float(input("Введіть відстань у футах: "))
    yards = feet * 0.333333333
    result = f"{feet} футів = {yards} ярдів"
elif convert_choosing == '3':
    feet = float(input("Введіть відстань у футах: "))
    miles = feet * 0.000189393939
    result = f"{feet} футів = {miles} миль"


print(result)
