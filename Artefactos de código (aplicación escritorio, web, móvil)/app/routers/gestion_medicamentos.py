from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.Medications_service import Medications_service
from config.db import Session

db = Session()

gestion_medicamentos = APIRouter()
template = Jinja2Templates(directory="frontend")


@gestion_medicamentos.get("/all_list/medicamentos", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/listaMedicamentos.html", {"request": request})


@gestion_medicamentos.get("/gestion/medicamentos", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/Gestion_medicamentos.html", {"request": request})


@gestion_medicamentos.get("/gestion/medicamentos_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/EliminarMedicamento.html", {"request": request})


@gestion_medicamentos.delete("/gestion/user_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
async def delete_user(request: Request, name_medication: str = Form(...),  token: str = Depends(JWTBearer())):
    Medications_service(db).delete_medications(generic_name=name_medication)

    return template.TemplateResponse(
        "templates/paginaPrincipalAdministrador.html",
        {"request": request, "token": token}
    )
