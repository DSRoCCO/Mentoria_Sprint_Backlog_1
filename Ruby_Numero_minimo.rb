
def min(list)
  result  = [] << list[0]
  list.each {|num| result << num if num < result[-1]}
  result[-1]
end

#Driver code

p min([-20, -10, 0, 10, 20]) == -20
p min([1, 2, 3, 4, 5]) == 1
p min([5, 4, 3, 2, 1]) == 1
