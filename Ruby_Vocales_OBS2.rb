#vowels method

def vowels(word)
  counter = word.split(//).count { |letter| %w[a e i o u].include?(letter.downcase)}
end

def vowels2(word)
  word.downcase.count "\\aeiou"
end


#Driver code

p vowels("hello") == 2
p vowels("Magic") == 2
p vowels("Apologize") == 5


p vowels2("hello") == 2
p vowels2("Magic") == 2
p vowels2("Apologize") == 5


=begin

- Investiga método de ruby que te permite evitar el uso del método 'split' y la iteración.
Metodo Count aplicado directamente


=end
