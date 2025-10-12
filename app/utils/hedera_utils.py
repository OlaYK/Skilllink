import os
import hashlib
from dotenv import load_dotenv
from hedera import (
    Client,
    AccountId,
    PrivateKey,
    TransactionReceiptQuery,
    TransactionResponse,
    Hbar,
    FileCreateTransaction,
    FileAppendTransaction
)

load_dotenv()

HEDERA_ACCOUNT_ID = os.getenv("HEDERA_ACCOUNT_ID")
HEDERA_PRIVATE_KEY = os.getenv("HEDERA_PRIVATE_KEY")

client = Client.for_testnet()
client.set_operator(AccountId.fromString(HEDERA_ACCOUNT_ID), PrivateKey.fromString(HEDERA_PRIVATE_KEY))

def generate_credential_hash(credential_data: dict) -> str:
    """
    Generates a SHA-256 hash of the credential data.
    """
    data_string = "|".join(str(v) for v in credential_data.values())
    return hashlib.sha256(data_string.encode()).hexdigest()

def store_hash_on_hedera(credential_hash: str) -> str:
    """
    Stores the credential hash on Hedera as a small file and returns the file ID.
    """
    try:
        transaction = FileCreateTransaction().setKeys([PrivateKey.fromString(HEDERA_PRIVATE_KEY)]).setContents(credential_hash.encode())
        tx_response = transaction.execute(client)
        receipt = tx_response.getReceipt(client)
        file_id = receipt.fileId.toString()
        return file_id
    except Exception as e:
        print("Error storing hash on Hedera:", e)
        return None
