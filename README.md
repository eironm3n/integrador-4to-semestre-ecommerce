# Verdísimo — E-commerce fullstack (Angular + Flask)

> **Continuación individual de un proyecto académico** · Base: proyecto integrador del 4.º semestre
> de la Tecnicatura Universitaria en Programación — UTN, Facultad Regional San Rafael (2025),
> realizado con el equipo **Código Enigma**. Ver [Origen del proyecto](#origen-del-proyecto).

Tienda online completa: catálogo de productos, categorías, carrito de compras,
usuarios con autenticación y checkout con pasarela de pago. Frontend y backend
se despliegan por separado.

## Tecnologías

### Frontend (`/frontend`)

- **Angular 21** (standalone components, control flow `@if`/`@for`) · **TypeScript** · **SCSS**
- UI con **Nebular 17**
- Despliegue en **Vercel**

> Entregado originalmente en Angular 19; migrado después a Angular 21 con `ng update`
> (Nebular 17 es la última versión y solo admite Angular 21).

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
cp .env.example .env    # completar DB_* y SECRET_KEY (obligatoria en producción)
flask --app app db upgrade && python seed.py
flask --app app run --debug

# Frontend
cd frontend
npm install
ng serve -o
```

La URL del backend se configura en `frontend/src/environments/environment.ts` (desarrollo)
y `environment.prod.ts` (producción, la usa `ng build`).

Detalle completo (base de datos, `.env`, migraciones y seeders) en
[`backend/README-original.md`](./backend/README-original.md).

## Origen del proyecto

Este repositorio usa como **base principal el proyecto integrador de la Tecnicatura
Universitaria en Programación** (UTN, Facultad Regional San Rafael). El proyecto se
comenzó en **septiembre de 2025** y se realizó durante el 4.º semestre con el equipo
**Código Enigma**, hasta su entrega final en **noviembre de 2025**.

Durante la tecnicatura el equipo trabajó con **rotación de roles** (desarrollo,
gestión de tareas y seguimiento de avances semanales), y la publicación en los
repositorios de la cátedra la centralizaban algunos integrantes por turno.

### Continuación individual

A partir de esa base, **Arón Rojas**, integrante del equipo, continúa el proyecto
de forma individual en este repositorio:

- Unificación del frontend y el backend (que la cátedra mantenía en dos repositorios) en uno solo.
- Migración del frontend de **Angular 19 a Angular 21** y de Nebular 15 a 17, con la
  sintaxis moderna de control flow (`@if`/`@for`) y el constructor `@angular/build`.
- Actualización de dependencias: el frontend pasó de 73 vulnerabilidades conocidas a **0**,
  y el backend (Flask, Werkzeug, PyJWT, cryptography, entre otras) también quedó sin vulnerabilidades conocidas.
- Seguridad: la clave que firma los tokens JWT pasa a ser obligatoria en producción.
- Configuración de entornos (`src/environments`) para que el proyecto compile desde un clon limpio.

### Repositorios originales de la cátedra

- Frontend: <https://github.com/PowerSystem2024/CodigoEnigma_ProyectoIntegrador_CuartoSemestre_Front>
- Backend: <https://github.com/PowerSystem2024/CodigoEnigma_ProyectoIntegrador_CuartoSemestre_Back>
