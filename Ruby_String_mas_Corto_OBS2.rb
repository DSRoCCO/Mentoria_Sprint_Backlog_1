#shortest method

def shortest(mi_array)
  min = mi_array[0].length
  result = []
  mi_array.each {|dato| min = dato.length if dato.length < min}
  mi_array.each {|dato| result << dato if dato.length == min}
  result
end

""" Metodos Enumerables"""
def shortest2(mi_array)
  min = mi_array[0].length
  mi_array.each {|dato| min = dato.length if dato.length < min}
  mi_array.select {|arr| arr.length == min}
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

=begin

- ¿Es necesario usar la variable 'result'?

 No, las funciones en ruby devuelven el resultado de la ultima linea de codigo


- ¿Para aplicar el método 'select' es necesario volver a llamar al arreglo 'mi_array?

No, se corrigio.


- ¿Cuál es la opción rubista del método 'push'?

Se puede usar el push o el append pero el metodo rubista seria "<<""

=end


