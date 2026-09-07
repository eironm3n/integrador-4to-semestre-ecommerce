# setup.ps1 - Configura el backend Flask con MySQL desde cero

Write-Host 'Creando entorno virtual...'
python -m venv .venv

Write-Host 'Activando entorno virtual...'
. .\.venv\Scripts\Activate.ps1

Write-Host 'Actualizando pip e instalando dependencias...'
pip install --upgrade pip
pip install -r requirements.txt

Write-Host 'Inicializando migraciones de Flask-Migrate...'
# Comprueba si la carpeta migrations ya existe
if (-Not (Test-Path '.\migrations')) {
    python -m flask --app app db init
    Write-Host 'Carpeta migrations creada.'
} else {
    Write-Host 'La carpeta migrations ya existe, saltando db init...'
}

Write-Host 'Aplicando migracion a la base de datos (usando la head actual)...'
# Esto aplicará todas las migraciones pendientes hasta la current head
python -m flask --app app db upgrade

Write-Host 'Todo listo!'
Write-Host 'Para activar el entorno en otra sesion: .\.venv\Scripts\Activate.ps1'
Write-Host 'Para correr Flask: flask --app app run --debug'
Write-Host 'Podes ejecutar tus seeders con: python seed.py'