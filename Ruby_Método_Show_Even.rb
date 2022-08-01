#show_even method

def show_even(lista)  # con each
  result = []
  lista.each {|dato| result << (dato + 2) if (dato + 2).even?}
  result
end

def show_even2(lista)  # con metodos enumerables
  lista.filter_map{|dato| (dato + 2) if (dato + 2).even?}
end

#driver code
p show_even([4, 6, 8, 10, 23, 45, 56, 2]) == [6, 8, 10, 12, 58, 4]
p show_even([12, 34, 21, 1, 2, 7, 89]) == [14, 36, 4]


p show_even2([4, 6, 8, 10, 23, 45, 56, 2]) == [6, 8, 10, 12, 58, 4]
p show_even2([12, 34, 21, 1, 2, 7, 89]) == [14, 36, 4]
