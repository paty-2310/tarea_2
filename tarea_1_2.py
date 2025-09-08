import os
os.system("cls")
win = False

print("\n\nUna fuerte luz invade tu habitacion en la mitad de la noche, una fuerza mueve tu cuerpo a traves del edificio en el que vives, tu cuerpo se vuelve intangible y es transportado a traves de un rayo de luz a una gigantesca nave espacial. Al llegar al final del rayo de luz una luz blanca te ciega y te encuentras atrapado en una camilla de metal, un grupo de aliens estan hablando en un idioma que no entiendes y dejan la habitacion un tiempo despues.")
option1 = input("\n\tQue haras? ESCAPAR o ESPERAR: ").lower()

if option1 == "escapar" :
    print("\n\nConsigues aflojar las cintas que te atrapan y liberarte de la camilla, la puerta por la que los aliens salieron esta abierta y tiene dos pasillos.")
    option1_1 = input("\n\tPor cual pasillo iras? IZQUIERDO o DERECHO: ").lower()

    if option1_1 == "izquierdo" :
        print("\n\nEntras a una habitacion extensas, dos puertas grandes se alzan ante ti, una lleva a los motores de la nave, la otra a armeria")
        option1_1_1 = input("\n\tPor cual puerta iras? MOTORES o ARMERIA: ").lower()

        if option1_1_1 == "motores" :
            print("\n\nEncuentras dos herramientas extrañas en el suelo, una parece ser un tubo de algun tipo de metal con varias puntas diferentes y un circulo hecho de algo viscoso y que parece corrosivo.")
            option1_1_1_1 = input("\n\tCual herramienta elegiras? TUBO o CIRCULO: ").lower()

            if option1_1_1_1 == "tubo" :
                print("\n\nTomaste el tubo y tienes dos opciones, tratar de destruir los motores o intentar luchar con los alienigenas")
                option1_1_1_1_1 = input("\n\tQue haras? DESTRUIR o LUCHAR: ").lower()

                if option1_1_1_1_1 == "destruir" :
                    print("\n\nInsertas el tubo en los motores de la nave y ves como se detienen, escuchas explosiones en la distancia, parece que dañaste fatalmente la nave.")
                    option1_1_1_1_1_1 = input("\n\tQue haras? HUIR o QUEDARTE: ").lower()

                    if option1_1_1_1_1_1 == "huir" :
                        print("\n\nSales al pasillo, encontrando un objeto que te teletransporta a la superficie, ves la nave caer a la distancia.")
                        win = True
                    elif option1_1_1_1_1_1 == "quedarte" :
                        print("\n\nLa nave explota desde adentro, los motores fallan y se estrella en la tierra, tu y todos los aliens mueren en el impacto.")
                        win = False
                    else :
                        print("\n\nLa nave se estabiliza despues de un tiempo y un grupo de guardias aliens te encuentran. Eres terminado en el instante.")
                        win = False

                elif option1_1_1_1_1 == "luchar" :
                    print("\n\nSales corriendo al pasillo fuera de la zona de motores, un grupo de cientificos aliens desarmados se ven al final del pasillo, un grupo de guardias del otro lado.")
                    option1_1_1_1_1_2 = input("\n\tQue aliens atacaras? CIENTIFICOS o GUARDIAS").lower()

                    if option1_1_1_1_1_2 == "cientificos" :
                        print("\n\nAtacas a los aliens desarmados, tomando el dispositivo de escape que intentaban utilizar, eres transportado a la tierra en un pais lejano al tuyo.")
                        win = True
                    elif option1_1_1_1_1_2 == "guardias" :
                        print("\n\nIntentas luchar contra los guardias, pero no eres rival para ellos, te detienen justo antes de que la nave se estrelle.")
                        win = False
                    else :
                        print("\n\nTardas demasiado en decidir, una torreta de la nave te derriba antes de que puedas hacer algo.")
                        win = False
                else :
                    print("\n\nNo tomas ninguna accion, los guardias aliens te encuentran y te terminan.")
                    win = False

            elif option1_1_1_1 == "circulo" :
                print("\n\nTomaste el circulo, el mango evita que tu mano se derrita por el material viscoso. Puedes intentar derretir los motores o la pared de la nave.")
                option1_1_1_1_2 = input("\n\tQue derretiras? MOTORES o PARED: ").lower()

                if option1_1_1_1_2 == "motores" :
                    print("\n\nIntentas derretir los motores, los cuales se detienen por un momento antes de resumir su actividad, parece que el acido no es lo suficientemente efectivo contra lo motores, pero quizas puedas derretir la pared y huir. La nave ha ascendido a la alta atmosfera")
                    option1_1_1_1_2_2 = input("\n\tQue derretiras? MOTORES o PARED: ").lower()

                    if option1_1_1_1_2_2 == "motores" :
                        print("\n\nIntentas derretir los motores de nuevo, pero no funciona. La nave se mantiene en funcionamiento y escuchas los pasos de los guardias acercandose a ti.")
                        win = False
                    elif option1_1_1_1_2_2 == "pared" :
                        print("\n\nDerrites la pared de la nave, siendo lanzado a la alta atmosfera, muriendo en el instante.")
                        win = False
                    else :
                        print("\n\nEl acido de tu herramienta lentamente empieza a corroer tu mano, muriendo en el proceso.")
                        win = False

                elif option1_1_1_1_2 == "pared" :
                    print("\n\nDerrites la pared de la nave. No pareces estar tan lejos de la superficie, y mientras la pared se derrite tienes tiempo para pensar en como escapar.")
                    option1_1_1_1_1_2 = input("\n\tQue haras? ESPERAR o BUSCAR: ").lower()

                    if option1_1_1_1_1_2 == "esperar" :
                        print("\n\nDecides esperar a que la pared se derrita por completo, saltando desde la nave. Mueres en el impacto contra la tierra.")
                        win = False
                    elif option1_1_1_1_1_2 == "buscar" :
                        print("\n\nDecides buscar una algo que te ayude a sobrevivir la caida, encuentras un dispositivo que crea un campo de energia, permitiendote caer desde la nave hasta la tierra sin sufrir daño.")
                        win = True
                    else :
                        print("\n\nTardas demasiado en decidir, el acido de tu herramienta lentamente empieza a corroer tu mano, muriendo en el proceso.")
                        win = False

                else :
                    print("\n\nEl acido de tu herramienta lentamente empieza a corroer tu mano, muriendo en el proceso.")
                    win = False
            else :
                print("\n\n No tomas ninguna herramienta, los guardias aliens te encuentran y te terminan.") 
                win = False
              
               #Falta aqui 
        
        elif option1_1_1 == "armeria" :
            print("entras a la armeria y te encuentras con armas y objetos extraños que nunca has visto antes, una de estas te podria ayudar a escapar o podria matarte, ahora debes decidir que haras.\n\n ") 
            option1_1_3 = input("que haras?, ESPERAR O ARRIESGARTE: ").upper()
            if option1_1_3 == "ARRIESGARTE" or option1_1_3 == "ARRIESGARME" :
                print("decides arriesgarte y te pones a analizar toda sala,tratando de encontrar algun objeto  o arma que puedas utilizar para salir de ahi,en esto te encuentras dos tipos de armas extrañas, una es un baston hecho de un metal oscuro y pulido que absorbe y tiene una esfera traslucida en la punta,el otro es un rifle de tamaño mediano, con un cañon segmentado que brilla.\n\n") 
                option1_1_3_1 = input("\nque elegiras?,EL BASTON O RIFLE: ").upper() 
                if option1_1_3_1 == "EL BASTON" or option1_1_3_1 == "BASTON" :
                    print("coges el baston y te diriges al pasillo que esta lleno de guardias,te dispones a usarlo contra ellos asi que los apuntas, y tratas de regular el extraño baston el cual tiene escrito en un idioma desconocido para ti,logras regularlo y disparas,por suerte este funciona y envia odas electromagneticas hacia los alieniges haciendo que estos empiencen a agonizar,y se desintegren de adentro hacia fuera,ahora corres por el pasilo y llegas a la sala de control, puedes continuar o entrar\n\n")
                    option1_1_3_1_1 = input("que haras?, CONTINUAR O ENTRAR: ").upper() 
                    if option1_1_3_1_1 == "ENTRAR" : 
                        print("\n\nentras a la sala que esta vacia ya que todos en la nave estan en alerta,te acercas al panel y lo empiezas a manipular tratanto de entender el idioma,terminas presionando un boton y de la nada escuchas una voz humana, te comunicas con esta voz y era el capitan de una nave cercana,logras hacer que te busquen, eres rescatado antes de que la nave se destruya\n\n")
                        win = True
                    elif option1_1_3_1_1 == "CONTINUAR" :
                        print("decides continuar y te topas con escuadron de guardias,que a pesar el arma tan potente que tienes logran retenerte y deciden acabar contigo\n\n") 
                        win = False 
                    else : 
                        ("\n\ntardas mucho en tomar una desicion y las guardias terminan contigo") 
                elif option1_1_3_1 == "RIFLE" : 
                    print("\n\ndecides agarrar el rifle,te dirigirte al pasillo el cual esta lleno de guardias y los apuntas con el rifle pero este al ser tan pontente te muestra un texto rojo en un idioma extraño,el cual parece una advertencia\n\n") 
                    option1_1_3_1_2 = input("que haras?, DISPARAR O HUIR: ").upper() 
                    if option1_1_3_1_2 == "DISPARAR" : 
                        print("\n\ndecides dispara y debido a la potencia del rifle y el no saber manejarlo hay una sobrecarga,y esto provoca una explosion que destruye parte de la nave, tu y los guardias terminan muriendo")
                        win = False
                    elif option1_1_3_1_2 == "HUIR" : 
                        print("\n\nhuyes y dejas caer el arma ya antes recargada al suelo,lo que ocaciona que empienze a lanzar rayos descontroladamente, afortunadamente logras refugiarte en una sala, la cual para tu fortuna tiene capsulas de escape,en las que podrias escapar")
                        option1_1_3_1_2_1 = input("\n\nque haras?, ENTRAR O BUSCAR OTRA SALIDA: ").upper() 
                        if option1_1_3_1_2_1 == "ENTRAR" : 
                            print("\n\nentras a la capsula y logras escapar antes e que la nave sea completamente destruida.") 
                            win = True 
                        elif option1_1_3_1_2_1 == "SALIDA" : 
                            print("\n\ndecides buscar otra salida,pero no lo logras a tiempo y terminas muriendo por la explosion de la nave") 
                        else : 
                            print("tardas mucho en elegir una opcion y los guardias te capturan")    
                else : 
                   print("\n\ntardas demasido en tomar una desicion y terminas muriendo")
                    
            elif option1_1_3 == "ESPERAR" : 
                print("\n\ndecides esperar, pero en ese momento entran guardias,y logran capturarte.")  
                win = False
            else :
                print("\n\ntardas mucho en tomarbuna decision y mueres") 
        else :  
            print("\n\ntardas mucho en decidir y mueres") 

    elif option1_1 == "derecho" :
        print("\n\nTe diriges por el pasillo derecho, al final del pasillo ves dos puertas grandes que se abren, llevandote a una enorme sala de control y a una habitacion llena de camillas con cadenas.") 
        option1_1_2 = input("\nPor cual puerta iras? CONTROL O CAMILLAS:").upper()

        if option1_1_2 == "CONTROL":
            print("\n\nEntras a la sala de control, varios aliens estan operando la nave, al verte entran en alerta y llaman a los guardias.")
            option1_1_2_2 = input("\n\nQue haras? HUIR o LUCHAR:").upper()
            if option1_1_2_2 == "HUIR":
                print("\n\nAl huir te encuestras con una puerta la cual lleva a un laboratorio vacio, exepto por otro humano que vez atado a una camilla, el cual te ve y te implora que lo ayudes.") 
                option1_1_2_2_2 = input("\n\nQue haras? AYUDARLO o SEGUIR HUYENDO:").upper()

                if option1_1_2_2_2 == "AYUDARLO":
                    print(" \n\nLogras liberarlo y ambos salen corriendo por el pasillo, esta persona que te acompaña te guia a una sala donde hay capsulas de evacuacion.")
                    option1_1_2_2_2_1 = input("\n\nQue haras? ENTRAR o NO ENTRAR:").upper()

                    if option1_1_2_2_2_1 == "ENTRAR":
                        print("\n\nLogran entrar a una capsula y escapar de la nave, cayendo en un bosque lejano a tu casa.") 
                        win = True
                    elif option1_1_2_2_2_1 == "NO ENTRAR":
                        print("\n\nDecides no confiar en el otro humano y seguir huyendo, pero los guardias te encuentran y terminan contigo. ") 
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                        win = False

                elif option1_1_2_2_2 == "SEGUIR HUYENDO": 
                    print("\n\nDecides huir e ignorar la suplicas de la otra persona y continuas por el pasillo.")
                    option1_1_2_2_2_1 = input("\n\nQue haras? CONTINUAR o REGRESAR:").upper()

                    if option1_1_2_2_2_1 == "CONTINUAR":
                        print("\n\nSigues corriendo por el pasillo, pero te topas con un grupo de guardias que te atrapan y terminan contigo.")
                        win = False
                    elif option1_1_2_2_2_1 == "REGRESAR":
                        print("\n\nDecides regresar y ayudar al otro humano, pero al hacerlo los guardias te encuentran y terminan contigo.")
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo.")
                        win = False

                else:
                    print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo.")
                    win = False

            elif option1_1_2_2 == "LUCHAR": 
                print("\n\nIntentas luchar contra los navegantes para tomar control de la nave, uno de ellos corre hacia un boton de alerta, puedes atacarlo o intentar tomar control de la nave.") 
                option1_1_2_2 = input("\n\nQue haras? ATACARLO o TOMAR CONTROL: ").upper()

                if option1_1_2_2 == "ATACARLO":
                    print("\n\nAtacas al alien y lo derribas, evitando que llame a los guardias. Los otros aliens toman control de la nave nuevamente, puedes intentar quitarle el control de la nave a los aliens o pulsar uno de los botones de la consola que tienes enfrente.")
                    option1_1_2_2_1 = input("\n\nQue haras? QUITAR CONTROL o PULSAR BOTON: ").upper()

                    if option1_1_2_2_1 == "QUITAR CONTROL":
                        print("\n\nIntentas quitarle el control de la nave a los aliens, pero no tienes idea de como hacerlo, estrellando la nave contra la tierra.") 
                        win = False
                    elif option1_1_2_2_1 == "PULSAR CONTROL":
                        print("\n\nDecides pulsar uno de los botones de la consola, pero no sabes que hace y activas una alarma. Los guardias llegan y terminan contigo.")
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                        win = False
                
                elif option1_1_2_2 == "TOMAR CONTROL": 
                    print("\n\nCorres hacia la consola, quitando a los aliens del camino y tomando control de la nave, puedes intentar regresar a la tierra o estrellar la nave en algun lugar alejado.")
                    option1_1_2_2_1 = input("\n\nQue haras? REGRESAR a la tierra o ESTRELLAR la nave: ").upper()

                    if option1_1_2_2_1 == "ESTRELLAR":
                        print("\n\nIntentas regresar a la tierra, pero no sabes como pilotear la nave y terminas estrellandote en el oceano, muriendo en el proceso. ") 
                        win = False
                    elif option1_1_2_2_1 == "REGRESAR":
                        print("\n\nDecides regresar a la tierra, pero no sabes como pilotear la nave y terminas estrellandote en el oceano, muriendo en el proceso. ") 
                        win = False
                    else:
                        print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                        win = False
                
                else:
                    print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                    win = False

            else:
                print("\n\nTardas demasiado en decidir y los guardias te encuentran y terminan contigo. ") 
                win = False
    
        elif option1_1_2 == "CAMILLAS": 
            print("\n\nEntras a la habitacion llena de camillas, varias de ellas tienen humanos atados, puedes intentar liberarlos o buscar algun objeto que te ayude a escapar.") 
            option2 = input("que haras?, LIBERARLOS O BUSCAR: ") 
            if option2 == "LIBERARLOS" : 
                print("Te acercas al humano más cercano y, con un gran esfuerzo, logras soltarlo. Él te mira con gratitud y te susurra: Gracias. Me obligaron a trabajar en los sistemas de ventilación. Conozco una ruta.Juntos, liberan a los demás prisioneros. Una vez que están todos de pie, el guía que acabas de salvar señala una rejilla en la parte alta de la pared.—Podemos ir por los conductos. Es lento, pero seguro, susurra.Sin embargo, otra de las liberadas, de aspecto ansioso, interviene en voz baja:¡No hay tiempo! La esclusa del hangar principal está más cerca. Si corremos ahora, podemos lograrlo antes de que den la alarma.El grupo se divide en miradas, y todos esperan tu decisión..") 
                option2_2 = input("¿Qué plan eliges?, VENTILACION O HANGAR") 
                if option2_2 == "VENTILACION" : 
                    print("Decides que el sigilo es la mejor opción y le haces una seña al guía para que los dirija. Se ayudan unos a otros para alcanzar la rejilla y, uno por uno, se deslizan en la fría oscuridad del conducto. El espacio es reducido y el sonido de sus movimientos parece amplificarse en el silencio metálico.Después de varios minutos arrastrándose en fila, llegan a una bifurcación.El conducto de la izquierda emite un fuerte zumbido mecánico y un calor intenso.Por el de la derecha se filtran extraños y guturales murmullos alienígenas.El guía te mira y se encoge de hombros; no recuerda esta parte de la red. La decisión, de nuevo, es tuya.")
                    option2_2_2 = input("que elejiras?IZQUIERDA O DERECHA: ") 
                    if option2_2_2 == "IZQUIERDA" :
                        print("Eliges el camino de la izquierda, avanzando con dificultad hacia el calor. El zumbido se vuelve ensordecedor. De repente, el suelo del conducto, debilitado por el calor, cede bajo su peso. Caen estrepitosamente en una sala de máquinas llena de pistones y cables. El estruendo alertó a los técnicos alienígenas, quienes bloquean la única salida y activan una alarma. Están atrapados.") 
                        win = False 
                    elif option2_2_2 == "DERECHA" : 
                        print("Con la máxima cautela, guías al grupo por el conducto de la derecha. Los murmullos se hacen más claros; parecen venir de una sala de descanso para la tripulación. Pasan sigilosamente por encima de la rejilla que da a esa sala y, más adelante, el conducto desemboca exactamente donde esperaban: una bahía de evacuación de emergencia, vacía y silenciosa. Adentro hay una única cápsula de escape. Se apresuran, se amontonan dentro y logran activar la secuencia de lanzamiento justo cuando escuchan las alarmas desatarse a sus espaldas. A través de la ventanilla, ven la gigantesca nave hacerse pequeña mientras ustedes huyen hacia la libertad.") 
                        win = True
                elif option2_2 == "HANGAR" : 
                    print("Optas por la velocidad y el riesgo. ¡Ahora!, susurras con urgencia. El grupo sale corriendo en tropel por el pasillo metálico. La audacia casi funciona; logran avanzar por dos corredores sin ser vistos. Pero al doblar la última esquina antes del hangar, se topan de frente con una patrulla de guardias. La sorpresa dura solo un segundo antes de que los alienígenas levanten sus armas. No tienen a dónde huir. La apuesta no dio resultado.") 
                    win = False     
                else : 
                    print("tradas en tomar una decision y los guardias te atrapan") 
                
            elif option2 == "BUSCAR" : 
                print("Optas por la velocidad y el riesgo. ¡Ahora!, susurras con urgencia. El grupo sale corriendo en tropel por el pasillo metálico. La audacia casi funciona; logran avanzar por dos corredores sin ser vistos. Pero al doblar la última esquina antes del hangar, se topan de frente con una patrulla de guardias. La sorpresa dura solo un segundo antes de que los alienígenas levanten sus armas. No tienen a dónde huir. La apuesta no dio resultado.") 
                win = False
            
    else:
       print("\n\nNo eliges ningun pasillo, y los guardias te encuentran y terminan contigo. ")
       win = False  

