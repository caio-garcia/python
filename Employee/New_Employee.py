class new_employee:
    def __init__(self, first_name,surname):
        self.first_name = first_name
        self.surname = surname
        self.full_name  = first_name + " " + surname
        self.email  = first_name.lower()+"."+surname.lower()+"@and.digital"