#get_item method
def get_item(*args)
  result = []
  result << args[0][1][0] << args[1][0][0]
end


#driver code
names = [["Lourdes", "Libis", "Lalo"], ["Moni", "Marcela"]]
fruits = [["fresa", "frambuesa"], ["lima", "limon"]]

p get_item(names, fruits) == ["Moni", "fresa"]
