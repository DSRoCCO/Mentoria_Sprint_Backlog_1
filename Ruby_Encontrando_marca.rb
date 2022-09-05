#brand groups
BRAND_GROUPS = {
  "celular" => ['iphone','lg', 'samsung', 'motorola'],
  "computadora" => ['MacBook', 'HP', 'Toshiba', 'Dell'],
  "cerveza" => ['Stella', 'Bohemia', 'Heineken', 'Corona'],
  "refresco" => ['coca-cola', 'Yoli', 'Sprite', 'Fanta']
  }

#brand_group method
def brand_group(brand)
  result = "Marca no encontrada"
  BRAND_GROUPS.values.each_with_index do |value, index|
    result = BRAND_GROUPS.keys[index] if value.include?(brand)
  end
  result
end

#Driver code

p brand_group('Yoli') == "refresco"
p brand_group('Heineken') == "cerveza"
p brand_group('HP') == "computadora"
p brand_group('Tecate') == "Marca no encontrada"
