def multiplication_tables(number)
  n = 5
  (1..number).each do |pos|
    (1..10).each do |value|
      print ((value*pos).to_s + " "*(n-(value*pos).to_s.length))
    end
    puts ""
  end

end

multiplication_tables(5)
puts ""
multiplication_tables(7)
