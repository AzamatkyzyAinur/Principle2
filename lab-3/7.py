def grams_to_ounces(grams):
   """Converts a weight from grams to ounces."""
   # Conversion factor: 1 ounce = 28.3495231 grams
   ounces = grams / 28.3495231
   return ounces
# Example Usage:
grams_weight = 100
ounces_weight = grams_to_ounces(grams_weight)
print(f"--- Grams to Ounces ---")
print(f"{grams_weight} grams is equivalent to {ounces_weight:.4f} ounces.")