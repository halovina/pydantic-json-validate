# JSON string dengan data yang SALAH
json_data_salah = """
{
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "username": "eko",
    "first_name": "E", 
    "last_name": "Kurniawan",
    "age": 15,
    "experience_years": 5,
    "penalty_points": 10,
    "level": 5,
    "rating": 1.2,
    "email": "bukan-email",
    "tags": [],
    "favorite_foods": [],
    "followers": ["A", "B", "A"],
    "address": {
        "street": "Jl. Sudirman",
        "city": "Jakarta",
        "zip_code": "123"
    },
    "legacy_id": true,
    "join_date": "2025-10-25",
    "password": "xxxxx",
    "confirm_password": "xxx"
}
"""

# JSON string dengan data yang BENAR
json_data_benar = """{
    "userId": "123e4567-e89b-12d3-a456-426614174000",
    "username": "Anjas.Mara",
    "first_name": "Anjas",
    "last_name": "Mara",
    "age": 30,
    "experience_years": 5,
    "penalty_points": 10,
    "level": 5,
    "rating": 4.5,
    "email": "anjas@example.com",
    "tags": ["python", "fastapi"],
    "favorite_foods": ["Nasi Goreng"],
    "followers": ["andi", "budi", "charlie"],
    "address": {
        "street": "Jl. Thamrin",
        "city": "Jakarta Pusat",
        "zip_code": "10210"
    },
    "legacy_id": "LGC-12345",
    "join_date": "2024-01-01",
    "password": "xxxxxx!",
    "confirm_password": "xxxxxx!"
}"""

