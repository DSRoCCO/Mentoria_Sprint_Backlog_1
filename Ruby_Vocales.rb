#vowels method
def vowels(word)
  count = 0
  for letter in word.split("")
    count += 1 if ["a", "e", "i", "o", "u"].include?(letter.downcase)
  end
  return count
end


#Driver code

p vowels("hello") == 2
p vowels("Magic") == 2
p vowels("Apologize") == 5
