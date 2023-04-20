metros_cubiertos = input("Ingrese los metros cubiertos: ")
dormitorios = input("Ingrese la cantidad de dormitorios: ")
antiguedad = input("Ingrese la antigüedad (en años): ")
banios = input("Ingrese la cantidad de baños: ")
ambientes = input("Ingrese la cantidad de ambientes: ")
barrio = input("Ingrese el nombre del barrio: ")
moneda = input("Ingrese la moneda (ej: USD, ARS, EUR, etc.): ")
precio = input("Ingrese el precio: ")

    
   propiedades_filtradas = Propiedad.objects.filter(
    metros_cubiertos__gte=metros_cubiertos,
    dormitorios__gte=dormitorios,
    antiguedad__lte=antiguedad,
    banios__gte=banios,
    ambientes__gte=ambientes,
    barrio=barrio,
    moneda=moneda,
    precio__lte=precio
)