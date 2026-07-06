import modulo
import os

def leer_opcion():
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if 1 <= opcion <= 7:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return None
    except ValueError:
        print("Debe seleccionar una opción válida")
        return None

def main():
    
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por categoría")
        print("2. Buscar productos por rango de precio")
        print("3. Actualizar precio")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Mostrar productos")
        print("7. Salir")
        print("====================================")
        
        opcion = leer_opcion()
        if opcion is None:
            continue

    
        if opcion == 1:
            categoria = input("Ingrese la categoría a buscar: ")
            modulo.stock_categoria(categoria, productos, inventario)

        
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min < 0 or p_max < 0 or p_min > p_max:
                    print("Valores de rango inválidos.")
                    continue
                modulo.buscar_precio(p_min, p_max, productos, inventario)
            except ValueError:
                print("Error: Los precios deben ser valores numéricos enteros.")

        
        elif opcion == 3:
            procesando = True
            while procesando:
                codigo = input("\nIngrese el código del producto a actualizar: ")
                if modulo.buscar_codigo(codigo, productos):
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        if modulo.validar_precio(nuevo_precio):
                            modulo.actualizar_precio(codigo, nuevo_precio, productos)
                            print("Precio actualizado con éxito.")
                        else:
                            print("Precio inválido. Debe ser un entero mayor que cero.")
                    except ValueError:
                        print("Error: El precio debe ser un número entero.")
                else:
                    print("Código inexistente")

                # Ciclo de continuidad
                rpta = input("¿Desea actualizar otro precio? (s/n): ").strip().lower()
                if rpta != 's':
                    procesando = False

        
        elif opcion == 4:
            print("\n--- Registro de Nuevo Producto ---")
            
            codigo = input("Código: ")
            if not modulo.validar_codigo(codigo, productos):
                print("Código inválido (Vacío, contiene espacios o ya está registrado).")
                continue

            nombre = input("Nombre: ")
            if not modulo.validar_nombre(nombre):
                print("Nombre inválido.")
                continue

            categoria = input("Categoría: ")
            if not modulo.validar_categoria(categoria):
                print("Categoría inválida.")
                continue

            precio = input("Precio: ")
            if not modulo.validar_precio(precio):
                print("Precio inválido (Debe ser un entero mayor que cero).")
                continue

            disponible = input("¿Disponible? (s/n): ")
            if not modulo.validar_disponible(disponible):
                print("Opción inválida (Debe ingresar 's' o 'n').")
                continue

            stock = input("Stock inicial: ")
            if not modulo.validar_stock(stock):
                print("Stock inválido (Debe ser entero mayor o igual a cero).")
                continue

            vendidos = input("Cantidad vendidos inicial: ")
            if not modulo.validar_vendidos(vendidos):
                print("Cantidad de vendidos inválida (Debe ser entero mayor o igual a cero).")
                continue

            # Si todas las validaciones pasaron, procedemos a insertar mediante la transacción
            exito = modulo.agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario)
            if exito:
                print("¡Producto agregado exitosamente!")
            else:
                print("Error: No se pudo agregar el producto.")

        
        elif opcion == 5:
            codigo = input("Ingrese el código del producto a eliminar: ")
            if modulo.eliminar_producto(codigo, productos, inventario):
                print("Producto eliminado correctamente.")
            else:
                print("Código inexistente. No se pudo eliminar.")

        
        elif opcion == 6:
            modulo.mostrar_productos(productos, inventario)

        
        elif opcion == 7:
            print("Saliendo del sistema... ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
        