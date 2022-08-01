def join_arrays(array1, array2)
  n1 = array1.length()
  result = array1.union(array2)
  n = 2
  result.each_with_index do |value,index|
    if index >= n1
      result[index] = [value, [n]]
      n+=1
    end
  end
  result
end

#Driver code

p join_arrays([1, 2, 3], [4, 5, 6]) == [1, 2, 3, [4, [2]], [5, [3]], [6, [4]]]
p join_arrays(['a', 'b', 'c'], ['d', 'e', 'f']) == ['a', 'b', 'c', ['d', [2]], ['e', [3]], ['f', [4]]]

