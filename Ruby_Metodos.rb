#=> Hola Carlos te estamos esperando! Soy Rolando.
#=> Hola Manuel te estamos esperando! Soy Rolando.
#=> Hola Gaby te estamos esperando! Soy Rolando.
#=> Hola Samy te estamos esperando! Soy Rolando.
#=> Hola Yadira te estamos esperando! Soy Rolando.
#=> Hola Libis te estamos esperando! Soy Rolando.
#=> Hola Yoli te estamos esperando! Soy Rolando.
#=> Hola Faby te estamos esperando! Soy Rolando.
#=> Hola Moni te estamos esperando! Soy Rolando.
#=> Hola Pamela te estamos esperando! Soy Rolando.

lista = ["Carlos","Manuel","Gaby","Samy","Yadira","Libis","Yoli","Faby","Moni","Pamela"]

def mensaje(parameter)
  for name in parameter
    puts "Hola #{name} te estamos esperando! Soy Rolando."
  end

end

mensaje(lista)
