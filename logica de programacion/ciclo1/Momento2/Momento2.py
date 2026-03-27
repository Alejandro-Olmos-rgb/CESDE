def ejecutar_sistema_vip():

    asistentes = []
    CUPO_MAXIMO = 20
    
    while True:
        print("\n" + "="*40)
        print("      SISTEMA DE GESTIÓN VIP 1.0")
        print("="*40)
        print(f" ASISTENTES ACTUALES: {len(asistentes)} | CUPOS DISPONIBLES: {CUPO_MAXIMO - len(asistentes)}")
        print("-" * 40)
        print("1. Registrar Asistente")
        print("2. Ver Lista de Invitados")
        print("3. Corregir Nombre (Editar)")
        print("4. Retirar Persona (Salida)")
        print("5. Ver Estadísticas Detalladas")
        print("6. Salir")
        print("-" * 40)
        
        opcion = input("Seleccione una opción (1-6): ")

       
        if opcion == "1":
            if len(asistentes) >= CUPO_MAXIMO:
                print("\n ERROR: Aforo completo. No pueden ingresar más personas.")
            else:
                nuevo_nombre = input("Ingrese el nombre completo del asistente: ").strip()
                
                
                if nuevo_nombre.lower() in [a.lower() for a in asistentes]:
                    print(f"\n ELERTA: '{nuevo_nombre}' ya está registrado en la lista.")
                elif nuevo_nombre == "":
                    print("\n ERROR: El nombre no puede estar vacío.")
                else:
                    asistentes.append(nuevo_nombre)
                    print(f"\n ¡Registro exitoso! {nuevo_nombre} ha ingresado.")

        elif opcion == "2":
            if not asistentes:
                print("\n La lista está vacía actualmente.")
            else:
                print("\n--- LISTA ACTUAL DE ASISTENTES ---")
                for i, nombre in enumerate(asistentes, start=1):
                    print(f"{i}. {nombre}")

        
        elif opcion == "3":
            if not asistentes:
                print("\n No hay nadie en la lista para editar.")
                continue
                
            nombre_editar = input("Ingrese el nombre exacto que desea corregir: ").strip()
            
            
            if nombre_editar in asistentes:
                indice = asistentes.index(nombre_editar)
                nuevo_nombre = input("Ingrese el nombre corregido: ").strip()
                asistentes[indice] = nuevo_nombre
                print("\n Nombre actualizado correctamente.")
            else:
                print("\n ERROR: El nombre no se encuentra en la lista.")

        elif opcion == "4":
            nombre_retirar = input("Ingrese el nombre de la persona que se retira: ").strip()
            
            
            if nombre_retirar in asistentes:
                asistentes.remove(nombre_retirar)
                print(f"\n {nombre_retirar} ha sido removido de la lista.")
            else:
                print("\n ERROR: Esa persona no está registrada como asistente.")

        elif opcion == "5":
          
            ingresados = len(asistentes)
            disponibles = CUPO_MAXIMO - ingresados
            porcentaje = (ingresados / CUPO_MAXIMO) * 100
            
            print("\n--- ESTADÍSTICAS DEL EVENTO ---")
            print(f"Total Ingresados: {ingresados}")
            print(f"Cupos Restantes: {disponibles}")
            print(f"Capacidad ocupada: {porcentaje}%")

        elif opcion == "6":
            print("\nCerrando sistema de portería... ¡Feliz noche!")
            break

        else:
            print("\n Opción inválida. Por favor, marque un número del 1 al 6.")

if __name__ == "__main__":
    ejecutar_sistema_vip()