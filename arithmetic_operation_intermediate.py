
#Intermediate !!!


import math #to use math.log for the calculation
from datetime import datetime

# 1 Paint cost estimator.
# Ask user for room dimensions, doors/windows area, coats, paint price & coverage → calculate total cost
# Hint: Total area = 2×(L×H + W×H) − exclusions  #Total Liters required = (area × coats) / coverage_per_liter  #Cost = liters × price_per_liter

try:
    #asking room dimensions
    r_length, r_width, r_height = float(input("Enter room Length: ")), float(input("Enter room Width: ")), float(input("Enter room Height: "))
    #asking door/windows dimensions
    d_width, d_height = float(input("Enter door width: ")), float(input("Enter door height: "))
    w_width, w_height = float(input("Enter window width: ")), float(input("Enter window height: "))
    #asking paint cost, painting method, coverage
    paint_price = float(input("Enter paint price/ltr: "))
    coats = int(input("Enter number of coats: "))
    coverage = int(input("Enter the coverage of the wall in sq feet by per liter paint: "))

    #calculation of area of room,door and windows
    r_area = float(2*(r_length*r_width + r_width*r_height))
    d_area = float(2*(d_height*d_width))
    w_area = float(2*(w_height*w_width))
    #calculation of area to paint
    total_area = r_area - d_area - w_area
    #calculation of total paint required in liters
    total_liters = (total_area*coats)/coverage
    #calculation of total cost to paint the room
    total_cost = total_liters*paint_price
    print("Total cost: $" + str(total_cost))
except ValueError:
    print(ValueError)

# 2 Body Fat Percentage (US Navy Method – Men)
# Ask height (cm), waist (cm), neck (cm) → estimate body fat percentage
# Hint: %BF = 86.010 × log₁₀(waist − neck) − 70.041 × log₁₀(height) + 36.76

#taking input of height, waist, neck of a man on float data type
m_height, m_waist, m_neck = float(input("Enter height in cm ")), float(input("Enter waist measurement in cm ")), float(input("Enter neck measurement in cm "))
body_fat_per = round(495/(1.0324-0.19077 * math.log10(m_waist-m_neck) + 0.15456 * math.log10(m_height))-450,2)
print(f"Body fat percentage: {body_fat_per}")


# 3 Age in Different Time Units
# Ask date of birth of user and identify how what is his exact age, like how old year, months, days.
# Asking date of birth form user

d = datetime.strptime(input("YYYY-MM-DD: "), "%Y-%m-%d")
n = datetime.now()

years = n.year - d.year - ((n.month, n.day) < (d.month, d.day))
months = (n.month - d.month - (n.day < d.day)) % 12
days = (n - d.replace(year=n.year, month=n.month)).days

print(f"{years}y {months}m {days}d")

# 4 Loan EMI Calculator (Monthly Installment)
#Ask loan amount, annual interest rate (%), tenure in years → calculate EMI
#Hint: EMI = P × r × (1+r)^n / ((1+r)^n − 1)

p = float(input("Loan Amount: ")) #principal amount
r = float(input("Annual Rate (%): ")) / 1200 #annual rate/ interest rate
n = float(input("Years: ")) * 12 #loan tenure

emi = p * r * (1+r)**n / ((1+r)**n - 1)
print(f"\nEMI = $ {emi:,.2f}/month")



#5 Weighted GPA Calculator (4.0 Scale)
#Ask marks + credit hours for 5 subjects → calculate weighted GPA
#Hint: Grade points: 90–100 → 4.0, 80–89 → 3.0, 70–79 → 2.0, 60–69 → 1.0, below 60 → 0.0 #GPA = Σ(grade_points × credit_hours) / Σ(credit_hours)
total_gp = 0
total_cr = 0
for i in range(5):
    marks = float(input(f"Subject {i + 1} marks: "))
    credit = float(input(f"Subject {i + 1} credits: "))

    gp = 4.0 if marks >= 90 else \
        3.0 if marks >= 80 else \
            2.0 if marks >= 70 else \
                1.0 if marks >= 60 else 0.0

    total_gp += gp * credit
    total_cr += credit

print(f"\nGPA = {total_gp / total_cr:.2f}")