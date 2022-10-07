def shopping(list)
  list.any? ? list.join(", ") : "Not valid"
end

#Driver code

p shopping(["eggs", "milk", "bread", "orange juice"]) == "eggs, milk, bread, orange juice"
p shopping([]) == "Not valid"
