puts "-"*10 + "sum methods"+"-"*10
#sum methods
def metodo1(num)
  num + num + num + num
end

def metodo2(num)
  num + num
end

#driver code
puts metodo1(3) == metodo2(6)

puts "-"*10 + "subtraction methods"+"-"*10
#subtraction methods
def metodo3(num1, num2)
  num = num2 - num1
end

def metodo4(num1, num2)
  num1 - num2 - 4
end
#driver code
puts metodo3(4, 6) == metodo4(9, 3)

puts "-"*10 + "combined arithmetic expression (all arithmetic operation methods)"+"-"*10
#combined arithmetic expression (all arithmetic operation methods)
def metodo5(*args)
  (args[0] * args[1]) - (args[2]/args[1])+ args [0]
end

def metodo6(*args)
  (args[0] * args[1]) - (args[3]/args[0])+ args[2]
end
#driver code
puts metodo5(3, 7, 8, 2) == metodo6(3, 8, 2, 9)

puts "-"*10 + "multiplication methods"+"-"*10
#multiplication methods
def metodo7(num1, num2)
  num1 * num2  #782
end

def metodo8(num1, num2)
  num1*(num1*5 + num2*3) - (num1 - num2)
end

#driver code
puts metodo7(23, 34) == metodo8(12, 2)


#division & module methods
puts "-"*10 + "division & module methods"+"-"*10
def metodo9(num1, num2, num3)
  (num3.to_f / num2 * num1 * num1).floor
end

def metodo10(num1, num2, num3)
  (num3.to_f / num2 * num1).floor
end
#driver code
puts metodo9(2, 4, 6) == metodo10(4, 6, 10)

puts "-"*10 + "joining strings method"+"-"*10
#joining strings method
def metodo11(word)
  word = word.downcase
  "Te mando #{word} Marcos"
end

#driver code
puts metodo11("Saludos") == "Te mando saludos Marcos"
