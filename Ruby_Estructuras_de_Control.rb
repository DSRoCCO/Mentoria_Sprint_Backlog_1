require 'Prime'

#prime method
def prime_one?(number)
  prime = true
  (2..(number-1)).to_a.each do |value|
    if number % value == 0
      prime = false
      break
    end
  end
  return prime
end

def prime(rango)
  rango.each_with_index do |number,position|
    #puts "#{position} : #{number}"
      if prime_one?(number)
        rango[position] = "prime"
      end
  end
  return rango
end

def is_prime?(rango)
  rango.each_with_index do |number,position|
    #puts "#{position} : #{number}"
      if Prime.prime?(number)
        rango[position] = "prime"
      end
  end
  return rango
end

#driver code

puts prime([2, 3, 4, 5, 6, 7, 8, 9, 10]) == ["prime", "prime", 4, "prime", 6, "prime", 8, 9, 10]
puts prime([23, 54, 7, 123, 56, 76, 83, 101]) == ["prime", 54, "prime", 123, 56, 76, "prime", "prime"]

#driver code
puts is_prime?([2, 3, 4, 5, 6, 7, 8, 9, 10]) == ["prime", "prime", 4, "prime", 6, "prime", 8, 9, 10]
puts is_prime?([23, 54, 7, 123, 56, 76, 83, 101]) == ["prime", 54, "prime", 123, 56, 76, "prime", "prime"]
