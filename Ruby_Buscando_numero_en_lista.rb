#numbers method

def numbers(lista, number)
  lista.include?(number)
end

#Driver code

p numbers([1, 3, 5, 7, 9, 11], 5) == true
p numbers([1, 50, 24, 7, 9, 100], 25) == false
p numbers([11, 33, 55, 77, 99, 11], 33) == true
p numbers([20, 43, 55, 77, 99, 40], 43) == true
