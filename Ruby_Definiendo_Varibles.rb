puts "-"*10+"Define tres variable tipo entero"+"-"*10
puts " "
_var = 100
var_entero = 1000
dato1 = -200
puts "variable _var: #{_var}"
puts "variable var_entero: #{var_entero}"
puts "variable dato1: #{dato1}"
puts " "
#Define tres variables tipo flotante.
puts "-"*10+"Define tres variables tipo flotante"+"-"*10
puts " "
_var = 25.0
var_flotante = 3.1416
dato2 = 3.0/4
puts "variable _var: #{_var}"
puts "variable var_flotante: #{var_flotante}"
puts "variable dato2: #{dato2}"
puts " "
#Define tres variables tipo boolean.
puts "-"*10+"Define tres variables tipo boolean"+"-"*10
puts " "
var = true
var_boolean = false
dato3 = (1==1)
puts "variable _var: #{_var}"
puts "variable var_boolean: #{var_boolean}"
puts "variable dato3: #{dato3}"
puts " "
#Define una variable y asígnale un arreglo que tenga valores tipo string y hash.
puts "-"*10+"Define una variable y asígnale un arreglo que tenga valores tipo string y hash"+"-"*10
puts " "
var_arreglo = ["Hello","World",{"Peru" => "Lima", "Bolivia"=> "La Paz", "Ecuador" => "Quito"}]

puts "variable var_arreglo: #{var_arreglo}"
puts "variable var_arreglo[0]: #{var_arreglo[0]}"
puts "variable var_arreglo[1]: #{var_arreglo[1]}"
puts "variable var_arreglo[2]: #{var_arreglo[2]}"
puts " "
#Define una variable y asígnale un hash con tres claves (keys) de tipo symbol, dos valores tipo arreglo (array) y un valor tipo hash con 3 elementos del tipo de dato que decidas.
puts "-"*10+"Define una variable y asígnale un arreglo que tenga valores tipo string y hash"+"-"*10
puts " "
var_hash = {"Arreglo1:" =>  [1,2,3], "Arreglo2:"=> [4,5,6], "v_Hash:" => {"Peru" => "Lima", "Altura" => 2.87, "Codigo_Postal" => 15001}}

puts "var_hash: #{var_hash}"
puts "var_hash: #{var_hash["Arreglo1:"]}"
puts "var_hash: #{var_hash["Arreglo2:"]}"
puts "var_hash: #{var_hash["v_Hash:"]}"

