from django.db import models

# Ya existen las tablas Almuno, empleado y rol
#--------------------------------------------------------------------------
class Rol (models.Model):
    Rol = models.CharField(max_length = 20)
    
    class Meta:
        managed = True

class Alumnos (models.Model):
    nombre_completo = models.CharField(max_length = 100)
    no_control = models.CharField(max_length = 8)
    # RegexValidator(regex=r"^\d{8}$")

    class Meta:
        managed = True

class Empleados (models.Model):
    nombre_completo = models.CharField(max_length = 100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        managed = True

#--------------------------------------------------------------------------
    
class Estado (models.Model):
    nombre = models.CharField(max_length=10)
    # ENTREGADO, CANCELADO, ATRASADO, INICIADO, PENDIENTE, 
    
    class Meta:
        managed = True

class Comentarios (models.Model):
    descr = models.CharField(max_length=100)   # Descripcion
    
    class Meta:
        managed = True

class Tipo_Archivo (models.Model):
    extension = models.CharField(max_length=5)
    # Ejemplo: pdf, doc, jpg, png, xml, xlsx

    class Meta:
        managed = True

class Tipo_Tramite (models.Model):
    nombre = models.CharField(max_length=40)
    tiempo_estimado = models.IntegerField(default=5) #_______________________
    habilitado = models.BooleanField()

    class Meta:
        managed = True

class Tipo_Documento (models.Model):
    nombre = models.CharField(max_length=40)
    tamano_MB = models.IntegerField(default=4) 
    tipo_arch = models.ForeignKey(Tipo_Archivo, on_delete=models.CASCADE)

    class Meta:
        managed = True

class Rel_Tram_Doc (models.Model): #Reliacion tramite-documento
    tramite = models.ForeignKey(Tipo_Tramite, on_delete=models.CASCADE)
    documento = models.ForeignKey(Tipo_Documento , on_delete=models.CASCADE)

    class Meta:
        managed = True

class Rel_Tram_Rol (models.Model): #Reliacion tramite-rol
    tramite = models.ForeignKey(Tipo_Tramite, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)  #______________________________________

    class Meta:
        managed = True

class Entrega_Doc (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE) #______________________________________
    tipo_doc = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)

    class Meta:
        managed = True

class Observ_Doc (models.Model):
    documento = models.ForeignKey(Entrega_Doc, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE) #______________________________________
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    class Meta:
        managed = True

class Tramite (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE) #______________________________________
    tramite = models.ForeignKey(Tipo_Tramite, on_delete=models.CASCADE)
    
    class Meta:
        managed = True

class Observ_Tramite (models.Model):
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE) #______________________________________
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    class Meta:
        managed = True

