def take_a_decision(option_a,option_b)
  if option_b > option_a
    message = "#{option_b} es mayor que #{option_a}"
  elsif option_a > option_b
    message = "#{option_b} es menor que #{option_a}"
  else
    message = "#{option_b} es igual que #{option_a}"
  end
  message  # retorno implicito, para retorno explicito le agregamos return
end

puts take_a_decision(2.3, 4) == "4 es mayor que 2.3"
puts take_a_decision(7, 4) == "4 es menor que 7"

