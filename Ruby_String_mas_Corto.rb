#shortest method

def shortest(mi_array)
  min = 100
  result = []
  for dato in mi_array
    min = dato.length if dato.length < min
  end

  for word in mi_array
    result.push(word) if word.length == min
  end

  return result
end

""" Metodos Enumerables"""
def shortest2(mi_array)
  min = 100
  for dato in mi_array
    min = dato.length if dato.length < min
  end
  result = mi_array.select {|arr| arr if arr.length == min}
end

#Driver code
p shortest(['uno', 'dos', 'tres', 'cuatro', 'cinco']) == ["uno", "dos"]
p shortest(['gato', 'perro', 'elefante', 'jirafa']) == ["gato"]
p shortest(['verde', 'rojo', 'negro', 'morado']) == ["rojo"]


#Driver code
p "Con Metodo Enumerable"
p shortest2(['uno', 'dos', 'tres', 'cuatro', 'cinco']) == ["uno", "dos"]
p shortest2(['gato', 'perro', 'elefante', 'jirafa']) == ["gato"]
p shortest2(['verde', 'rojo', 'negro', 'morado']) == ["rojo"]
