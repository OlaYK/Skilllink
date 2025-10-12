from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import database
from .. import models
from ..utils.hedera_utils import generate_credential_hash, store_hash_on_hedera

router = APIRouter()

@router.post("/create")
def create_credential(user_id: int, title: str, issuer: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    credential_data = {
        "title": title,
        "issuer": issuer,
        "user": user.email
    }
    credential_hash = generate_credential_hash(credential_data)
    file_id = store_hash_on_hedera(credential_hash)

    if not file_id:
        raise HTTPException(status_code=500, detail="Failed to store hash on Hedera")

    new_credential = models.Credential(
        title=title,
        issuer=issuer,
        verification_hash=file_id,
        owner_id=user.id
    )
    db.add(new_credential)
    db.commit()
    db.refresh(new_credential)

    return {"message": "Credential verified and stored", "file_id": file_id}
