#Ejercicio - Refactoring unless

def swim(time)
  "#{time} seconds... New Record for 50 meters" unless time >= 10
end

# Driver code

p swim(5) == "5 seconds... New Record for 50 meters"
p swim(8) == "8 seconds... New Record for 50 meters"
