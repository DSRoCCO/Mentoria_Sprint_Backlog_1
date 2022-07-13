#replace_vowels method
def replace_vowels(mi_array)
  for word in mi_array
    for letter in word.split("")
      letter = x if ["a", "e", "i", "o", "u"].include?(letter.downcase)
      word2+=letter
    end
    array2.push(word2)
  end
  return array2
end

#Driver code

p replace_vowels(["banana", "apple"]) == ["bxnxnx", "xpplx"]
