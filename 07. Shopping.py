budget = float(input())
videocards_number = int(input())
processors_number = int(input())
RAM_chips_number = int(input())

videocard = 250.00
processor = 0.35 * videocard * videocards_number
RAM_chip = 0.1 * videocard * videocards_number

#Ако броя на видеокартите е по-голям от този на
# процесорите получава 15% отстъпка от крайната сметка.

expenses = videocard * videocards_number + \
    processor * processors_number +\
    RAM_chip * RAM_chips_number

if videocards_number > processors_number:
    expenses = expenses * 0.85

if budget >= expenses:
    print(f"You have {budget - expenses:.2f} leva left!")

else:
    print(f"Not enough money! You need {expenses - budget:.2f} leva more!")