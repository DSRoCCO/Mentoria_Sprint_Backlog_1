def world_cup(word)

  if word == "Clave: Rutio"
    word.gsub!("t","s") if word.include?("t")
    word.gsub!("o", 'a') if word.include?("o")
  end

  if word == "Clave: Rutia"
    word = "Wrong Password"
  end

  return word
end


p world_cup("Clave: Rutio") == "Clave: Rusia"
p world_cup("Clave: Rutia") == "Wrong Password"
