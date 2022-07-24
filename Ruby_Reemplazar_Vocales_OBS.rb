#replace_vowels method

def replace_vowels(mi_array)
  mi_array.each {|word| word.tr!('aeiou','x')}
end


#Driver code

p replace_vowels(["banana", "apple"]) == ["bxnxnx", "xpplx"]
