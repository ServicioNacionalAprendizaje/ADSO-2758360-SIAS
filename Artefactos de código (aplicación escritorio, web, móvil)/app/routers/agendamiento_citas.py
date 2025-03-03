from fastapi import APIRouter, Request, Depends, Form
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.medical_appointments_services import appoinments_service
from schemas.Medical_appointment_schema import medical_appointments_schema
from services.affiliate_services import Affiliate_service
from services.Specialist_service import specialist_service
from services.hospital_service import hospìtal_service
from fastapi.templating import Jinja2Templates
from typing import Optional
from config.db import Session
from datetime import datetime, timedelta


db = Session()
templates = Jinja2Templates(directory="frontend")

agendamiento_citas_router = APIRouter()


@agendamiento_citas_router.get("/agendamiento_citas", tags=["agendamiento_citas"])
def agendamiento_citas(request: Request):

    return templates.TemplateResponse("templates/agendamientoCitas.html", {"request": request})


@agendamiento_citas_router.post("/create/citas", tags=["agendamiento_citas"], dependencies=[Depends(JWTBearer())])
async def get_update_pg(
    request: Request,
    especialidad: str = Form(...),
    fecha: str = Form(...),
    departamento: str = Form(...),
    ciudad: str = Form(...),
    citas_cercanas: Optional[bool] = Form(False),
    token: str = Depends(JWTBearer())
):
    doctor = specialist_service(db).get_specialist_frist()
    hospital = hospìtal_service(db).get_hospital_first()
    email = token["email"]
    afiliate = Affiliate_service(db).validate_affilate_email(email=email)
    template = medical_appointments_schema(
        appointment_type=especialidad,
        fullname_affiliate=afiliate.fullname,
        document_number_affiliate=afiliate.document_number,
        name_doctor=doctor.fullname,
        created_by=token["email"],
        day=fecha,
        hospital_name=hospital.name_hospital,
        hour=(datetime.now() + timedelta(hours=2)).time(),
        Clinical_history=afiliate.Clinical_history)

    result = appoinments_service(db).create_appoinments(template)
    return templates.TemplateResponse("templates/ordenCitasConfirmacion.html", {
        "request": request,
        "dia": fecha,  # La fecha de la cita
        "nombre_completo": afiliate.fullname,  # Nombre completo del afiliado
        "especialidad": especialidad,  # Especialidad médica
        "direccion": hospital.city,  # Dirección del hospital
        "email": afiliate.email,  # Email del afiliado
        "ciudad": hospital.city,  # Ciudad del hospital
        # Hora de la cita
        "hora": (datetime.now() + timedelta(hours=2)).strftime("%H:%M:%S")
    })
