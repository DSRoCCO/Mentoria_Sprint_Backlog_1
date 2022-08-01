#get_index method
def get_index(lista)
  result = []
  lista.each {|dato| result << [dato, lista.index(dato)]}
  result
end

def get_index2(lista)
  result = []
  lista.each_with_index { |dato, index| result << [dato, index]}
  result
end


#Driver code
p get_index([2, 10, 6, 34, 0, 3]) == [[2, 0], [10, 1], [6, 2], [34, 3], [0, 4], [3, 5]]
p get_index2([2, 10, 6, 34, 0, 3]) == [[2, 0], [10, 1], [6, 2], [34, 3], [0, 4], [3, 5]]

