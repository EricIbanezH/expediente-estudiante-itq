# expediente-estudiante-itq
Creacion de un expediente digital para el ITQ

# Politicas de creacion de codigo
## Objetivo.
  Realizar las siguientes politicas como parte de una buena practica de programacion,
  ademas permitira realizar codigo mantenible y ayuda a la realizacion de pruebas.
  ayudara a crear codigo profesional.

## Bibliografia.
  Robert C. Martin. (2009). Codigo Limpio. 
## Una buenas citas.
  El codigo limpio es simple y directo. El codigo
  limpio se lee como un texto bien escrito. El
  codigo limpio no oculta la intencion del dise
  ñador sino que muestra nitidas abstracciones
  y lineas directas de control. (Grady Booch, citado en Robert C. Martin (2009)).
  
  Podria enumerar todas las cualidades del codigo
  limpio pero hay una principal que engloba a
  todas ellas. El codigo limpio simpre parece que
  ha sido escrito por alguien a quien le importa.
  No hay nada evidente que hacer para mejorarlo.
  El autor del codigo penso en todos los aspectos
  posibles y si intentamons imaginar alguna
  mejora, volvemos al punto de partida y solo
  nos queda disfrutar del codigo que alguien a
  quien le importa realmente nos ha proporcionado.
  (Michael Feathers, citado en Robert C. Martin (2009)).
## Nombramientos de variables, clases, funciones, etc.
  
  ESTADARIZACION:
  Las clases deben difinir sustantivos (entidades) y las funciones verbos (acciones). Uso de
  Camel Case. Clases empiesan con mayuscula, funciones y variables empiezan con minuscula
  en Camel Case la primera letra de cada palabra es con mayuscula excepto la primera
  palabra, ejemplos: enviarMensaje(), borrarArchivo(), estadoDelArchivoActual, etc. Las
  constantes deben estar todas en mayuscula.
  
  USAR NOMBRES QUE REVELEN LAS INTENCIONES:
  deben indicar por que existe, que hace y como se usa. ejemplo.
  **MAL nombramiento: int d; // tiempo transcurrido en dias
  **BUEN nombramiento: int TiempoTranscurridoEnDias;
  
  EVITAR LA DESINFORMACION:
  no usar nombres que den a entender otra informacion, ejemplo,
  **int x,y; ¿son coordenadas cartesianas?
  cuando en realidad las variables son para un contador vertical y horizontal
  de una matriz, mejor poner;
  ** int contadorVertical, contadorHorizontal;
  tambien evitar variaciones minimas en los nombres, ejemplo:
  ** int controladorDeManejoEficcienteDeCadenas;
  ** int controladorDeAlmacenamientoEfficienteDeCadenas;
  
  REALIZAR DISTINCIONES CON SENTIDO.
  cuando se realiza una referencia a 2 elemnetos distintos del mismo ambito se debe
  diferenciar de manera adecuada, por ejemplo, 2 objetos una funcion para copiar una
  cadena.
  ** public void copiarCadena (char cadena1[], char cadena2[] )
  mejor diferenciarlos con sentido como:
  ** public void copiarCadena(char origen[], char destino[])
  
  USAR NOMBRES QUE SE PUEDAN PRONUNCIAR
  Todas los nombres se deben poder pronunciar, para esto no usar acronimos
  por ejemplo para nombrar una variable para guardar el tiempo en dias no usar
  **int tiEnDi; / int ted;
  mejor usar
  **int tiempoEnDias;
  es mejor un nombre largo, que tratar de adivinar que para que es la variable.
  
  
## Funciones.

## Comentarios.
