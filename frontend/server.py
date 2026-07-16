from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from frontend.api.routes import router

# ==========================================================
# APLICACIÓN FASTAPI
# ==========================================================

app = FastAPI(
    title="Pegasus Agente Empresarial",
    version="1.0.0"
)

# ==========================================================
# ROUTERS
# ==========================================================

app.include_router(router)

# ==========================================================
# ARCHIVOS ESTÁTICOS
# ==========================================================

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)

# ==========================================================
# REDIRECCIÓN A LA PÁGINA PRINCIPAL
# ==========================================================

@app.get("/", include_in_schema=False)
async def home():

    return RedirectResponse(url="/index")