// Producción (ng build): reemplaza a environment.ts (ver fileReplacements en angular.json).
// Poner acá la URL pública del backend desplegado. No es un secreto: queda visible en el navegador.
export const environment = {
  production: true,
  // Con barra final: los servicios concatenan rutas como `${apiUrl}products`.
  apiUrl: 'https://tu-backend.vercel.app/',
};
