-- Valores de prueba

-- Estados
INSERT INTO `editor_estado` (`nombre`) VALUES ('Aceptado');
INSERT INTO `editor_estado` (`nombre`) VALUES ('Rechazado');
INSERT INTO `editor_estado` (`nombre`) VALUES ('Pendiente');
INSERT INTO `editor_estado` (`nombre`) VALUES ('Correccion');
INSERT INTO `editor_estado` (`nombre`) VALUES ('Prorroga');


-- Comentarios
INSERT INTO `editor_comentarios`(`descr`) VALUES ('Documento ilegible');
INSERT INTO `editor_comentarios`(`descr`) VALUES ('Documento incorrecto');
INSERT INTO `editor_comentarios`(`descr`) VALUES ('Falta de firmas y/o sellos');
INSERT INTO `editor_comentarios`(`descr`) VALUES ('Documento desactualizado');

-- Tipo archivo
INSERT INTO `editor_tipo_archivo`(`extension`) VALUES ('pdf');
INSERT INTO `editor_tipo_archivo`(`extension`) VALUES ('docs');
INSERT INTO `editor_tipo_archivo`(`extension`) VALUES ('jpg');

-- Tipo de documento
INSERT INTO `editor_tipo_documento`(`nombre`, `tamano_MB`, `tipo_arch_id`) VALUES ('Acta de nacimiento','4','1');
INSERT INTO `editor_tipo_documento`(`nombre`, `tamano_MB`, `tipo_arch_id`) VALUES ('CURP','4','1');
INSERT INTO `editor_tipo_documento`(`nombre`, `tamano_MB`, `tipo_arch_id`) VALUES ('Reporte del Servicio Social no. 1','4','1');
INSERT INTO `editor_tipo_documento`(`nombre`, `tamano_MB`, `tipo_arch_id`) VALUES ('Reporte del Servicio Social no. 2','4','1');
INSERT INTO `editor_tipo_documento`(`nombre`, `tamano_MB`, `tipo_arch_id`) VALUES ('Reporte del Servicio Social no. 3','4','1');

-- Tipo de tramite
INSERT INTO `editor_tipo_tramite`(`nombre`, `tiempo_estimado`, `habilitado`) VALUES ('Titulacion','50',1);
INSERT INTO `editor_tipo_tramite`(`nombre`, `tiempo_estimado`, `habilitado`) VALUES ('Servicio Social','180',1);
INSERT INTO `editor_tipo_tramite`(`nombre`, `tiempo_estimado`, `habilitado`) VALUES ('Residencias','180',1);

-- Roles
INSERT INTO `editor_rol`(`Rol`) VALUES ('Coordinacion');
INSERT INTO `editor_rol`(`Rol`) VALUES ('Titulacion');
INSERT INTO `editor_rol`(`Rol`) VALUES ('Docente');