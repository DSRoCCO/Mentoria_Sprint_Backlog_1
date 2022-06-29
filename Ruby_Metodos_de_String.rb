word1 = "Hello World!"
n = 40
puts "-"*10 + "Uso de downcase" + "-"*10
metodo1 = word1[0,4]
metodo2 = metodo1.downcase == "hell"
puts metodo2 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de include?" + "-"*10
metodo3 = word1.include?(metodo1) == true
puts metodo3 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de to_s and capitalize" + "-"*10
metodo4 = metodo3.to_s.capitalize == "True"
puts metodo4 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de to_s and length" + "-"*10
metodo5 = metodo4.to_s.length == 4
puts metodo5 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de to_s and split" + "-"*10
metodo6 = metodo5.to_s.split(//) == ["t", "r", "u", "e"]
puts metodo6 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de to_s and downcase" + "-"*10
metodo7 = metodo6.to_s.split(//)
metodo8 = metodo7[1] = "h"
puts metodo7 == ["t", "h", "u", "e"]
#=> true
puts "-"*n


puts "-"*10 + "Uso de join" + "-"*10
metodo9 = metodo7.join == "thue"
puts metodo9 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de to_s & include" + "-"*10
metodo10 = metodo9.to_s.include?("t") == true
puts metodo10 == true
#=> true
puts "-"*n

puts "-"*10 + "Uso de ppcase y reverse" + "-"*10
metodo11 = metodo7.join.upcase.reverse == "EUHT"
puts metodo11 == true
#=> true
puts "-"*n

