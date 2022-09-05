#array_to_hash method
def array_to_hash(lista)
  lista.to_h
end

#Driver code

p array_to_hash([["animal", "cat"],
  ["name", "Carlos"],
  ["things", "pencil"]]) == {
                             "animal"=>"cat",
                             "name"=>"Carlos",
                             "things"=>"pencil"
                            }
