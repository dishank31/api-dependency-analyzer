from src.schemas.auth import UserRegister
from src.schemas.service import ServiceCreate
from src.schemas.endpoint import EndpointCreate

# Should pass
u = UserRegister(email="test@example.com", password="strongpass")
print("UserRegister OK:", u.email)

# Should fail — password too short
try:
    UserRegister(email="test@example.com", password="short")
except Exception as e:
    print("Caught expected error:", e)

# Should normalise to lowercase
s = ServiceCreate(name="Payment-Service")
print("ServiceCreate normalised:", s.name)  # → payment-service

# Should fail — bad method
try:
    EndpointCreate(path="/users", method="FETCH")
except Exception as e:
    print("Caught expected error:", e)

print("All schema tests done.")