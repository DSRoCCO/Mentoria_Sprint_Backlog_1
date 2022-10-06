# Ejercicio - Refactoring language

def language(speak)
  lenguajes = ["Javascript", "CSS", "Python", "R", "C++", "Unity", "Ruby", "Rails", "Java"]
  (lenguajes.include?(speak) or lenguajes.include?(speak.capitalize!)) ? "I like #{speak}": "I don't like to code"
end
# Driver code

p language("Javascript") == "I like Javascript"
p language("Unity") == "I like Unity"
p language("Swift") == "I don't like to code"
p language("Kotlin") == "I don't like to code"
p language("Android") == "I don't like to code"
p language("ruby") == "I like Ruby"
p language("rails") == "I like Rails"
