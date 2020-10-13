# import telebot
from datetime import datetime, timedelta
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

lista = list()
listaaux = list()


class Airport:
    def __init__(self):
        self.__disponible = True
        self.__precio = 0
        self.__destino = None
        self.__IATA = ""
        self.__aeropuerto = ""
        self.__pais = ""
        self.__numeroasientos = 50
        self.__reservar = False
        self.__aerolinea = ""
        self.__tiempo = ""

    def settiempo(self, vuelta):
        self.__tiempo = vuelta

    def gettiempo(self):
        return self.__tiempo

    def setAerolinea(self, aerolinea):
        self.__aerolinea = aerolinea

    def getAerolinea(self):
        return self.__aerolinea

    def getReservar(self):
        return self.__reservar

    def setReservar(self, reservar):
        self.__reservar = reservar

    def getAsientos(self):
        return self.__numeroasientos

    def setAsientos(self, numeros):
        self.__numeroasientos = numeros

    def isDisponible(self):
        if self.__disponible is True:
            return True
        else:
            return False

    def setDisponible(self, var1):
        self.__disponible = var1

    def getPrecio(self):
        return self.__precio

    def setprecio(self, var2):
        self.__precio = var2

    def getDestino(self):
        return self.__destino

    def setDestino(self, destino):
        self.__destino = destino

    def setIATA(self, destino):
        self.__IATA = destino

    def getIATA(self):
        return self.__IATA

    def setAeropuerto(self, aeropuerto):
        self.__aeropuerto = aeropuerto

    def getAeropuerto(self):
        return self.__aeropuerto

    def setPais(self, pais):
        self.__pais = pais

    def getPais(self):
        return self.__pais


# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)

with open('lista2.csv', 'r') as archivo:
    lineas = archivo.read().splitlines()
    for l in lineas:
        linea = l.split(',')
        ramdon = random.randrange(100)
        if ramdon < 20:
            obj = Airport()
            obj.setIATA(str(linea[0]))
            obj.setAerolinea(linea[1])
            obj.setAeropuerto(str(linea[2]))
            obj.setPais(str(linea[3]))

            ramdon2 = random.randint(200, 2000)
            obj.setDisponible(True)
            obj.setprecio(ramdon2)
            lista.append(obj)


# bot = telebot.TeleBot("1106516479:AAHG43mi53VKdqRw7I7iQ6vXxWbwqgSQFyg")
def generardesandorigen():
    for i in lista:
        ramdon1 = random.randrange(len(lista))
        ramdon9 = random.randrange(10)
        if len(listaaux) > 7:
            rd1 = random.randrange(len(listaaux))

        if ramdon9 > 2 and len(listaaux) > 7:

            i.setDestino(listaaux[rd1])
            listaaux.append(listaaux[rd1])
        else:
            i.setDestino(lista[ramdon1])
            listaaux.append(lista[ramdon1])


def start(update, context):
    update.message.reply_text(' Bienvenido a AirportUG ')
    update.message.reply_text("\n 1.- Informacion de vuelos disponibles. /list"
                              "\n 2.- Vuelos disponibles. /searchd"
                              "\n 3.- Vuelos disponibles. /searcho"
                              "\n 4.- Reserver un vuelo de ida. /buy_ticket "
                              "\n 5.- Reserver un vuelo de ida y vuelta. /buyrt_ticket ")


def help(update, context):
    update.message.reply_text("Mantenimiento")


# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)


def listar(update, context):
    for i in lista:
        if i.isDisponible():
            update.message.reply_text(enviarsms(i.getIATA(), i.getAeropuerto(), i.getPais(), i.getAerolinea()))


def enviarsms(iata, aeropuerto, pais, aerolinea):
    return "- El vuelo " + iata + " |  Aeropuerto: " + aeropuerto + " | En este pais: " + pais + " | Aerolinea: " + aerolinea + " esta disponible!"


