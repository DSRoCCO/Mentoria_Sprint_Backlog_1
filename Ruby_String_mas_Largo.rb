#longest method
def longest(mi_array)
  max = 0
  result = []
  for dato in mi_array
    max = dato.length if dato.length > max
  end

  for word in mi_array
    result.push(word) if word.length == max
  end
  return result
end

"""Metodo Enumerable"""
def longest2(mi_array)
  max = 0
  for dato in mi_array
    max = dato.length if dato.length > max
  end
  result = mi_array.select {|arr| arr if arr.length == max}
end

#Driver code

p longest(['tres', 'pez', 'alerta', 'cuatro', 'tesla', 'tropas', 'siete']) == ["alerta", "cuatro", "tropas"]
p longest(['gato', 'perro', 'elefante', 'jirafa']) == ["elefante"]
p longest(['verde', 'rojo', 'negro', 'morado']) == ["morado"]

p "Metodo Enumerable"
p longest2(['tres', 'pez', 'alerta', 'cuatro', 'tesla', 'tropas', 'siete']) == ["alerta", "cuatro", "tropas"]
p longest2(['gato', 'perro', 'elefante', 'jirafa']) == ["elefante"]
p longest2(['verde', 'rojo', 'negro', 'morado']) == ["morado"]
