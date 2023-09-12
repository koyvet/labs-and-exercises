juniors_num = int(input())
seniors_num = int(input())
trace = input()
tax = 0

if trace == "trail":
    tax = juniors_num * 5.50 + seniors_num * 7
elif trace == "cross-country":
    if (juniors_num + seniors_num) >= 50:
        tax = 0.75 *(juniors_num * 8 + seniors_num * 9.50)
    else:
        tax = juniors_num * 8 + seniors_num * 9.50
elif trace == "downhill":
    tax = juniors_num * 12.25 + seniors_num * 13.75
elif trace == "road":
    tax = juniors_num * 20 + seniors_num * 21.50
expenses = 0.05 * tax
print(f"{(tax - expenses):.2f}")