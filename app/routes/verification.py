from hedera import FileContentsQuery
from fastapi import APIRouter, HTTPException
from ..utils.hedera_utils import client

router = APIRouter()

@router.get("/verify/{file_id}")
def verify_credential(file_id: str):
    try:
        contents = FileContentsQuery().setFileId(file_id).execute(client)
        return {"verified": True, "hash": contents.toString()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Verification failed: {str(e)}")
