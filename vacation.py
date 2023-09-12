budget = float(input())
season = input()
location = ""
country = ""
price = 0

if budget <= 1000:
    location = "Camp"
    if season == "Summer":
        country = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        country = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    location = "Hut"
    if season == "Summer":
        country = "Alaska"
        price = 0.8 * budget
    elif season == "Winter":
        country = "Morocco"
        price = 0.6 * budget
else:
    location = "Hotel"
    if season == "Summer":
        country = "Alaska"
    elif season == "Winter":
        country = "Morocco"
    price = 0.9 * budget
print(f"{country} - {location} - {price:.2f}") 