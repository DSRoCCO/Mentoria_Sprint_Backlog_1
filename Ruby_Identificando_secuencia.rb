#find_symbols method
def find_symbols(text)
  #/^(\W[a-z]\W)/.match?(text) Solucion 1
  /^([\W\D]\p{Ll}[\W\D]).{4}([\W\D]\p{Ll}[\W\D])$/.match?(text) #Solucion 2
end

#driver code
p find_symbols("-m+=10=+s+") == true
p find_symbols("h++l+") == false
p find_symbols("lk-+jh") == false
p find_symbols("-+hello") == false
p find_symbols("-d+0=sa-z-") == true
p find_symbols("--+0=sa-z-") == false
p find_symbols("-++0=sa-z-") == false
p find_symbols("-8+0=sa-z-") == false
