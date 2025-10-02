def reverse_words(sentence):
   """Accepts a string, returns a sentence with the words reversed."""
   # 1. Split the sentence into a list of words
   words = sentence.split()
   # 2. Reverse the order of the words list
   words.reverse() # or words[::-1]
   # 3. Join the words back into a single string with spaces
   reversed_sentence = " ".join(words)
   return reversed_sentence
# Example Usage:
input_sentence = "We are ready"
reversed_output = reverse_words(input_sentence)
print(f"\n--- Reverse Words in Sentence ---")
print(f"Original: '{input_sentence}'")
print(f"Reversed: '{reversed_output}'")