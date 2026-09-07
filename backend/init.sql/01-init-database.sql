-- Configuración inicial de la base de datos
-- Este archivo se ejecuta automáticamente cuando se crea el contenedor de MySQL

-- La base de datos proyecto_db ya se crea automáticamente por la variable MYSQL_DATABASE
-- El usuario proyecto_user ya se crea automáticamente por las variables MYSQL_USER y MYSQL_PASSWORD

-- Configurar el charset y collation para la base de datos
ALTER DATABASE proyecto_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Otorgar todos los privilegios al usuario (redundante pero por seguridad)
GRANT ALL PRIVILEGES ON proyecto_db.* TO 'enigma_user'@'%';
FLUSH PRIVILEGES;

-- Verificar que todo esté configurado correctamente
SELECT 'Base de datos configurada correctamente' as status;