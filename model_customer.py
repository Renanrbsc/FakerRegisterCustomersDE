from model_validate_customer import ModelValidateCustomer
from faker import Faker
from typing import Tuple, List
import random
import string

class ModelCustomer:
    def __init__(self, name, lastname, email, document, age, height, weight, country, phone:str):
        self.model_validate_customer = ModelValidateCustomer()
        self.name = name
        self.lastname = lastname
        self.email = self.model_validate_customer.valid_email(email)
        self.document = self.model_validate_customer.valid_document(document)
        self.age = age
        self.height = height
        self.weight = weight
        self.country = country
        self.phone = self.model_validate_customer.valid_phone(phone, country)

        
        
    @staticmethod    
    def generate_personal_info(n: int) -> List[Tuple[str, int, str]]:
        """
        This function generates random personal information using the Faker library.
        It includes name, last name, email, phone, document, age, height, and weight.
        The information is returned as a tuple.
        """
        countries = ["pt_BR", "en_US", "fr_FR"]
        personal_info_list = list()
        for _ in range(n):
            country = random.choice(countries)
            fake = Faker(country)
            if country == "pt_BR":
                document = random.choices(["CPF", "CNPJ"], weights=[0.5,0.5])[0]
                if document == "CPF":
                    document = fake.cpf()
                else:
                    document = fake.cnpj()
            elif country == "en_US":
                document = fake.ssn()
            elif country == "fr_FR":
                document = fake.random_int(min=100000000, max=999999999)
            personal_info_list.append((fake.first_name(), 
                                       fake.last_name(), 
                                       fake.email(), 
                                       fake.phone_number(), 
                                       document,
                                       fake.random_int(min=18, max=70), #Age
                                       fake.random_int(min=140, max=220), #Height
                                       fake.random_int(min=40, max=150), #Weight
                                       country))
        return personal_info_list


    def get_data(self):
        customer_data = {'name': self.name,
                         'lastname': self.lastname,
                         'email': self.email,
                         'check_valid_email': self.model_validate_customer.check_valid_email,
                         'phone': self.phone,
                         'check_valid_phone': self.model_validate_customer.check_valid_phone,
                         'document': self.document,
                         'type_document': self.model_validate_customer.type_document,
                         'check_valid_document': self.model_validate_customer.check_valid_document,
                         'age': self.age,
                         'height': self.height,
                         'weight': self.weight,
                         'country': self.country}
        return customer_data
    
    
    @classmethod
    def load_customers(cls, customers_df):
        customers_list = []
        for row in customers_df.collect():
            customer = cls(row["name"], row["lastname"], row["email"], 
                           row["document"], row["age"], row["height"], 
                           row["weight"], row["country"], row["phone"])
            customers_list.append(customer.get_data())
        return customers_list