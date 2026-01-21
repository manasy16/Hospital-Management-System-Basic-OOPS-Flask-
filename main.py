from services.hospital_service import HospitalServices

hospital = HospitalServices()


#hospital.add_patient(11, "Manas", 21, "Male", "9999999999", "Fever")
#hospital.add_doctor(1001, "Sharma", "Cardiologist", "8888888888")

#hospital.book_appointment(10001, 1, 1001, "2025-01-12", "11:00 AM")

bill = hospital.generate_bill(51, 10001, 500, 300)
print(bill)

