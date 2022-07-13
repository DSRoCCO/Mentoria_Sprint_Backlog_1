#user method
def user()
  word = "zero"
  count = 0
  while word != "Ya"
    print 'Escriba su palabra :'
    word = gets.chomp
    count += 1
  end
  return count
end


#driver code

#=> Ejemplo de entradas
#>uno
#>dos
#>tres
#>cuatro
#>cinco
#>seis
#>Ya

#=> Número de entradas del usuario: 7
p user
#=> 7
