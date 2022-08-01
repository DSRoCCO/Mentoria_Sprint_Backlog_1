#driver code
def nested_array(lista, factor)
  result = []
  lista.each do |value|
    (1..factor).each do |number|
      result << [value, number]
    end
  end
  result
end

p nested_array(["uno", "dos", "tres", "cuatro"], 3) == [["uno", 1], ["uno", 2], ["uno", 3], ["dos", 1], ["dos", 2], ["dos", 3], ["tres", 1], ["tres", 2], ["tres", 3], ["cuatro", 1], ["cuatro", 2], ["cuatro", 3]]
p nested_array(["cinco"], 4) == [["cinco", 1], ["cinco", 2], ["cinco", 3], ["cinco", 4]]
