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
    

    


