from utils.jwt_handler import create_access_token, verify_access_token

token=create_access_token({"sub":"testuser"})

print(token)
payload=verify_access_token(token)
print(payload)