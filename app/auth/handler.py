from ..models.schema import AuthCredentials, AuthType

class AuthHandler:

    @staticmethod
    def validate_credentails(auth: AuthCredentials, provider: str) -> bool:

        if not auth:
            return True

        if auth.auth_type == AuthType.PASSWORD:
            return auth.username and auth.password
        
        elif auth.auth_type == AuthType.API_KEY:
            return bool(auth.api_key)
        
        elif auth.auth_type == AuthType.OAUTH:
            return bool(auth.auth_token)
        
        return False