#En la expresión1 no está permitido agregar otra operación aritmética,
#ni modificar el tipo de operación (p.e. una división por una resta, etc.)

expresion1 = 5 / 4.to_f ** 2 + 1 * 2
expresion2 = (expresion1 / 23.125).to_s.reverse.to_i
expresion3 = 1 ** 1000
expresion4 = expresion3 == expresion2
expresion4 == true
#=> true


#En la expresión1 no está permitido agregar otra operación aritmética,
#ni modificar el tipo de operación (p.e. una resta por una suma, etc.)

expresion1 = (4 * 2 + (3 / 7.0) ** 3).round(2)
expresion2 = expresion1 == 8.08
#=> true
expresion3 = (expresion1 ** 3).floor
expresion4 = 527
expresion5 = expresion3 == expresion4
#=> true
expresion6 = ((expresion4 / expresion4) % 2).to_f.to_s.reverse.to_i
expresion7 = expresion6 == 0
#=> true
