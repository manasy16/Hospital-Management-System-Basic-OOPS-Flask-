class Patient:
    def __init__(self,patient_id,name,age,gender,contact,disease):
        self.patient_id = patient_id
        self.name=name
        self.age = age
        self.gender = gender
        self.contact=contact
        self.disease=disease

    def get_details(self):
        return {
            "Pateint ID":self.patient_id,
            "Name":self.name,
            "Age":self.age,
            "Gender":self.gender,
            "Contact":self.contact,
            "Disease":self.disease


        }
    def __str__(self):
        return f"Patient{self.patient_id} {self.name},Age:{self.age},Disease:{self.disease}"