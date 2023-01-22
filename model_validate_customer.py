import re
from typing import Optional


class ModelValidateCustomer:
    def __init__(self):
        self.expressions_phone = {"pt_BR": r"^55[0-9]{10}$|^55[0-9]{11}$|^[0-9]{11}$|^[0-9]{10}$",
                                  "en_US": r"^11[0-9]{10}$|^[0-9]{10}$|^1[0-9]{3}[0-9]{3}[0-9]{4}$",
                                  "fr_FR": r"^33[0-9]{9}$|^0[1-9][0-9]{8}$"}
        self.expression_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+$"
        self.expressions_document = {"CPF": r"^[0-9]{11}$",
                                     "CNPJ": r"^[0-9]{14}$"}
        
    
        
    def valid_phone(self, phone: Optional[str], country: str) -> Optional[str]:
        """
        Validate if the passed phone number is valid based on the country
        :param phone: phone number to be validated
        :return: phone number if valid, None otherwise
        """
        if (phone is None) or (phone == ''):
            self.check_valid_phone = False
            return phone
        
        phone = re.sub(r'\D', '', str(phone))
        for key_country, expression in self.expressions_phone.items():
            if (key_country == country) and (re.search(expression, phone)):
                self.check_valid_phone = True
                return phone
            
        self.check_valid_phone = False
        return phone
    
        
    def valid_email(self, email: str) -> str:
        """
        Validate if the passed email is valid
        :param email: email to be validated
        :return: email if valid, None otherwise
        """
        if (email is None) or (email == ''):
            self.check_valid_email = False
            return email
        
        if re.search(self.expression_email, email):
            self.check_valid_email = True
            return email
        self.check_valid_email = False
        return email
        
        
    def valid_document(self, document: Optional[str]):
        """
        Validate if the passed document is valid
        :param document: document to be validated
        :return: document if valid, None otherwise
        """
        if (document is None) or (document == ''):
            self.check_valid_document = False
            return document
        
        document = re.sub(r'\D', '', str(document))
        if len(document) > 11:
            document = document.zfill(14)
        elif len(document) in [5, 6]:
            document = document.zfill(11)
        
        for type_document, expression in self.expressions_document.items():
            if re.search(expression, document):
                self.check_valid_document = True
                self.type_document = type_document
                return document
            
        self.check_valid_document = False
        self.type_document = None
        return document