elif option1 == "esperar" :
    print("\n\nDecides esperar. Los aliens regresan y comienzan a discutir sobre ti en su idioma extraño. Finalmente, parecen dudar sobre qué hacer contigo.")
    option1_2 = input("\n\tQue haras? COOPERAR o RESISTIR: ").lower()

    if option1_2 == "cooperar" :
        print("\n\nLos aliens notan tu calma y deciden conducirte por un pasillo con dos puertas iluminadas y marcadas por simbolos, uno parecido a una 'x', el otro parecido a una 'y'.")
        option1_2_1 = input("\n\tPor cual puerta entraras? 'X' o 'Y': ").lower()

        if option1_2_1 == "x" :
            print("\n\nTras la puerta 'X', entras en una sala con una pantalla gigante mostrando imagenes de la Tierra. Un boton en la tabla de comandos esta a tu alcance.")
            option1_2_1_1 = input("\n\tQue haras? OBSERVAR o TOCAR: ").lower()

            if option1_2_1_1 == "observar" :
                print("\n\nLa pantalla cambia, mostrando imagenes de calma y destruccion. Los aliens parecen interesados en tu reaccion.")
                option1_2_1_1_1 = input("\n\tCuales te interesan mas? CALMA o DESTRUCCION: ").lower()

                if option1_2_1_1_1 == "calma" :
                    print("\n\nLa imagen de calma crea un pequeño portal frente a ti. Parece que los aliens terminaron su investigacion contigo, quien sabe que habra tras ese portal.")
                    option1_2_1_1_1_1 = input("\n\tQue haras? ENTRAR o RECHAZAR: ").lower()

                    if option1_2_1_1_1_1 == "entrar" :
                        print("\n\nCruzas el portal y apareces en tu habitacion. La nave se desvanece del cielo.")
                        win = True
                    elif option1_2_1_1_1_1 == "rechazar" :
                        print("\n\nEl portal se colapsa. Los aliens consideran que prefieres mantenerte siendo investigado y te retienen.")
                        win = False
                    else :
                        print("\n\nDudas demasiado, el portal se cierra y un campo de contencion te inmoviliza.")
                        win = False

                elif option1_2_1_1_1 == "destruccion" :
                    print("\n\nUn pulso mental recorre tu cabeza, sientes comandos e instrucciones entrando a tu mente.")
                    option1_2_1_1_1_2 = input("\n\tComo reaccionas? ACEPTAR o RESISTIR: ").lower()

                    if option1_2_1_1_1_2 == "aceptar" :
                        print("\n\nAceptas la conexion, los aliens te envian de vuelta a la tierra con un proposito desconocido.")
                        win = True
                    elif option1_2_1_1_1_2 == "resistir" :
                        print("\n\nResistes como puedes los comandos e instrucciones. Los aliens ven tu resistencia y deciden seguir investigando.")
                        win = False
                    else :
                        print("\n\nTu mente colapsa entre señales contradictorias.")
                        win = False
                else :
                    print("\n\nTu reaccion es inentendible, los aliens te consideran fallido y apagan la sala contigo dentro.")
                    win = False

            elif option1_2_1_1 == "tocar" :
                print("\n\nAl tocar el boton, la pantalla se apaga, los aliens te observan.")
                option1_2_1_1_2 = input("\n\tComo reaccionas? CONFUNDIDO o DESAFIANTE: ").lower()

                if option1_2_1_1_2 == "confundido" :
                    print("\n\nLos aliens no parecen descubrir lo que hiciste.")
                    option1_2_1_1_2_1 = input("\n\tMientras los aliens discuten, que haras? ESPERAR o ESCAPAR: ").lower()

                    if option1_2_1_1_2_1 == "esperar" :
                        print("\n\nEsperas pacientemente y los aliens terminan el experimento y te llevan a una capsula criogenica.")
                        win = False
                    elif option1_2_1_1_2_1 == "escapar" :
                        print("\n\nTu intento de escape es fallido, no eres capaz de liberarte de tus ataduras antes de que te envien a una capsula criogenica")
                        win = False
                    else :
                        print("\n\nLos aliens terminan su discousion y deciden que eres un sujeto no cooperativo.")
                        win = False

                elif option1_2_1_1_2 == "desafiante" :
                    print("\n\nLos aliens no aprecian tu actitud y te llevan al pasillo.")
                    option1_2_1_1_2_2 = input("\n\tQue haras? RESIGNARTE o LUCHAR: ").lower()

                    if option1_2_1_1_2_2 == "resignarte" :
                        print("\n\nAceptas tu destino y te llevan a una sala de contencion.")
                        win = False
                    elif option1_2_1_1_2_2 == "luchar" :
                        print("\n\nLuchas con todas tus fuerzas, pero los aliens son demasiado fuertes.")
                        win = False
                    else :
                        print("\n\nEres lanzado a una zona de desechos.")
                        win = False
                else :
                    print("\n\nLos aliens vieron tu mano en el boton y no aprecian tu accion. Eres confinado para observacion.")
                    win = False
            else :
                print("\n\nApartas la vista de la pantalla, tu falta de cooperacion te muestra como un especimen inutil y eres llevado a la zona de desechos.")
                win = False

        elif option1_2_1 == "y" :
            print("\n\nTras la puerta 'Y' hay jaulas con criaturas extraterrestres, los aliens te dejan frente a dos de ellas, una parecida a un insecto, la otra parecida a un anfibio.")
            option1_2_1_2 = input("\n\tCual elegiras? INSECTO o ANFIBIO: ").lower()

            if option1_2_1_2 == "insecto" :
                print("\n\nEstiras la mano hacia la jaula del insecto, el cual acerca su cabeza a tu mano.")
                option1_2_1_2_1 = input("\n\tQue haras con tu mano? ACERCARLA o RETIRARLA: ").lower()

                if option1_2_1_2_1 == "acercarla" :
                    print("\n\nEl insecto acerca su cabeza a tu mano, mordiendote, puedes sentir un liquido correr por tus venas, no sabes si sera beneficioso o toxico.")
                    option1_2_1_2_1_1 = input("\n\tQue haras con tu mano? MANTENERLA o QUITARLA:  ").lower()

                    if option1_2_1_2_1_1 == "mantenerla" :
                        print("\n\nEl liquido comienza a hacer efecto, derritiendote desde adentro.")
                        win = False
                    elif option1_2_1_2_1_1 == "quitarla" :
                        print("\n\nRetiras tu mano, pero el liquido ya ha entrado a tu cuerpo, derrtiendo tu mano.")
                        win = False
                    else :
                        print("\n\nLos aliens cortan tu mano para evitar que el liquido se propague, dejandote incapacitado para mas experimentos.")
                        win = False

                elif option1_2_1_2_1 == "retirarla" :
                    print("\n\nRetiras tu mano a tiempo, el insecto choca con la jaula al intentar morderte. Los aliens revelan un boton para matar el insecto.")
                    option1_2_1_2_1_2 = input("\n\tQue haras? PRESIONARLO o IGNORARLO: ").lower()

                    if option1_2_1_2_1_2 == "presionarlo" :
                        print("\n\nPresionas el boton, el insecto muere, los aliens entienden tu reaccion y determinan que el experimento a concluido, liberandote.")
                        win = True
                    elif option1_2_1_2_1_2 == "ignorarlo" :
                        print("\n\nIgnoras el boton, el insecto sigue intentando morderte, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False
                    else :
                        print("\n\nNo haces nada, el insecto consigue morderte y mueres por el veneno.")
                        win = False
                else :
                    print("\n\nNo haces nada, el insecto consigue morderte y mueres por el veneno.")

            elif option1_2_1_2 == "anfibio" :
                print("\n\nTe acercas a la jaula del anfibio, el cual te observa con curiosidad, te sientes atraido a acercar tu mano.")
                option1_2_1_2_2 = input("\n\tQue haras? ACERCAR o IGNORAR: ").lower()

                if option1_2_1_2_2 == "acercar" :
                    print("\n\nEl anfibio se acerca a tu mano, su piel es suave y gelatinosa, sientes una conexión telepática.")
                    option1_2_1_2_2_1 = input("\n\tQue haras? ALEJARTE o ESCUCHAR: ").lower()

                    if option1_2_1_2_2_1 == "alejarte" :
                        print("\n\nTe alejas lentamente, el anfibio te observa con tristeza. Los aliens parecen apreciar tu respuesta. Te liberan poco despues.")
                        win = True
                    elif option1_2_1_2_2_1 == "escuchar" :
                        print("\n\nTe concentras en la conexión telepática y comienzas a escuchar los pensamientos del anfibio, perdiendote en su mente.")
                        win = False
                    else :
                        print("\n\nNo reaccionas ante el anfibio, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False

                elif option1_2_1_2_2 == "ignorar" :
                    print("\n\nIgnoras al anfibio. Al intentar mirar a otro lado, sientes una fuerza extraña en tu mente.")
                    option1_2_1_2_2_2 = input("\n\tQue haras? MIRARLO o IGNORARLO: ").lower()

                    if option1_2_1_2_2_2 == "mirarlo" :
                        print("\n\nMiras al anfibio a los ojos, no parece apreciar haber sido ignorado. Utiliza tu poder mental para destruir tu mente.")
                        win = False
                    elif option1_2_1_2_2_2 == "ignorarlo" :
                        print("\n\nIntentas ignorar al anfibio. Los aliens aprecian tu decision, cerrando la jaula del anfibio y liberandote.")
                        win = True
                    else :
                        print("\n\nNo tomas ninguna accion, los aliens deciden que eres un sujeto no cooperativo.")
                        win = False
                else :
                    print("\n\nNo haces nada, los aliens deciden que eres un sujeto no cooperativo.")
                    win = False
        else :
            print("\n\nNo eliges ninguna puerta, te vuelven a sujetar a la camilla y te confinan para observacion.")
            win = False

    elif option1_2 == "resistir" :
        print("\n\nTe resistes con fuerza, sorprendiendo a los aliens. Uno abre dos compartimentos en la pared.")
        option1_2_2 = input("\n\tPor cual compartimento entraras? IZQUIERDO o DERECHO: ").lower()

        if option1_2_2 == "izquierdo" :
            print("\n\nEl compartimento izquierdo es una camara de simulacion.")
            option1_2_2_1 = input("\n\tQue haras? EXPLORAR o SALIR: ").lower()

            if option1_2_2_1 == "explorar" :
                print("\n\nLa simulacion muestra una ciudad futurista que responde a tu voluntad. Puedes intentar vivir en ella o buscar una forma de destruir la simulacion.")
                option1_2_2_1_1 = input("\n\tQue haras? VIVIR o DESTRUIR: ").lower()

                if option1_2_2_1_1 == "vivir" :
                    print("\n\nLa ciudad te ofrece un hogar perfecto. Realmente parece una ilusion placentera.")
                    option1_2_2_1_1_1 = input("\n\tAceptas? ACEPTAR o DESPERTAR: ").lower()

                    if option1_2_2_1_1_1 == "aceptar" :
                        print("\n\nAceptas la ilusion y vives una vida plena en la simulacion.")
                        win = True
                    elif option1_2_2_1_1_1 == "despertar" :
                        print("\n\nRechazas la ilusion, forzando un reinicio, los aliens te reciben molestos.")
                        win = False
                    else :
                        print("\n\nLa simulacion se corrompe y quedas atrapado.")
                        win = False

                elif option1_2_2_1_1 == "destruir" :
                    print("\n\nEncuentras vulnerabilidades en el entorno virtual. Puedes intentar escapar la simulacion o tomar tu tiempo para destruirla.")
                    option1_2_2_1_1_2 = input("\n\tAccion? HUIR o DESTRUIR: ").lower()

                    if option1_2_2_1_1_2 == "huir" :
                        print("\n\nAbres una brecha en el codigo y tu conciencia es transportada a la realidad. Los aliens parecen molestos ante tus acciones, confinandote nuevamente.")
                        win = False
                    elif option1_2_2_1_1_2 == "destruir" :
                        print("\n\nUtilizas tu poder sobre la simulacion para destruirla. Tus esfuerzos, sin embargo, son en vano, los aliens detienen la simulacion y te llevan a una capsula criogenica.")
                        win = False
                    else :
                        print("\n\nLa simulacion se corrompe y quedas atrapado.")
                        win = False

            elif option1_2_2_1 == "salir" :
                print("\n\nConsigues escapar la simulacion, tu cuerpo transportado a una camara de mantenimiento.")
                option1_2_2_1_2 = input("\n\tQue haras? CORRER o ESPERAR: ").lower()

                if option1_2_2_1_2 == "correr" :
                    print("\n\nEl corredor conectado a la camara lleva a una esclusa con sirenas activas.")
                    option1_2_2_1_2_1 = input("\n\tUltimo paso? CORRER o OCULTARTE: ").lower()

                    if option1_2_2_1_2_1 == "correr" :
                        print("\n\nCorres hasta un modulo de escape y despegas hacia la Tierra.")
                        win = True
                    elif option1_2_2_1_2_1 == "ocultarte" :
                        print("\n\nTe ocultas hasta que la seguridad de la nave te encuentra.")
                        win = False
                    else :
                        print("\n\nTe quedas inmovil y la seguridad de la nave te atrapa.")
                        win = False

                elif option1_2_2_1_2 == "esperar" :
                    print("\n\nTe quedas inmovil, escuchando pasos acercarse.")
                    option1_2_2_1_2_2 = input("\n\tPlan? PEDIR AYUDA o RENDIRTE: ").lower()

                    if option1_2_2_1_2_2 == "pedir ayuda" :
                        print("\n\nUn tecnico alien te escucha, alertando la seguridad de la nave de tu presencia.")
                        win = False
                    elif option1_2_2_1_2_2 == "rendirte" :
                        print("\n\nLevantas las manos, te recluyen permanentemente.")
                        win = False
                    else :
                        print("\n\nLa seguridad de la nave te encuentra y te atrapa.")
                        win = False

                else :
                    print("\n\nLa salida se sella y quedas atrapado.")
                    win = False

            else :
                print("\n\nTe quedas atrapado en la simulacion.")
                win = False

        elif option1_2_2 == "derecho" :
            print("\n\nEl compartimento derecho conduce a un hangar con dos naves pequenas. Los aliens parecen interesados en tu preferencia, la NAVE 1 es circular y la NAVE 2 es rectangular.")
            option1_2_2_2 = input("\n\tCual eliges? NAVE 1 o NAVE 2: ").lower()

            if option1_2_2_2 == "nave 1" :
                print("\n\nLa NAVE 1 esta operativa, pero los controles son indescifrables. Los aliens esperan tu decision.")
                option1_2_2_2_1 = input("\n\tPilotearas la nave? PILOTEAR o NO PILOTEAR: ").lower()

                if option1_2_2_2_1 == "pilotear" :
                    print("\n\nEl sistema se activa y traza una ruta segura. Parece pedir una altura de vuelo.")
                    option1_2_2_2_1_1 = input("\n\tAltura? ALTA ORBITA o BAJA ORBITA: ").lower()

                    if option1_2_2_2_1_1 == "alta orbita" :
                        print("\n\nTu decision de alta orbita es arriesgada, los aliens no parecen convencidos de tu inteligencia al tomar decisiones y detienen el experimento.")
                        win = False
                    elif option1_2_2_2_1_1 == "baja orbita" :
                        print("\n\nLos aliens parecen felices a tu decision, viendote como un experimento exitoso y dejandote ir.")
                        win = True
                    else :
                        print("\n\nElijes una altura de vuelo no válida, terminando el experimento.")
                        win = False

                elif option1_2_2_2_1 == "no pilotear" :
                    print("\n\nDecides no pilotear la nave, los aliens parecen decepcionados pero te permiten elegir otra opcion. Buscaras otra nave o te resignaras a tu destino.")
                    option1_2_2_2_1_2 = input("\n\tQue haras? BUSCAR OTRA NAVE o RESIGNARSE: ").lower()

                    if option1_2_2_2_1_2 == "buscar otra nave" :
                        print("\n\nNo encuentras otra nave, los aliens deciden que eres un experimento fallido.")
                        win = False
                    elif option1_2_2_2_1_2 == "resignarse" :
                        print("\n\nTe resignas a tu destino y esperas lo peor.")
                        win = False
                    else :
                        print("\n\nTu indecision molesta a los aliens.")
                        win = False
                else :
                    print("\n\nLa consola no reconoce tu orden y bloquea el despegue.")
                    win = False

            elif option1_2_2_2 == "nave 2" :
                print("\n\nLa NAVE 2 parpadea con alertas de averia. Ves algunos mecanismos expuestos, puedes intentar repararlos o pilotar la nave.")
                option1_2_2_2_2 = input("\n\tQue haras? REPARAR o ARRIESGAR: ").lower()

                if option1_2_2_2_2 == "reparar" :
                    print("\n\nConsigues estabilizar el reactor temporalmente.")
                    option1_2_2_2_2_1 = input("\n\tDespegar ahora? DESPEGAR o ABORTAR: ").lower()

                    if option1_2_2_2_2_1 == "despegar" :
                        print("\n\nLos aliens parecen satisfechos con tus desiciones, enviandote a la tierra.")
                        win = True
                    elif option1_2_2_2_2_1 == "abortar" :
                        print("\n\nAbortas el despegue y los aliens deciden que eres un experimento fallido.")
                        win = False
                    else :
                        print("\n\nLa reparacion falla y la nave colapsa.")
                        win = False

                elif option1_2_2_2_2 == "arriesgar" :
                    print("\n\nIntentas despegar tal cual, ignorando las alertas. Los aliens permiten que la nave despegue, pero las puertas no se han abierto.")
                    option1_2_2_2_2_2 = input("\n\t Que haras? EJECTAR o ACELERAR: ").lower()

                    if option1_2_2_2_2_2 == "ejectar" :
                        print("\n\nTe eyectas en el ultimo segundo y caes con un paracaidas de energia de vuelta en el hangar.")
                        win = False
                    elif option1_2_2_2_2_2 == "acelerar" :
                        print("\n\nEl motor explota, destruyendo la nave contigo adentro.")
                        win = False
                    else :
                        print("\n\nNo decides y el sistema te apaga por seguridad.")
                        win = False
                else :
                    print("\n\nLa nave no responde a los controles.")
                    win = False
            else :
                print("\n\nNo eres capaz de elegir una nave, los aliens se cansan de esperar.")
                win = False
        else :
            print("\n\nNo eliges un compartimento, los aliens te confinan para observacion.")
            win = False
    else :
        print("\n\nLos aliens no entienden tu respuesta, te confinan para observacion.")
        win = False
else :
    print("\n\nNo eliges una accion, los aliens te mantienen en animacion suspendida.")
    win = False

if win == True :
    print("\n\n\t\tHAS SOBREVIVIDO.")
elif win == False :
    print("\n\n\t\tHAS PERDIDO.")