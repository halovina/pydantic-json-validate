import json
from datetime import date
from enum import Enum
from typing import List, Optional, Set, Union, Annotated
from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr,
    HttpUrl,
    Field,
    ValidationError,
    field_validator,
    StrictStr
)

# Untuk contoh 17 (Enum)
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

# Untuk contoh 18 (Nested Model)
class Address(BaseModel):
    street: str
    city: str
    zip_code: Annotated[str, Field(pattern=r'^\d{5}(-\d{4})?$')] # Validasi Regex

class User(BaseModel):
    # 1. Field Wajib (Otomatis jika tanpa default/Optional)
    username: str 
    
    # 2. Field Opsional (Bisa None)
    bio: Optional[str] = None  # atau 'str | None = None'
    
    # 3. Field dengan Nilai Default
    points: int = 0
    
    # 4. Panjang Minimal (min_length)
    first_name: Annotated[str, Field(min_length=2)]
    
    # 5. Panjang Maksimal (max_length)
    last_name: Annotated[str, Field(max_length=50)]
    
    # 6. Tipe Data Ketat (Strict Mode)
    #    Mencegah koersi tipe, misal 123 menjadi "123"
    coupon_code: Optional[StrictStr] = None

    # 7. Angka: Lebih Besar Dari (gt)
    age: Annotated[int, Field(gt=17)]  # Harus > 17 (minimal 18)
    
    # 8. Angka: Lebih Besar Atau Sama Dengan (ge)
    experience_years: Annotated[int, Field(ge=0)]  # Harus >= 0
    
    # 9. Angka: Kurang Dari (lt)
    penalty_points: Annotated[int, Field(lt=100)] # Harus < 100

    # 10. Angka: Kurang Dari Atau Sama Dengan (le)
    level: Annotated[int, Field(le=99)] # Harus <= 99
    
    # 11. Angka: Kelipatan Dari (multiple_of)
    rating: Annotated[float, Field(multiple_of=0.5)] # Harus kelipatan 0.5

    # 12. Validasi Tipe Spesifik: Email
    email: EmailStr
    
    # 13. Validasi Tipe Spesifik: URL
    website: Optional[HttpUrl] = None

    # 14. Alias Field (Key JSON berbeda dari nama field Python)
    user_id: Annotated[UUID, Field(alias="userId")] # JSON akan pakai "userId"
    
    # 15. List dengan Tipe Tertentu
    tags: List[str]
    
    # 16. List dengan Jumlah Item Minimal (min_items)
    # 17. List dengan Jumlah Item Maksimal (max_items)
    favorite_foods: Annotated[List[str], Field(min_items=1, max_items=5)]
    
    # 18. Set (Otomatis unik)
    followers: Set[str] # Memastikan tidak ada follower duplikat

    # 19. Enum (Hanya menerima nilai dari Enum)
    role: UserRole = UserRole.USER
    
    # 20. Model Bersarang (Nested Model)
    address: Address

    # 21. Union (Bisa salah satu dari beberapa tipe)
    legacy_id: Union[str, int] # atau 'str | int'

    # 22. Tipe Data Tanggal
    join_date: date
    
    # 23. Validator Kustom (Custom Validator)
    password: str
    confirm_password: str

    @field_validator('confirm_password')
    @classmethod
    def passwords_match(cls, v: str, info: 'ValidationInfo') -> str:
        # 'info.data' berisi semua data yang sudah divalidasi sejauh ini
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v