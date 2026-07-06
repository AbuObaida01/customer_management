from utils.password import(hash_password, verify_password)

password="12345"

hashed=hash_password(password)

print("Original :",password)
print("Hashed :",hashed)

print(verify_password("12345", hashed))

print(verify_password("abcde", hashed))