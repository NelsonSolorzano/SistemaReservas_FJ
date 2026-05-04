from abc import ABC, abstractmethod
import datetime

# ---------------- LOG ----------------
def registrar_log(mensaje):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

# ---------------- EXCEPCIONES ----------------
class ErrorSistema(Exception):
    pass

# ---------------- CLIENTE ----------------
class Cliente:
    def __init__(self, nombre, documento):
        if not nombre or not documento:
            raise ValueError("Datos del cliente inválidos")
        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

# ---------------- SERVICIO ----------------
class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

# ---------------- SERVICIOS ----------------
class Sala(Servicio):
    def calcular_costo(self):
        return 100

class Equipo(Servicio):
    def calcular_costo(self):
        return 50

class Asesoria(Servicio):
    def calcular_costo(self):
        return 150

# ---------------- RESERVA ----------------
class Reserva:
    def __init__(self, cliente, servicio):
        if not isinstance(cliente, Cliente):
            raise TypeError("Cliente inválido")
        if not isinstance(servicio, Servicio):
            raise TypeError("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

# ---------------- PRUEBAS ----------------
clientes = []
reservas = []

try:
    c1 = Cliente("Nelson", "1080292740")
    clientes.append(c1)

    s1 = Sala("Sala VIP")

    r1 = Reserva(c1, s1)
    r1.confirmar()

    reservas.append(r1)

    print("Reserva realizada correctamente")

except Exception as e:
    registrar_log(str(e))
    print("Error:", e)

# -------- PRUEBA CON ERROR --------
try:
    c2 = Cliente("", "")  # error
except Exception as e:
    registrar_log(f"Error cliente: {e}")
    print("Error controlado:", e)
