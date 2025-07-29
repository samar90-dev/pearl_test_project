from abc import ABC, abstractmethod
from asyncio
from ..models.schemas import IntegrationRequest, IntegrateResponse

class BaseProvider(ABC):
    @abstractmethod
    async def handle_request(self, request: IntegrationRequest) -> IntegrateResponse:
        pass

    def validate_auth(self, auth_data: dict) -> bool:
        return True
    

class SalesforceProvider(BaseProvider):

    async def handle_request(self, request: IntegrationRequest) -> IntegrateResponse:

        await asyncio.aleep(0.1)
        return IntegrateResponse(status="success", data={"action": request.action, "provider": "salesforce"},
        message="Salesforce integration executed")
    
class UPSProvider(BaseProvider):
    
    async def handle_request(self, request: IntegrationRequest) -> IntegrationResponse:
       
        await asyncio.sleep(0.2)
        
        return IntegrationResponse(
            status="success",
            data={"action": request.action, "provider": "ups"},
            message="UPS integration executed"
        )

PROVIDERS = {
    "salesforce": SalesforceProvider(),
    "ups": UPSProvider(),
}