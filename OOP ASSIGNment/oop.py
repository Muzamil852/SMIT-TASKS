class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def calculate_salary(self):
        pass

    def get_info(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, bonus):
        super().__init__(id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

    def get_info(self):
        return (
            f"Full-Time Employee | ID: {self.id} | "
            f"Name: {self.name} | Salary: {self.calculate_salary()}"
        )


class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours_worked):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_info(self):
        return (
            f"Part-Time Employee | ID: {self.id} | "
            f"Name: {self.name} | Salary: {self.calculate_salary()}"
        )


class Contractor(Employee):
    def __init__(self, id, name, daily_rate, days_worked):
        super().__init__(id, name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        return self.daily_rate * self.days_worked

    def get_info(self):
        return (
            f"Contractor | ID: {self.id} | "
            f"Name: {self.name} | Salary: {self.calculate_salary()}"
        )


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_payroll(self):
        print("\n========== PAYROLL DETAILS ==========")

        for employee in self.employees:
            print(employee.get_info())

        print("=====================================")


payroll = Payroll()

emp1 = FullTimeEmployee("E01", "Ali", 50000, 10000)
emp2 = PartTimeEmployee("E02", "Ahmed", 500, 40)
emp3 = Contractor("E03", "Sara", 3000, 20)

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

payroll.display_payroll()
