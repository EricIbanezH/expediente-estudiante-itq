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
## Nombramientos de variables, clases, funciones, etc._______________________________________________________________________________
  
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
  
  NO USAR PREFIJOS ejemplo clase_auto, clase_persona. mejor usar las reglas de estandarizacion.
  
  NO USAR ASIGNACIONES MENTALES
  usar nombres que el programador solo recuerda o solo el sabe que significa, usar un nombre
  que revele la intencion.
## Funciones _________________________________________________________________________________________________________________________

  TAMAÑO REDUCIDO
  las funciones deben ser lo mas pequeñas posibles.
  
  HACER UNA COSA
  las funciones deben hacer una sola cosa, cada funcion debe tener una tarea, si la funcion hace mas de 1 tarea, entonces
  la otra tarea se puede realizar desde otra funcion. esta es la clave para hacer codigo para pruebas.
  
  EVITAR USAR INTRUCCIONES SWITCH
  
  ARGUMENTOS DE FUNCIONES
  es ideal que una funcion tenga de 0 a 1 argumento, muchos argumentos hacen mas dificil hacer pruebas unitarias debido
  al numero de cominaciones posibles. si es muy dificil que una funcion tenga pocos argumentos, posiblemente todos los
  argumentos (por ejemplo mas de 3) podrian formar parte de una clase asi se reduciria el numero de argumentos y hace mas
  entendible nuestro codigo.
  ejemplo
  ** def transformar(x,y,z,angulo)
  ** def transformar(Coordenada,angulo)
  
  SIN EFECTO SECUNDARIOS
  las funciones deben hacer solo una cosa segun lo descriva su nombre, si la funcion tiene un efecto secundario no realiza
  una sola cosa y probablemente su nombre de funcion no hace lo que promete por ejemplo:
  ** def comparaUsuarioYContraseña(entradaDeUsuario): if usuario.getContraseña == entradaUsuario {login () return True}
  en la funcion anterior no solo compara una contraseña con una entrada de usuario si no tambien realiza el login, no hace
  una sola cosa y no hace lo que promete.
  
  ARGUMENTOS DE SALIDA
  los argumentos de una funcion deben ser de entrada y no de salida a menos que el nombre de la funcion especifique claramente
  que lo que hace tendra un argumento de salida, por ejemplo:
  no hacer 
  ** public void appendFooter(StringBuffer report)
  **appendFooter(s) /objeto en realidad es un argumento de salida.
  mejor usar la programaicion orientada a objetos:
  StringBuffer report = new StringBuffer();
  report.appendFooter();

## Comentarios.

  SI EL CODIGO NECESITA COMENTARIOS PARA QUE SEA ENTENDIBLE ENTONCES ALGO NO SE ESTA HACIENDO BIEN
  NO ES CODIGO LIMPIO HAY QUE REFACTORIZAR EL CODIGO.
  
 ## concluciones.
 
 siempre hay que revisar el codigo que ver si es lo mas limpio posible, es decir, ver si el codigo esta optimizado,
 ver si se entiende cada parte del codigo, visualizar como si fueras otro programador y ver si se entiende el codigo
 sin necesidad de preguntar que hace cada cosa, la lectura del codigo debe parecer como si contaras una historia, cada
 parte esta conectada logicamente y es entendible.
