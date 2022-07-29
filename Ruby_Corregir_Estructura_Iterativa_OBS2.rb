def each_loop(list)
  list.map! { |item| item + 1}
end

def each_loop2(list)
  list.map! { |item| item + 1}
end

#driver code
p each_loop([1, 4, 2, 10, 9]) == [2, 5, 3, 11, 10]
p each_loop2([10, 20, 30]) == [11, 21, 31]


=begin

- ¿Por qué usar 'map' o 'map!'? Explica brevemente.

El metodo map o map! me entrega un array con el resultado de la operacion que se le aplique al arrays original
El simbolo "!" normalmente indica que la variable toma los valores del resultado pero en este metodo no marca ninguna diferencia.
Se podria utilizar otros metodos como el each, while, do, until o el loop, pero con el map lo puedo hcer en una linea de codigo

=end

