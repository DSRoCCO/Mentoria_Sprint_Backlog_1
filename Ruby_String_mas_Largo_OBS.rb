#longest method
def longest(mi_array)
  max = mi_array[0].length
  result = []
  mi_array.each {|dato| max = dato.length if dato.length > max}
  mi_array.each {|dato| result.push(dato) if dato.length == max}
  result
end

"""Metodo Enumerable"""
def longest2(mi_array)
  max = mi_array[0].length
  result = []
  mi_array.each {|dato| max = dato.length if dato.length > max}
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
