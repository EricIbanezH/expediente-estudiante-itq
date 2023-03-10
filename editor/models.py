from django.db import models

# Ya existen las tablas Almuno, empleado y rol
#--------------------------------------------------------------------------
class Rol (models.Model):
    Rol = models.CharField(max_length = 20, verbose_name="Nombre")
    
    class Meta:
        managed = True
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

class Alumnos (models.Model):
    nombre_completo = models.CharField(max_length = 100, verbose_name="Nombre")
    no_control = models.CharField(max_length = 8, verbose_name="No. Control")
    # RegexValidator(regex=r"^\d{8}$")

    class Meta:
        managed = True

class Empleados (models.Model):
    nombre_completo = models.CharField(max_length = 100, verbose_name="Nombre")
    
    class Meta:
        managed = True

#--------------------------------------------------------------------------
    
class Estados (models.Model):
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

class Tipo_Archivos (models.Model):
    extension = models.CharField(max_length=5, verbose_name="Extensión")
    # Ejemplo: pdf, doc, jpg, png, xml, xlsx

    class Meta:
        managed = True
        verbose_name="Tipo de archivo"
        verbose_name_plural="Tipos de archivos"

class Tipo_Tramites (models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    tiempo_estimado = models.IntegerField(default=5, verbose_name="Días estimados") #_______________________
    habilitado = models.BooleanField(verbose_name="Habilitado")

    class Meta:
        managed = True
        verbose_name="Tipo de tramite"
        verbose_name_plural="Tipos de tramites"

class Tipo_Documentos (models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    tamano_MB = models.IntegerField(default=4, verbose_name="Tamaño en MB") 
    
    class Meta:
        managed = True
        verbose_name="Tipo de documento"
        verbose_name_plural="Tipos de documentos"

class Rel_Tram_Doc (models.Model): #Relacion tramite-documento
    tramite = models.ForeignKey(Tipo_Tramites, on_delete=models.CASCADE, verbose_name="Tramite")
    documento = models.ForeignKey(Tipo_Documentos , on_delete=models.CASCADE, verbose_name="Documento")

    class Meta:
        managed = True

class Rel_Tram_Rol (models.Model): #Relacion tramite-rol
    tramite = models.ForeignKey(Tipo_Tramites, on_delete=models.CASCADE, verbose_name="Tramite")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")

    class Meta:
        managed = True

class Rel_Empl_Rol (models.Model): #Relacion empleado-rol
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")

    class Meta:
        managed = True

class Rel_Doc_TipoArch (models.Model): #Relacion Documento-extension
    documento = models.ForeignKey(Tipo_Documentos, on_delete=models.CASCADE, verbose_name="Documento")
    extension = models.ForeignKey(Tipo_Archivos, on_delete=models.CASCADE, verbose_name="Extensión")

    class Meta:
        managed = True

class Entrega_Doc (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno") #______________________________________
    tipo_doc = models.ForeignKey(Tipo_Documentos, on_delete=models.CASCADE, verbose_name="Tipo de documento")
    direccion = models.CharField(max_length=100, verbose_name="Dirección del archivo")

    class Meta:
        managed = True
        verbose_name="Entrega de documento"
        verbose_name_plural="Entregas de documentos"

class Observ_Doc (models.Model):
    documento = models.ForeignKey(Entrega_Doc, on_delete=models.CASCADE, verbose_name="Documento")
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Supervisor") #______________________________________
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name="Estado")
    comentario = models.CharField(max_length=100, verbose_name="Comentario")
    fecha = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        managed = True
        verbose_name="Observación del documento"
        verbose_name_plural="Observaciones del documento"

class Tramite (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno") #______________________________________
    tramite = models.ForeignKey(Tipo_Tramites, on_delete=models.CASCADE, verbose_name="Tramite")
    
    class Meta:
        managed = True
        verbose_name="Tramite"
        verbose_name_plural="Tramites"

class Observ_Tramite (models.Model):
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE, verbose_name="Tramite")
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Supervisor") #______________________________________
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name="Estado")
    comentario = models.CharField(max_length=100, verbose_name="Comentario")
    fecha = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        managed = True
        verbose_name="Observación del tramite"
        verbose_name_plural="Observaciones del tramite"

