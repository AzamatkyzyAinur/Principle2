def reverse_words(sentence):
   words = sentence.split()
   words.reverse()
   reversed_sentence = " ".join(words)
   return reversed_sentence
input_sentence = input("Enter a sentence: ")
reversed_output = reverse_words(input_sentence)
print("\n--- Reverse Words in Sentence ---")
print(f"Original: '{input_sentence}'")
print(f"Reversed: '{reversed_output}'")