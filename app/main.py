from fastapi import FastAPI
from .database import Base, engine
from .routes import users, credentials, verification

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SkillLink API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(credentials.router, prefix="/credentials", tags=["Credentials"])
app.include_router(verification.router, prefix="/verification", tags=["Verification"])

@app.get("/")
def root():
    return {"message": "Welcome to SkillLink - Decentralized Credential Verification"}
