#mode method
def mode(lista)
  maxi = Hash.new
  lista.each do |value|
    unless maxi.keys.include?(value)
      maxi[value]=lista.count(value)
    end
  end
  result = []
  maxi.values.each_with_index {|value,index| result << maxi.keys[index] if value == (maxi.values).max}
  result

end

#Driver code

p mode([1, 2, 2, 3]) == [2]
p mode([1, 2, 2, 3, 3, 4]) == [2, 3]
p mode([1, 2, 3]) == [1, 2, 3]
p mode([0, 1, 2, 3, 4, 0]) == [0]
