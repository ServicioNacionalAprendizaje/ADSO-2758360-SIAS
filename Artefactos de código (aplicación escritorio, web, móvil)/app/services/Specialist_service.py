from schemas.Specialist_schemas import Specialist_schema, Specialist_update, specialistr_filter_schema
from models.Specialist import Specialist_model


class specialist_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_specialist(self):
        """
        esta funcion trear todos los  registro de la base de datos de  especialista,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Specialist_model).all()
        return result

    def get_specialist_frist(self):
        """
        esta funcion trear todos los  registro de la base de datos de  especialista,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Specialist_model).first()
        return result

    def get_specialist_filter(self, valor: specialistr_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.id != None:
            result = self.db.query(Specialist_model).filter(
                Specialist_model.id == valor.id).all()
            return result
        elif valor.fullname != None:
            result = self.db.query(Specialist_model).filter(
                Specialist_model.fullname == valor.fullname)
            return result
        elif valor.number_document != None:
            result = self.db.query(Specialist_model).filter(
                Specialist_model.number_document == valor.number_document).all()
            return result
        elif valor.email != None:
            result = self.db.query(Specialist_model).filter(
                Specialist_model.email == valor.email).all()
            return result
        elif valor.phone_number != None:
            result = self.db.query(Specialist_model).filter(
                Specialist_model.phone_number == valor.phone_number)
            return result
        elif valor.specialty != None:
            result = self.db.query(Specialist_model).filter(
                Specialist_model.specialty == valor.specialty).first()
            return result

    def get_filter_specillist(self, speciality: str):
        result = self.db.query(Specialist_model).filter(
            Specialist_model.specialty == speciality).first()
        return result

    def create_specialist(self, specialist: Specialist_schema):
        """
        esta funcion crea un registro de tipo espicialista utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_specialist = Specialist_model(**specialist.dict())
        self.db.add(new_specialist)
        self.db.commit()
        return

    def update_specialist(self, document_number: int, data: Specialist_update):
        """
        esta funcion actualiza un registro de tipo especialista utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        Specialist = self.db.query(Specialist_model).filter(
            Specialist_model.number_document == document_number).first()
        Specialist.email = data.email
        Specialist.phone_number = data.phone_number
        Specialist.specialty = data.specialty
        self.db.commit()
        return

    def delete_specialist(self, document_number: int):
        """
        esta funcion eliminar un registro de tipo medications,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Specialist_model).filter(
            Specialist_model.document_number == document_number).delete()
        self.db.commit()
        return

    def verif_name(self, fullname: str):
        self.db.query(Specialist_model).filter(
            Specialist_model.fullname == fullname).all()
        self.db.commit()
        return