def searchd(update, context):
    update.message.reply_text("Cargando...")
    if len(context.args) == 0:
        update.message.reply_text("Para buscar el destino siga estas indicaciones."
                                  "\n /searchd [IATA] [Nombre del aeropuerto] [Pais]")
        return
    num = 0
    print(len(context.args))
    if len(context.args) >= 2:

        try:
            update.message.reply_text("Vuelos con destino a: " + context.args[2])
            print(context.args[0])
            for i in lista:
                destino = i.getDestino()
                print(destino.getIATA())

                if destino.getIATA() == context.args[0] and i.isDisponible():
                    update.message.reply_text("Aerolinea: " + destino.getAerolinea())
                    update.message.reply_text(
                        "- El vuelo " + i.getIATA() + "| con origen  " + i.getPais() + "  | Aeropuerto:  " + i.getAeropuerto() + " | Con destino  " + destino.getPais() + "  | Aeropuerto:  " + destino.getAeropuerto() + " Aerolinea: " + i.getAerolinea())
                    num += 1
            if num == 0:
                update.message.reply_text("No se ah encontrado resultados")

            print(num, " -", len(listaaux))
        except:
            update.message.reply_text("ERRO! Completar con todos los argumentos establecidos")
            update.message.reply_text("Para buscar el destino siga estas indicaciones."
                                      "\n /searchd [IATA] [Nombre del aeropuerto] [Pais]")

    else:
        update.message.reply_text("Error ingresa los valores correctamente")


def searcho(update, context):
    update.message.reply_text("Cargando...")
    if len(context.args) == 0:
        update.message.reply_text("Para buscar el origen siga estas indicaciones."
                                  "\n /searchd [IATA] [Nombre del aeropuerto] [Pais]")
        return
    num = 0
    print(len(context.args))
    if len(context.args) >= 2:

        try:
            update.message.reply_text("Vuelos con origen a: " + context.args[2])
            for i in lista:
                destino = i.getDestino()
                print(destino.getIATA())

                if i.getIATA() == context.args[0] and i.isDisponible():
                    update.message.reply_text("Aerolinea: " + i.getAerolinea())
                    update.message.reply_text(
                        "- El vuelo " + i.getIATA() + "| con origen  " + i.getPais() + " | Aeropuerto:  " + i.getAeropuerto() + " | Con destino a: " + destino.getPais() + " | Aeropuerto:  " + destino.getAeropuerto() + "| Aerolinea: " + destino.getAerolinea())
                    num += 1
            if num == 0:
                update.message.reply_text("No se ah encontrado resultados")
            print(num, " -", len(listaaux))
        except:
            update.message.reply_text("ERRO! Completar con todos los argumentos establecidos")
            update.message.reply_text("Para buscar el origen siga estas indicaciones."
                                      "\n /searchd [IATA] [Nombre del aeropuerto] [Pais]")
    else:
        update.message.reply_text("Error ingresa los valores correctamente")


