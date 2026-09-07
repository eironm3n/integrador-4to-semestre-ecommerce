# E-commerce Fullstack — Proyecto Integrador

> **Trabajo académico** · Tecnicatura Universitaria en Programación — UTN, Facultad Regional San Rafael
> **Entrega final del 4.º semestre** (2025) · Equipo **Código Enigma**

Tienda online completa: catálogo de productos, categorías, carrito de compras,
usuarios con autenticación y checkout con pasarela de pago. Frontend y backend
desplegados por separado.

## Tecnologías

### Frontend (`/frontend`)

- **Angular 17** · **TypeScript** · **SCSS**
- Despliegue en **Vercel**

### Backend (`/backend`)

- **Python** · **Flask 3**
- **SQLAlchemy** + **Alembic** para migraciones
- **MySQL 8**
- Autenticación con **JWT**
- Integración de pagos con **Mercado Pago**
- Seeders, capa de servicios (`services/`), modelos y *schemas*
- CORS habilitado; configuración por variables de entorno (`.env`)

## Puesta en marcha (resumen)

```bash
# Backend
cd backend
python -m venv .venv && . .venv/Scripts/Activate.ps1   # o: source .venv/bin/activate
pip install -r requirements.txt
flask --app app db upgrade && python seed.py
flask --app app run --debug

# Frontend
cd frontend
npm install
ng serve -o
```

Detalle completo (base de datos, `.env`, migraciones y seeders) en
[`backend/README-original.md`](./backend/README-original.md).

## Contexto y autoría

Proyecto integrador grupal del equipo **Código Enigma**, presentado como entrega
final del 4.º semestre. La cátedra lo mantuvo en **dos repositorios** (frontend y
backend); aquí se consolidan en uno solo para facilitar su lectura. El equipo
trabajó con **rotación de roles**: desarrollo, gestión de tareas y seguimiento de
avances semanales; la publicación en los repositorios de la cátedra la
centralizaban algunos integrantes por turno.

Repositorios originales de la cátedra:

- Frontend: <https://github.com/PowerSystem2024/CodigoEnigma_ProyectoIntegrador_CuartoSemestre_Front>
- Backend: <https://github.com/PowerSystem2024/CodigoEnigma_ProyectoIntegrador_CuartoSemestre_Back>
