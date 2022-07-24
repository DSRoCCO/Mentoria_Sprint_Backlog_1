def each_loop(list)
  list.map! { |item| item + 1}
end

def each_loop2(list)
  list2 = list.map { |item| item + 1}
end

#driver code
p each_loop([1, 4, 2, 10, 9]) == [2, 5, 3, 11, 10]
p each_loop2([10, 20, 30]) == [11, 21, 31]
