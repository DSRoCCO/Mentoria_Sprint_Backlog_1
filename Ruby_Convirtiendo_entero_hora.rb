#require Time

def conversion_of_time(*args)
  result = []
  args.each do |arg|
    result <<[arg, Time.at(arg).min, Time.at(arg).sec, [Time.at(arg).min.to_s,":",Time.at(arg).sec.to_s].join]
  end
  result
end



#Driver code

p conversion_of_time(126, 230, 31) == [[126, 2, 6, "2:6"], [230, 3, 50, "3:50"], [31, 0, 31, "0:31"]]
p conversion_of_time(45) == [[45, 0, 45, "0:45"]]
