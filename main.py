from usersModel import User
from pydantic import ValidationError
from example_json_data import json_data_salah, json_data_benar
import json


try:
    user = User.model_validate_json(json_data_benar)
    print("Validasi SUKSES! ✅\n")
    # .model_dump() mengubahnya kembali jadi dict
    print(user.model_dump()) 
except ValidationError as e:
    print(f"Validasi GAGAL! ❌\n{e}")