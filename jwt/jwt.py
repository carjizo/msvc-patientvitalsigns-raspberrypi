import requests
import jwt.config as cfg


class JWT:
    """ Clase para obtener el Token """
    def __init__(self):
        self.AUTH_READ = cfg.AUTH_READ
        self.AUTH_READ_WRITE = cfg.AUTH_READ_WRITE
        self.AUTH_LOGIN = cfg.AUTH_LOGIN
        self.HEADERS_LOGIN = cfg.HEADERS_LOGIN
        self.DATA_LOGIN = cfg.DATA_LOGIN
        self.AUTH_JWT = cfg.AUTH_JWT
        self.HEADERS_JWT = cfg.HEADERS_JWT
        self.REDIRECT_URI = cfg.REDIRECT_URI

    def on_session(self):
        """ Crear una sesión para mantener las cookies entre las solicitudes """
        return requests.Session()

    def auth_read(self) -> tuple:
        """ Obtener permiso para lectura """
        try:
            session = self.on_session()
            r = session.get(self.AUTH_READ)
            return r.status_code, session
        except Exception as e:
            print(f"GENERIC EXCEPTION: {str(e)}")

    def auth_read_write(self) -> tuple:
        """ Obtener permiso para lectura - escritura """
        try:
            session = self.on_session()
            r = session.get(self.AUTH_READ_WRITE)
            return r.status_code, session
        except Exception as e:
            print(f"GENERIC EXCEPTION: {str(e)}")

    def auth_login(self) -> tuple:
        """ Obtener código de autorización para lectura - escritura """
        code = 'NOT_CODE'
        status_code, session = self.auth_read_write()
        try:
            print("OBTENIENDO EL CODE")
            if status_code == 200:
                r = session.post(self.AUTH_LOGIN, headers=self.HEADERS_LOGIN, data=self.DATA_LOGIN)
                if r.status_code == 200:
                    if type(r.json()) is dict:
                        code = r.json().get('code')
            return code, session
        except Exception as e:
            print(f'status_code: {status_code}')
            print("NO SE OBTUVO EL PERMISO DE LECTURA - ESCRITURA")
            print(f"GENERIC EXCEPTION: {str(e)}")

    def get_token(self) -> str:
        """ Obtener token """
        token = 'NOT_TOKEN'
        try:
            code, session = self.auth_login()
            if code != 'NOT_CODE':
                print("OBTENIENDO TOKEN")
                data = {
                    'code': code,
                    'grant_type': 'authorization_code',
                    'redirect_uri': self.REDIRECT_URI
                }
                r = session.post(self.AUTH_JWT, headers=self.HEADERS_JWT, data=data)
                if r.status_code == 200:
                    print(f'status_code: {r.status_code }')
                    token = r.json().get('access_token')
            return token
        except Exception as e:
            print("NO SE OBTUVO EL CODE")
            print(f"GENERIC EXCEPTION: {str(e)}")
