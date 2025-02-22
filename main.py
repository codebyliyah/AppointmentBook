from appointments import AppointmentBook, MedicalAppointment, BusinessMeeting

if __name__ == "__main__":
    book = AppointmentBook()
    appt1 = MedicalAppointment("Dentist Visit", "2025-02-10", "10:00 AM", "Dr. Smith", "Dental Clinic")
    appt2 = BusinessMeeting("Project Review", "2025-02-11", "2:00 PM", ["Alice", "Bob"], "Conference Room")

    book.add_appointment(appt1)
    book.add_appointment(appt2)

    print("Appointments:")
    book.show_appointments()

    appt1.reschedule("2025-02-12", "11:00 AM")
    print("Updated Appointments:")
    book.show_appointments()
