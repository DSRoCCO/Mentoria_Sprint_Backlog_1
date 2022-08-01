
def fizzbuzz(min, max)
  array = (min..max).to_a
  array.each do |value|
    if value % 5 == 0 && value % 3 == 0
      array[array.index(value)]="FizzBuzz"
    elsif value % 3 == 0
      array[array.index(value)]="Fizz"
    elsif value % 5 == 0
      array[array.index(value)]="Buzz"
    end
  end
  array
end

#Driver code

p fizzbuzz(3, 5) == ["Fizz", 4, "Buzz"]
p fizzbuzz(10, 15) == ["Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
