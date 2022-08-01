
def subarray_index(array, factor)
  result = []
  array.each {|letter| result << [letter , (1..factor).to_a]}
  result
end

#Driver code

p subarray_index(["c", "b", "a"], 2) == [["c", [1, 2]], ["b", [1, 2]], ["a", [1, 2]]]
p subarray_index(["a"], 3) == [["a", [1, 2, 3]]]
