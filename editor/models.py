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
    nombre = models.CharField(max_length=10,verbose_name="Nombre")
    # ENTREGADO, CANCELADO, ATRASADO, INICIADO, PENDIENTE, 
    
    class Meta:
        managed = True
        verbose_name="Estado"
        verbose_name_plural="Estados"

class Comentarios (models.Model):
    descr = models.CharField(max_length=100, verbose_name="Descripción")   # Descripcion
    
    class Meta:
        managed = True
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"

class Tipo_Archivo (models.Model):
    extension = models.CharField(max_length=5, verbose_name="Extensión")
    # Ejemplo: pdf, doc, jpg, png, xml, xlsx

    class Meta:
        managed = True
        verbose_name="Tipo de archivo"
        verbose_name_plural="Tipos de archivos"

class Tipo_Tramite (models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    tiempo_estimado = models.IntegerField(default=5, verbose_name="Días estimados") #_______________________
    habilitado = models.BooleanField(verbose_name="Habilitado")

    class Meta:
        managed = True
        verbose_name="Tipo de tramite"
        verbose_name_plural="Tipos de tramites"

class Tipo_Documento (models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    tamano_MB = models.IntegerField(default=4, verbose_name="Tamaño en MB") 
    tipo_arch = models.ForeignKey(Tipo_Archivo, on_delete=models.CASCADE, verbose_name="Tipo de archivo")

    class Meta:
        managed = True
        verbose_name="Tipo de documento"
        verbose_name_plural="Tipos de documentos"

class Rel_Tram_Doc (models.Model): #Relacion tramite-documento
    tramite = models.ForeignKey(Tipo_Tramite, on_delete=models.CASCADE, verbose_name="Tramite")
    documento = models.ForeignKey(Tipo_Documento , on_delete=models.CASCADE, verbose_name="Documento")

    class Meta:
        managed = True

class Rel_Tram_Rol (models.Model): #Relacion tramite-rol
    tramite = models.ForeignKey(Tipo_Tramite, on_delete=models.CASCADE, verbose_name="Tramite")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")  #______________________________________

    class Meta:
        managed = True

class Entrega_Doc (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno") #______________________________________
    tipo_doc = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, verbose_name="Tipo de documento")
    direccion = models.CharField(max_length=100, verbose_name="Dirección del archivo")

    class Meta:
        managed = True
        verbose_name="Entrega de documento"
        verbose_name_plural="Entregas de documentos"

class Observ_Doc (models.Model):
    documento = models.ForeignKey(Entrega_Doc, on_delete=models.CASCADE, verbose_name="Documento")
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Supervisor") #______________________________________
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado")
    comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE, verbose_name="Comentario")
    fecha = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        managed = True
        verbose_name="Observación del documento"
        verbose_name_plural="Observaciones del documento"

class Tramite (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno") #______________________________________
    tramite = models.ForeignKey(Tipo_Tramite, on_delete=models.CASCADE, verbose_name="Tramite")
    
    class Meta:
        managed = True
        verbose_name="Tramite"
        verbose_name_plural="Tramites"

class Observ_Tramite (models.Model):
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE, verbose_name="Tramite")
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Supervisor") #______________________________________
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado")
    comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE, verbose_name="Comentario")
    fecha = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        managed = True
        verbose_name="Observación del tramite"
        verbose_name_plural="Observaciones del tramite"

