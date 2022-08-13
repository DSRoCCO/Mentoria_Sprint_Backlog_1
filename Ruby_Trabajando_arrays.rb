# Method to return the first n elements of the array
def first_n(list, n)
  list.first(n)
  #list[0...n]
end

# Method to drop the first n elements of the array
def drop_n(list, n)
  list.drop(n)
end

# Method to add `element` to the end of the array method
def end_arr_add(list, n)
  list.push(n)
  #list<<n
end

# Method to add `element` to the beginning of the array method
def begin_arr_add(list, n)
  list.unshift(n)
end

# Method to add `element` at position `index` to the array method
def index_arr_add(list, i, n)
  list.insert(i,n)
  #list[i] = n
end

# Method to add any two elements to the arr at the index method
def index_arr_multiple_add(list, i, n, m)
  list.insert(i, n, m)
end

# Method to delete the element from the end of the array method
def end_arr_delete(list)
  list.pop
end

# Method to delete the element at the beginning of the array and return the deleted element method
def start_arr_delete(list)
  list.shift
end

# Method to delete the element at the position 'index' method
def delete_at_arr(list, n)
  list.delete_at(n)
  list
end

# Method to delete all the elements of the array where element = val method
def delete_all(list, n)
  list.delete(n)
  list
end


#driver code
puts "Method to return the first n elements of the array"

p first_n([1, 4, 3, 6, 5], 3) == [1, 4, 3]

puts "Method to drop the first n elements of the array"

p drop_n([1, 4, 3, 6, 5], 3) == [6, 5]

puts "Method to add `element` to the end of the array method"

p end_arr_add([1, 4, 3, 6, 5], 20) == [1, 4, 3, 6, 5, 20]

puts "Method to add `element` to the beginning of the array method"

p begin_arr_add([1, 4, 3, 6, 5], 34) == [34, 1, 4, 3, 6, 5]

puts "Method to add `element` at position `index` to the array method"

p index_arr_add([1, 4, 3, 6, 5], 2, 100) == [1, 4, 100, 3, 6, 5]

puts "Method to add any two elements to the arr at the index method"

p index_arr_multiple_add([1, 4, 3, 6, 5], 3, 34, 23) == [1, 4, 3, 34, 23, 6, 5]

puts "Method to delete the element from the end of the array method"

p end_arr_delete([1, 4, 3, 6, 5]) == 5

puts "Method to delete the element at the beginning of the array and return the deleted element method"

p start_arr_delete([1, 4, 3, 6, 5]) == 1

puts "Method to delete the element at the position 'index' method"

p delete_at_arr([1, 4, 3, 6, 5], 2) == [1, 4, 6, 5]

puts "Method to delete all the elements of the array where element = val method"

p delete_all([1, 4, 3, 6, 5], 6) == [1, 4, 3, 5]

