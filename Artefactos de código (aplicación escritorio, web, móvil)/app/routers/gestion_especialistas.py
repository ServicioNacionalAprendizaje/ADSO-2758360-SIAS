from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.Specialist_service import specialist_service
from config.db import Session

db = Session()

gestion_especialistas = APIRouter()
template = Jinja2Templates(directory="frontend")


@gestion_especialistas.get("/all_list/especialistas", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/ListaEspecialista.html", {"request": request})


@gestion_especialistas.get("/gestion/especialistas", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/Gestionespecialistas.html", {"request": request})


@gestion_especialistas.get("/gestion/especialistas_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/EliminiarSpecialista.html", {"request": request})


@gestion_especialistas.delete("/gestion/especialista_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
async def delete_user(request: Request, document_number: str = Form(...),  token: str = Depends(JWTBearer())):
    result = specialist_service(db).delete_specialist(document_number)

    return template.TemplateResponse(
        "templates/paginaPrincipalAdministrador.html",
        {"request": request, "token": token}
    )
