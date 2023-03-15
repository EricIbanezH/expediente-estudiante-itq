-- Valores de prueba

-- Estados
INSERT INTO `estados` (`nombre`) VALUES ('Aceptado');
INSERT INTO `estados` (`nombre`) VALUES ('Rechazado');
INSERT INTO `estados` (`nombre`) VALUES ('Pendiente');
INSERT INTO `estados` (`nombre`) VALUES ('Correccion');
INSERT INTO `estados` (`nombre`) VALUES ('Prorroga');


-- Comentarios
INSERT INTO `comentarios`(`descr`) VALUES ('Documento ilegible');
INSERT INTO `comentarios`(`descr`) VALUES ('Documento incorrecto');
INSERT INTO `comentarios`(`descr`) VALUES ('Falta de firmas y/o sellos');
INSERT INTO `comentarios`(`descr`) VALUES ('Documento desactualizado');

-- Tipo archivo
INSERT INTO `tipo_archivos`(`extension`) VALUES ('pdf');
INSERT INTO `tipo_archivos`(`extension`) VALUES ('docs');
INSERT INTO `tipo_archivos`(`extension`) VALUES ('jpg');

-- Tipo de documento
INSERT INTO `tipo_documentos`(`nombre`, `tamano_MB`) VALUES ('Acta de nacimiento','4');
INSERT INTO `tipo_documentos`(`nombre`, `tamano_MB`) VALUES ('CURP','4');
INSERT INTO `tipo_documentos`(`nombre`, `tamano_MB`) VALUES ('Reporte del Servicio Social no. 1','4');
INSERT INTO `tipo_documentos`(`nombre`, `tamano_MB`) VALUES ('Reporte del Servicio Social no. 2','4');
INSERT INTO `tipo_documentos`(`nombre`, `tamano_MB`) VALUES ('Reporte del Servicio Social no. 3','4');

-- Tipo de tramite
INSERT INTO `tipo_tramites`(`nombre`, `tiempo_estimado`, `habilitado`) VALUES ('Titulacion','50',1);
INSERT INTO `tipo_tramites`(`nombre`, `tiempo_estimado`, `habilitado`) VALUES ('Servicio Social','180',1);
INSERT INTO `tipo_tramites`(`nombre`, `tiempo_estimado`, `habilitado`) VALUES ('Residencias','180',1);

-- Roles
INSERT INTO `roles`(`Rol`) VALUES ('Coordinacion');
INSERT INTO `roles`(`Rol`) VALUES ('Titulacion');
INSERT INTO `roles`(`Rol`) VALUES ('Docente');