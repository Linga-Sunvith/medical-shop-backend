from fastapi import FastAPI
from app.routers import medicine_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Include routers
app.include_router(medicine_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:8000"],  # Allow the frontend to communicate with the backend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
