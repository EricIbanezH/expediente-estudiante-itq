from django.db import models

# Ya existen las tablas Almuno, empleado y rol
#--------------------------------------------------------------------------
class Rol (models.Model):
    Rol = models.CharField(max_length = 20, verbose_name="Nombre")
    
    class Meta:
        managed = True
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        db_table = "roles"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Rol._meta.fields]

class Alumnos (models.Model):
    nombre_completo = models.CharField(max_length = 100, verbose_name="Nombre")
    no_control = models.CharField(max_length = 8, verbose_name="No. Control")
    # RegexValidator(regex=r"^\d{8}$")

    class Meta:
        managed = True
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        db_table = "alumnos"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Alumnos._meta.fields]

class Empleados (models.Model):
    nombre_completo = models.CharField(max_length = 100, verbose_name="Nombre")
    
    class Meta:
        managed = True
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "empleados"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Empleados._meta.fields]

#--------------------------------------------------------------------------
    
class Estados (models.Model):
    nombre = models.CharField(max_length=10,verbose_name="Nombre")
    # ENTREGADO, CANCELADO, ATRASADO, INICIADO, PENDIENTE, 
    
    class Meta:
        managed = True
        verbose_name="Estado"
        verbose_name_plural="Estados"
        db_table = "estados"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Estados._meta.fields]

class Comentarios (models.Model):
    descr = models.CharField(max_length=100, verbose_name="Descripci??n")   # Descripcion
    
    class Meta:
        managed = True
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        db_table = "comentarios"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Comentarios._meta.fields]

class Tipo_Archivos (models.Model):
    extension = models.CharField(max_length=5, verbose_name="Extensi??n")
    # Ejemplo: pdf, doc, jpg, png, xml, xlsx

    class Meta:
        managed = True
        verbose_name="Tipo de archivo"
        verbose_name_plural="Tipos de archivos"
        db_table = "tipo_archivos"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Tipo_Archivos._meta.fields]

class Tipo_Tramites (models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    tiempo_estimado = models.IntegerField(default=5, verbose_name="D??as estimados") #_______________________
    habilitado = models.BooleanField(verbose_name="Habilitado")

    class Meta:
        managed = True
        verbose_name="Tipo de tramite"
        verbose_name_plural="Tipos de tramites"
        db_table = "tipo_tramites"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Tipo_Tramites._meta.fields]

class Tipo_Documentos (models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    tamano_MB = models.IntegerField(default=4, verbose_name="Tama??o en MB") 
    
    class Meta:
        managed = True
        verbose_name="Tipo de documento"
        verbose_name_plural="Tipos de documentos"
        db_table = "tipo_documentos"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Tipo_Documentos._meta.fields]

class Rel_Tram_Doc (models.Model): #Relacion tramite-documento
    tramite = models.ForeignKey(Tipo_Tramites, on_delete=models.CASCADE, verbose_name="Tramite")
    documento = models.ForeignKey(Tipo_Documentos, on_delete=models.CASCADE, verbose_name="Documento")

    class Meta:
        managed = True
        db_table = "rel_tram_doc"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Rel_Tram_Doc._meta.fields]

class Rel_Tram_Rol (models.Model): #Relacion tramite-rol
    tramite = models.ForeignKey(Tipo_Tramites, on_delete=models.CASCADE, verbose_name="Tramite")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")

    class Meta:
        managed = True
        db_table = "rel_tram_rol"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Rel_Tram_Rol._meta.fields]

class Rel_Empl_Rol (models.Model): #Relacion empleado-rol
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Empleado")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")

    class Meta:
        managed = True
        db_table = "rel_emp_rol"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Rel_Empl_Rol._meta.fields]

class Rel_Doc_TipoArch (models.Model): #Relacion Documento-extension
    documento = models.ForeignKey(Tipo_Documentos, on_delete=models.CASCADE, verbose_name="Documento")
    extension = models.ForeignKey(Tipo_Archivos, on_delete=models.CASCADE, verbose_name="Extensi??n")

    class Meta:
        managed = True
        db_table = "rel_doc_tiparch"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Rel_Doc_TipoArch._meta.fields]

class Entrega_Doc (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno") #______________________________________
    tipo_doc = models.ForeignKey(Tipo_Documentos, on_delete=models.CASCADE, verbose_name="Tipo de documento")
    direccion = models.CharField(max_length=100, verbose_name="Direcci??n del archivo")

    class Meta:
        managed = True
        verbose_name = "Entrega de documento"
        verbose_name_plural = "Entregas de documentos"
        db_table = "entrega_documentos"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Entrega_Doc._meta.fields]

class Observ_Doc (models.Model):
    documento = models.ForeignKey(Entrega_Doc, on_delete=models.CASCADE, verbose_name="Documento")
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Supervisor") #______________________________________
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name="Estado")
    comentario = models.CharField(max_length=100, verbose_name="Comentario")
    fecha = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        managed = True
        verbose_name = "Observaci??n del documento"
        verbose_name_plural = "Observaciones del documento"
        db_table = "observ_doc"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Observ_Doc._meta.fields]

class Tramite (models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno") #______________________________________
    tramite = models.ForeignKey(Tipo_Tramites, on_delete=models.CASCADE, verbose_name="Tramite")

    class Meta:
        managed = True
        verbose_name = "Tramite"
        verbose_name_plural = "Tramites"
        db_table = "tramites"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Tramite._meta.fields]

class Observ_Tramite (models.Model):
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE, verbose_name="Tramite")
    supervisor = models.ForeignKey(Empleados, on_delete=models.CASCADE, verbose_name="Supervisor") #______________________________________
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name="Estado")
    comentario = models.CharField(max_length=100, verbose_name="Comentario")
    fecha = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        managed = True
        verbose_name = "Observaci??n del tramite"
        verbose_name_plural = "Observaciones del tramite"
        db_table = "observ_tramites"

    def get_fields_and_values(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Observ_Tramite._meta.fields]