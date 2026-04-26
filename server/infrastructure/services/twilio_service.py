import os
from twilio.rest import Client

class TwilioService:
    def __init__(self):
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.from_number = os.environ.get("TWILIO_WHATSAPP_NUMBER")
        
        self.client = None
        if self.account_sid and self.auth_token:
            self.client = Client(self.account_sid, self.auth_token)

    def send_whatsapp(self, to_phone: str, message: str) -> bool:
        if not self.client or not self.from_number:
            raise ValueError("ERRO: Credenciais do Twilio não encontradas no .env (verifique TWILIO_ACCOUNT_SID, AUTH_TOKEN e NUMBER)")

        to_whatsapp = f"whatsapp:{to_phone}" if not to_phone.startswith("whatsapp:") else to_phone
        
        try:
            print(f"DEBUG: Enviando mensagem REAL para {to_whatsapp}...")
            self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_whatsapp
            )
            return True
        except Exception as e:
            print(f"ERRO TWILIO REAL: {str(e)}")
            return False
