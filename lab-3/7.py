def grams_to_ounces(grams):
   ounces = grams / 28.3495231
   print(f"--- Grams to Ounces ---")
   print(f"{grams} grams is equivalent to {ounces:.4f} ounces.")
   return ounces
grams_weight = float(input("Enter weight in grams: "))
grams_to_ounces(grams_weight)