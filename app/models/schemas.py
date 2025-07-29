from pydantic import BaseModel
from typing import Dict, Any, Optional
from enum import Enum

class AuthType(str, Enum):
    PASSWORD = "password"
    API_KEY = "api_key"
    OAUTH = "oauth"


class AuthCredentails(BaseModel):
    auth_type: AuthType
    username: Optional[str] = None
    password: Optional[str] = None
    api_key: Optional[str] = None
    oauth_token: Optional[str] = None

class IntegrationRequest(BaseModel):
    action: str
    parameter: Dict[str, Any]
    auth: Optional[AuthCredentails] = None

class IntegrationResponse(BaseModel):
    status: str
    data: Dict[str, Any]
    message: Optional[str] = None

    