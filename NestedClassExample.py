class Company:
    class Employee:
        def __init__(this,name,position):
            this.name=name
            this.position=position
        def get_details(this):
            return f"{this.name} : {this.position}"
        
    def __init__(this,company_name):
        this.company_name=company_name
        this.employees=[]
    def add_Employee(this,name, position):
        new_Employee=this.Employee(name,position)
        this.employees.append(new_Employee)

    def list_Employee(this):
        return [employee for employee in this.employees]
    
company=Company("Wonka")
print(company.company_name)

company.add_Employee("vishnu","CEO")
company.add_Employee("Megan fox","CEO's wife")
company.add_Employee("Scarlett Johansson","CEO's side bitch")
for i in company.list_Employee():
    print(i.get_details())