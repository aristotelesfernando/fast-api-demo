import uuid
from datetime import datetime, timedelta
from pathlib import Path

import jwt
from cryptography.hazmat.primitives import serialization


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss": "https://auth.coffeemesh.io/",
        "sub": "d0acdca3-2c73-4f59-a0da-95d40132621c",
        "aud": "http://127.0.0.1:8000/todo",
        "iat": now,
        "exp": (now + timedelta(hours=2)).timestamp(),
        "scope": "openid",
    }

    private_key_text = Path("private_key.pem").read_text()
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(), password=None
    )

    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")

print(generate_jwt())