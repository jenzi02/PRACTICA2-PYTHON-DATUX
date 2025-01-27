class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de horarios asignados al conductor (solo horas)

    def agregar_horario(self, hora):
        if hora in self.horarios:
            return False  # Horario ya asignado
        self.horarios.append(hora)
        return True


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []  # Lista de horarios asignados al bus
        self.conductores_asignados = []  # Lista de conductores asignados al bus

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, hora):
        if hora in self.horarios:
            return False  # Horario ya asignado
        self.horarios.append(hora)
        return True

    def asignar_conductor(self, conductor, hora):
        if hora not in self.horarios:
            return False, "El horario no está registrado en el bus."

        for c in self.conductores_asignados:
            if hora in c.horarios:
                return False, f"El horario {hora} ya está asignado a otro conductor."

        if conductor.agregar_horario(hora):
            self.conductores_asignados.append(conductor)
            return True, "Conductor asignado correctamente."
        return False, "No se pudo asignar el horario al conductor."


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa):
        bus = Bus(placa)
        self.buses.append(bus)
        return bus

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        return conductor

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                bus = self.agregar_bus(placa)
                print(f"Bus con placa {bus.placa} agregado.")

            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta: ")
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    bus.agregar_ruta(ruta)
                    print(f"Ruta {ruta} agregada al bus con placa {placa}.")
                else:
                    print("Bus no encontrado.")

            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                hora = input("Ingrese el horario (hh:mm): ")
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    if bus.registrar_horario(hora):
                        print(f"Horario {hora} registrado en el bus con placa {placa}.")
                    else:
                        print("El horario ya está registrado en este bus.")
                else:
                    print("Bus no encontrado.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                conductor = self.agregar_conductor(nombre)
                print(f"Conductor {conductor.nombre} agregado.")

            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                hora = input("Ingrese el horario (hh:mm): ")
                conductor = next((c for c in self.conductores if c.nombre == nombre), None)
                if conductor:
                    if conductor.agregar_horario(hora):
                        print(f"Horario {hora} agregado al conductor {nombre}.")
                    else:
                        print("El horario ya está asignado a este conductor.")
                else:
                    print("Conductor no encontrado.")

            elif opcion == "6":
                placa = input("Ingrese la placa del bus: ")
                nombre = input("Ingrese el nombre del conductor: ")
                hora = input("Ingrese el horario (hh:mm): ")

                bus = next((b for b in self.buses if b.placa == placa), None)
                conductor = next((c for c in self.conductores if c.nombre == nombre), None)

                if bus and conductor:
                    exito, mensaje = bus.asignar_conductor(conductor, hora)
                    print(mensaje)
                else:
                    print("Bus o conductor no encontrado.")

            elif opcion == "7":
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida.")


if __name__ == "__main__":
    admin = Admin()
    admin.menu()