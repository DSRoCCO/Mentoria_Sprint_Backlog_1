def decade(year)
  dec = year % 100
  if dec < 10
    return "Hundreds"
  elsif dec < 20 && dec >= 10
    return "Tens"
  elsif dec < 30 && dec >= 20
    return "Twenties"
  elsif dec < 40 && dec >= 30
    return "Thirties"
  elsif dec < 50 && dec >= 40
    return "Forties"
  elsif dec < 60 && dec >= 50
    return "Fifties"
  elsif dec < 70 && dec >= 60
    return "Sixties"
  elsif dec < 80 && dec >= 70
    return "Seventies"
  elsif dec < 90 && dec >= 80
    return "Eighties"
  else
    return "Nineties"
  end
end



#Driver code

p decade(1905) == "Hundreds"
p decade(1914) == "Tens"
p decade(1920) == "Twenties"
p decade(1935) == "Thirties"
p decade(1943) == "Forties"
p decade(1952) == "Fifties"
p decade(1960) == "Sixties"
p decade(1975) == "Seventies"
p decade(1982) == "Eighties"
p decade(1999) == "Nineties"
p decade(1925) == "Twenties"
