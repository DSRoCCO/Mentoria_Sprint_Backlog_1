#shipping method
def shipping(address)
  result = "We only ship orders to Mexico"
  for word in address.split(" ")
    if word.downcase =="mexico" or word.downcase =="mèxico"
      result = "Order received"
    end
  end
  return result


end

#driver code

p shipping('Insurgentes Sur 8932, Alvaro Obregon, Mexico') == "Order received"
p shipping('Insurgentes Sur 8932, Alvaro Obregon, MÈxIcO') == "Order received"
p shipping('Geary Blvd 3320, San Francisco, Estados Unidos') == "We only ship orders to Mexico"
