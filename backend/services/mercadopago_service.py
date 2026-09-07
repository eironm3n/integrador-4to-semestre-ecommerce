# services/mercadopago_service.py
import os
import mercadopago
from dotenv import load_dotenv

load_dotenv()

class MercadoPagoService:
    @staticmethod
    def create_payment_link(total_amount, external_reference):
        access_token = os.getenv("MP_ACCESS_TOKEN")
        base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000")
        sandbox = os.getenv("MP_SANDBOX", "true").lower() == "true"

        if not access_token:
            raise EnvironmentError("Falta MP_ACCESS_TOKEN")

        sdk = mercadopago.SDK(access_token)

        preference_data = {
            "items": [
                {
                    "title": f"Orden {external_reference}",
                    "quantity": 1,
                    "unit_price": float(total_amount),
                    "currency_id": "ARS"
                }
            ],
            "back_urls": {
                "success": f"{base_url}/payments/success",
                "failure": f"{base_url}/payments/failure",
                "pending": f"{base_url}/payments/pending"
            },
            "external_reference": str(external_reference)
        }

        result = sdk.preference().create(preference_data)
        if result["status"] != 201:
            raise Exception(f"Error creando preferencia: {result}")

        return result["response"]["sandbox_init_point"] if sandbox else result["response"]["init_point"]
