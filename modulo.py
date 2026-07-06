def validar_texto(texto):
    return len(texto.strip()) >0

def validar_codigo(codigo, productos):
    if not codigo or codigo.strip() == "":
        return False
    if codigo in productos:
        return False
    return True

def validar_nombre(nombre):
    if not nombre or nombre.strip() =="":
        return False
    return True

def validar_categoria(categoria):
    if not categoria or categoria.strip() =="":
        return False
    return True

def validar_precio(precio):
    try: 
        precio = int(precio)
        return precio >0
    except ValueError:
        return False
    
def validar_disponible(opcion):
    if opcion is None:
        return False
    opcion = opcion.lower().strip()
    if opcion == "s":
        return True
    if opcion == "n":
        return False
    else:
        return False
    
def validar_stock(stock):
    try:
        stock =int(stock)
        return stock >=0
    except ValueError:
        return False
    
def validar_vendidos(vendidos):
    try:
        vendidos = int(vendidos)
        return vendidos >=0
    except ValueError:
        return False
    
def buscar_codigo(codigo, productos):
    if not codigo:
        return False
    return codigo in productos

def stock_categoria(categoria, productos, inventario):
    if not categoria or categoria.strip() == "":
        print("Error, la categoria no puede estar vacia")
        return False
    categoria_buscar = categoria.strip().lower()
    stock_total = 0
    encontrado = False

    for codigo, datos in productos.item():
        if datos [1].strip().lower() == categoria_buscar:
            encontrado = True
            if codigo in inventario:
                stock_total += inventario[codigo][0]

    if encontrado:
        print(f"Stock total para categoria {categoria} es {stock_total}")
    else:
        print(f"No se encontraron productos en la categoria {categoria}")


def buscar_por_precio(precio_min, precio_max, productos, inventario):
    try:
        precio_min =int(precio_min)
        precio_max = int(precio_max)
        if precio_min > precio_max:
            print("Error, el precio minimo no puede ser mayor al precio maximo")
            return

    except ValueError:
        print("Error, los numeros deben ser enteros positivos")
        return
    
     filtrados = []
    
    for codigo, datos in productos.item():
        if codigo in inventario and inventario[codigo][0] > 0:
            precio = datos[2]
            if precio_min <= precio <= precio_max:
                filtrados.append((datos[0], codigo))
    if not filtrados:
        print("No se encontraron productos con stock disponible en ese rango de precio.")
        return   
    filtrados.sort(key=lambda x: x[0].lower())   
    print("Productos encontrados (orden alfabético):")
    for nombre, codigo in filtrados:
        print(f"{nombre}--{codigo}")

def actualizar_precio(codigo, nuevo_precio, productos):
    if not buscar_codigo(codigo, productos):
        return False
    try:
        precio_int = int(nuevo_precio)
        if precio_int <= 0:
            return False
        productos[codigo][2] = precio_int
        return True
    except (ValueError, TypeError):
        return False
    
def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    if codigo in productos:
        return False
    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]  
    return True

def eliminar_productos(codigo, productos, inventario):
    if codigo not in productos:
        return False
    del productos[codigo]
    if codigo in inventario:
        del inventario[codigo]
    return True

def mostrar_productos(productos, inventario):
    if not productos:
        print("Error, no hay productos registrados")
        return
    for codigo, datos in productos.item():
        print(f"""
              codigo: {codigo}
              nombre: {datos[0]}
              categoria: {datos[1]}
              precio: ${datos[2]}
              disponible: {datos[3]}""")
        
        if codigo in inventario:
            print(f"stock: {inventario[codigo[0]]}")
            print(f"vendidos: {inventario[codigo[1]]}")
        else:
            print("stock = 0")
            print("vendidos = 0")
        print("-" * 30)




    


