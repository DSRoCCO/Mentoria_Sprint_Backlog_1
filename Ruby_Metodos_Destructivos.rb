first_name = "Rogelio"
last_name = "manzano"
mensaje = "Nombre Correcto"

if first_name.upcase! == "ROGELIO" && last_name.capitalize! == "Manzano"
  if mensaje.downcase! == "nombre correcto"
    test1 = first_name == "ROGELIO"
    test2 = last_name == "Manzano"
  end
end

#driver code

p test1 == true
p test2 == true
