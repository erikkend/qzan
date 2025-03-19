from pydantic import BaseModel, field_validator


class BINRequest(BaseModel):
    bin_code: str

    @field_validator("bin_code")
    @classmethod
    def validate_bin(cls, value):
        if not value.isdigit():
            raise ValueError("БИН должен содержать только цифры.")
        if len(value) != 12:
            raise ValueError("БИН должен состоять из 12 цифр.")
        return value