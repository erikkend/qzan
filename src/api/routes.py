from fastapi import APIRouter
from src.api.schemas import BINRequest
from src.services import external_egov_api, external_gemini_api


router = APIRouter(prefix='/api/egov')
gemini = external_gemini_api.GeminiAPI()

@router.post('/find_by_bin')
async def egov_find_by_bin(data: BINRequest):
    resp = await external_egov_api.get_external_data(data.bin_code)
    return resp

@router.post('/send_message')
async def send_message_to_gemini(message: str):
    resp = await gemini.generate_text(message)
    return resp