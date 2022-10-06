#Ejercicio - Refactoring temperature

def temperature(grade)
  indice = 0
  values = [(0..5), (6..10), (11..15), (16..20), (21..25), (26..30), (31..35), (36..40)]
  values.each_with_index {|value, i| indice = i if value.to_a.include?(grade) }

  indice > 0 ? "Temperature is between #{values[indice].min} and #{values[indice].max}" : "Temperature is greater than 40"

end

# Driver code

p temperature(23) == "Temperature is between 21 and 25"
p temperature(45) == "Temperature is greater than 40"
p temperature(34) == "Temperature is between 31 and 35"
