#family_members method
def family_members(family)
  family[:sisters].union(family[:brothers])
end


#Driver code

family = {  uncles: ["jorge", "samuel", "steve"],
  sisters: ["angelica", "mago", "julia"],
  brothers: ["polo","rob","david"],
  aunts: ["maria","minerva","susana"]
}

p family_members(family) == ["angelica", "mago", "julia", "polo", "rob", "david"]
