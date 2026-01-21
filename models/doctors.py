class Doctor:
    def __init__(self,doctor_id,name,specialization,contact):
        self.doctor_id=doctor_id
        self.name =name
        self.specialization=specialization
        self.contact=contact

    def get_details(self):
        return{
            "Doctor_ID":self.doctor_id,
            "Name":self.name,
            "Specialization":self.specialization,
            "Contact":self.contact

        }
        
        def __str__(self):
            return f"Doctor [{self.doctor_id}] Dr. {self.name} ({self.specialization})"