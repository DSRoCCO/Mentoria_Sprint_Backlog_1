#vowels method

def vowels(word)
  counter = word.split(//).count { |letter| %w[a e i o u].include?(letter.downcase)}
end


#Driver code

p vowels("hello") == 2
p vowels("Magic") == 2
p vowels("Apologize") == 5

