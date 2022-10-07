def bye(numbers)
  numbers.map{ |x| (x < 10) ? "Smaller": x }
end


#Driver code

p bye([2, 4, 6, 10, 20, 40, 76]) == ["Smaller", "Smaller", "Smaller", 10, 20, 40, 76]
