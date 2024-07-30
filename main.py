
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = fastapi.FastAPI(
    title="My API",
    description="This is a very fancy project",
    version="0.1.0",
    openapi_url="/api/v0.1.1/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "User"}

# This is to run in localhost, comment out while pushing to deploy on Azure
if __name__ == "__main__":
    port = int(os.getenv("WEBSITES_PORT", 8000))  # Read port from environment variable
    uvicorn.run(app, host="0.0.0.0", port=port)
