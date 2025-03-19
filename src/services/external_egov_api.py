import os
import json
import urllib.parse

import httpx
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EGOV_API_KEY")

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
#
async def get_external_data(bin_code):
    try:
        async with httpx.AsyncClient() as client:
            query = {
                "size": 100,
                "query": {
                    "bool": {
                        "must": [
                            {"match": {"bin": bin_code}}
                        ]
                    }
                }
            }
            encoded_query = urllib.parse.quote(json.dumps(query))
            url = f"https://data.egov.kz/api/v4/gbd_ul/v1?source={encoded_query}&apiKey={api_key}"
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))