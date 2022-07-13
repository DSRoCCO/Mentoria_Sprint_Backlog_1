#range method
def range(num)
  if num > 0 and num <= 50
    return "#{num} is between 0 and 50"
  elsif num > 50 and num <= 100
    return "#{num} is between 51 and 100"
  else
    return "#{num} is above 100"
  end

end


#driver Code
p range(10) == "10 is between 0 and 50"
p range(34) == "34 is between 0 and 50"
p range(79) == "79 is between 51 and 100"
p range(67) == "67 is between 51 and 100"
p range(54) == "54 is between 51 and 100"
p range(120) == "120 is above 100"
