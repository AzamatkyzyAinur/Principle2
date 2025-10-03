def fahrenheit_to_centigrade(fahrenheit):
   centigrade = (5 / 9) * (fahrenheit - 32)
   print(f"--- Temperature Conversion ---")
   print(f"{fahrenheit}°F is equivalent to {centigrade:.2f}°C.")
   return centigrade
f_temp = float(input("Enter temperature in Fahrenheit: "))
fahrenheit_to_centigrade(f_temp)