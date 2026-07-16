from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from frontend.services.pegasus_service import PegasusService

router = APIRouter()

templates = Jinja2Templates(
    directory="frontend/templates"
)

pegasus = PegasusService()


# ==========================================================
# MODELO DE LA PETICIÓN
# ==========================================================

class PreguntaRequest(BaseModel):

    pregunta: str


# ==========================================================
# PÁGINA PRINCIPAL
# ==========================================================

@router.get("/index")
async def index(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ==========================================================
# API DEL AGENTE
# ==========================================================

@router.post("/preguntar")
async def preguntar(data: PreguntaRequest):

    respuesta = pegasus.preguntar(data.pregunta)

    return JSONResponse(
        content={
            "respuesta": respuesta
        }
    )