def buyticket(update, context):
    update.message.reply_text("Cargando...")
    if len(context.args) == 0:
        update.message.reply_text("Para buscar el destino siga estas indicaciones."
                                  "\n /buyticket [Origen IATA] [Destino IATA] [Asientos que va a reservar]")
        return
    n = 0
    if len(context.args) >= 2:
        try:
            for i in lista:
                if i.getIATA() == context.args[0] and i.getDestino().getIATA() == context.args[1]:
                    if i.isDisponible():
                        i.setReservar(True)
                        asientores = i.getAsientos() - int(context.args[1])
                        i.setAsientos(asientores)
                        i.settiempo(get_rnd_date(datetime.now(), "31/12/2020", "%d/%m/%Y"))
                        update.message.reply_text("\n Tipo de vuelo: Ida" +
                                                  "\n Fecha del vuelo " + i.gettiempo() +

                                                  "\n Gracias por su compra en la Aerolinea " + i.getAerolinea() +
                                                  "\n Asientos reservados: " + str(context.args[2]) +
                                                  "\n Asientos disponibles: " + str(i.getAsientos()) +
                                                  "\n Origen: " + i.getAeropuerto() +
                                                  "\n Pais de origen: " + i.getPais() +
                                                  "\n Destino: " + i.getDestino().getAeropuerto() +
                                                  "\n Pais de destino: " + i.getDestino().getPais() +
                                                  "\n Precio: $" + str(i.getPrecio()) +
                                                  "\n Aerolinea: " + str(i.getAerolinea()))
                        i.setDisponible(False)
                        n = 1
                        return
                    else:
                        update.message.reply_text("Este vuelo no esta disponible")

            if n == 0:
                update.message.reply_text("No se a encontrado el vuelo que desea reservar")

        except:
            update.message.reply_text("ERRO! Completar con todos los argumentos establecidos")
            update.message.reply_text("Para buscar el destino siga estas indicaciones."
                                      "\n /buyticket [IATA] [Asientos que va a reservar]")

    else:
        update.message.reply_text("Error ingresa los valores correctamente")


def get_rnd_date(start, end, fmt):
    s = datetime.strptime(start, fmt)
    e = datetime.strptime(end, fmt)

    return e + (s - e) * random.random()



def vuelta(update, context):
    update.message.reply_text("Cargando....")
    if len(context.args) == 0:
        update.message.reply_text("Para buscar el destino siga estas indicaciones."
                                  "\n /buyticket [Origen IATA] [Destino IATA] [Asientos que va a reservar]")
        return
    n = 0
    if len(context.args) >= 2:
        try:
            for i in lista:
                if i.getIATA() == context.args[0] and i.getDestino().getIATA() == context.args[1]:
                    if i.isDisponible():
                        i.setReservar(True)
                        asientores = i.getAsientos() - int(context.args[1])
                        i.getDestino().setDestino(i)
                        i.setAsientos(asientores)
                        i.settiempo(get_rnd_date(datetime.now(), "31/12/2020", "%d/%m/%Y"))
                        update.message.reply_text("\n Tipo de Vuelo: Ida - vuelta"+
                                                  "\n Fecha del vuelo " + i.gettiempo() +
                                                  "\n Fecha del vuelta " + str(get_rnd_date(datetime.now(), "31/12/2020", "%d/%m/%Y")) +
                                                  "\n Gracias por su compra en la Aerolinea " + i.getAerolinea() +
                                                  "\n Asientos reservados: " + str(context.args[2]) +
                                                  "\n Asientos disponibles: " + str(i.getAsientos()) +
                                                  "\n Origen: " + i.getAeropuerto() +
                                                  "\n Pais de origen: " + i.getPais() +
                                                  "\n Destino: " + i.getDestino().getAeropuerto() +
                                                  "\n Pais de destino: " + i.getDestino().getPais() +
                                                  "\n Precio: $" + str(i.getPrecio()) +
                                                  "\n Aerolinea: " + str(i.getAerolinea()))
                        i.setDisponible(False)
                        n = 1
                        return
                    else:
                        update.message.reply_text("Este vuelo no esta disponible")

            if n == 0:
                update.message.reply_text("No se a encontrado el vuelo que desea reservar")
        except:
            update.message.reply_text("ERRO! Completar con todos los argumentos establecidos")
            update.message.reply_text("Para buscar el destino siga estas indicaciones."
                                      "\n /buyticket [IATA] [Asientos que va a reservar]")

    else:
        update.message.reply_text("Error ingresa los valores correctamente")


def main():
    generardesandorigen()
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1106516479:AAHG43mi53VKdqRw7I7iQ6vXxWbwqgSQFyg", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("list", listar))
    dp.add_handler(CommandHandler("searchd", searchd))
    dp.add_handler(CommandHandler("searcho", searcho))
    dp.add_handler(CommandHandler("buyticket", buyticket))
    dp.add_handler(CommandHandler("buyrtticket", vuelta))
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
