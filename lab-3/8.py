def fahrenheit_to_centigrade(fahrenheit):
   """Calculates and displays the equivalent centigrade temperature."""
   # Conversion formula: C = (5 / 9) * (F – 32)
   centigrade = (5 / 9) * (fahrenheit - 32)
   print(f"--- Temperature Conversion ---")
   print(f"{fahrenheit}°F is equivalent to {centigrade:.2f}°C.")
   return centigrade
# Example Usage:
f_temp = 68
fahrenheit_to_centigrade(f_temp)