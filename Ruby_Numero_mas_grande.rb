#Driver code
def max(list)
  result  = [] << list[0]
  list.each {|num| result << num if num > result[-1]}
  result[-1]
end


p max([-20, -10, 0, 10, 20]) == 20
p max([1, 2, 3, 4, 5]) == 5
p max([5, 4, 3, 2, 1]) == 5
