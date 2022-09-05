#join_hash method
def join_hash(*hashes)
  frutas = Hash.new
  hashes.each do |value|
    frutas.update(value)
  end
frutas

end


#merge_hash method
def merge_hash(*hashes)
  frutas = Hash.new
  hashes.each do |value|
    frutas[value.keys[0]]=value.values[0]
  end
frutas
end



# Driver code

fruit = {name: "pineapple"}
weight = {weight: "1 kg"}
taste = {taste: "good"}


p join_hash(fruit, weight, taste) == {:name=>"pineapple", :weight=>"1 kg", :taste=>"good"}

p merge_hash(fruit, weight, taste) == {:name=>"pineapple", :weight=>"1 kg", :taste=>"good"}

