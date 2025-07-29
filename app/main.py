from fastapi import FastAPI, HTTPException, Path
from .models.schemas import IntegerationRequest, IntegerationResponse
from .providers.handlers import PROVIDERS
from .auth.handler import AuthHandler

app = FastAPI(title="Integration Proxy API", version="1.0.0")

@app.post("/integrate/{provider}", response_model=IntegerationResponse)
async def integrate_provider(
    provider: str = Path(..., description="Provider name(e.g., saleforce, ups)"), requestL Integration: IntegerationRequest = None
) -> IntegerationResponse:
    try: 
        if provider.lower() not in PROVIDERS:
            raise HTTPException(
                status_code=404, detail=f"Provider '{provider}' not supported."
                f"Avaiable providers: {list(PROVIDERS.keys())}"
            )

        if request.auth and not AuthHandler.validate_credentials(
            request.auth, provider
        ):
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        
        provider_handler = PROVIDERS[provider.lower()]
        response = await provider_handler.handle_request(request)
        return response

    except HTTPException: 
        raise
    except Exception as e:
        return IntegerationResponse(status = "error", data={}, message=f"Unexpected error: {str(e)}"
        )
    


@app.get("/providers")
async def list_providers():
    return {"providers": list(PROVIDERS.keys())}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)