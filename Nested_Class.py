class Company:
    class Employee:
        def __init__(self,company_name,):
            self.company_name=company_name
            self.employees=[]
        def get_details(self):
            return f"{self.name}:{self.position}"
     
   
    def add_employee(self,name,position):
        new_employee=self.Employee(name,position)
        self.employees.append(new_employee)
    

     
    def list_employees(self):
        pass
company=Company("Wonka")
company.add_employee("david","manager")
company.add_employee("vishnu","GM")

    
