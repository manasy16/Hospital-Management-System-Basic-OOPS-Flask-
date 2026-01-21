class Billing:
    def __init__(self,bill_id,appointment,consultation_fee,medicine_cost):
        self.bill_id = bill_id
        self.appointment = appointment
        self.consulation_fee = consultation_fee
        self.medication_fee = medicine_cost
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        return self.consulation_fee + self.medication_fee
    def get_details(self):
        return {
            "Bill ID": self.bill_id,
            "Patient": self.appointment.patient.name,
            "Doctor":self.appointment.doctor.name,
            "Total Amount": self.total_amount
        }
    
    def __str__(self):
        return (
            f"Bill[{self.bill_id}] | "
            f"Patient: {self.appointment.patient.name} | "
            f"Doctor: Dr. {self.appointment.doctor.name} | "
            f"Amount: ₹{self.total_amount}"
        )
