
#Basics !!!

# 1 Ask user for temperature in Celsius → convert to Fahrenheit, Hint: °F = (°C × 9/5) + 32
celsius_temp = (float(input("Enter temperature in Celsius: "))) #float converts default string input into real number
fahrenheit_temp = (celsius_temp * 9/5) + 32
print(f"{fahrenheit_temp}°F")

#2 Ask for product price and discount percentage → calculate final price Hint: final = price × (1 − discount/100)
product_price, discount_percentage = float(input("Enter product price: ")), float(input("Enter discount percentage: "))  #Asking both input on same line
final_price = product_price * (1 - discount_percentage/100)
print(f"Final price: {final_price}")

#3 Ask user for exam marks → calculate average Hint: avg = (m1 + m2 + m3) / 3
marks = list(map(float,input("Enter three marks: ").split())) #mapping float to each input item separated by space and listing them to marks list.
average_marks = sum(marks) / len(marks)
print(f"Average Marks: {average_marks}")

#4 Ask for length and width of rectangle → calculate area and perimeter Hint: area = length × width, perimeter = 2 × (length + width)
length, width = map(float, input("Enter length and width separated by space ... ").split()) #taking both input and mapping float before calculating the area and perimeter.
print("Area", length * width)
print("Perimeter", 2 * (length + width))

#5 Ask price per kg and how many kg → calculate total cost Hint: total = price_per_kg × weight
rate, quantity = map(float, input("Enter price per kg and quantity separated by comma ... ").split(","))
print("total = ", rate * quantity)
