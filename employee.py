"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commissionPer, commissionContracts):
        self.name = name
        self.commissionContracts = commissionContracts
        self.commissionPer = commissionPer

    def get_commission_str(self):
        if (self.commissionPer > 0):
            if (self.commissionContracts == 1):
                return f" and receives a bonus commission of {self.commissionPer}"
            else:
                return f" and receives a commission for {self.commissionContracts} contract(s) at {self.commissionPer}/contract"
        else:
            return ""
    
    def get_commission(self):
        if (self.commissionPer > 0):
            return self.commissionContracts * self.commissionPer
        else:
            return 0

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, perMonth, commissionPer=0, commissionContracts=1):
        super().__init__(name, commissionPer, commissionContracts)
        self.perMonth = perMonth

    def get_pay(self):
        salary = self.perMonth
        addCommission = super().get_commission()

        return salary + addCommission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.perMonth}{super().get_commission_str()}. Their total pay is {self.get_pay()}."
        
class HourlyEmployee(Employee):
    def __init__(self, name, hours, perHour, commissionPer=0, commissionContracts=1):
        super().__init__(name, commissionPer, commissionContracts)
        self.hours = hours
        self.perHour = perHour
    
    def get_pay(self):
        salary = self.hours * self.perHour
        addCommission = super().get_commission()

        return salary + addCommission

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.perHour}/hour{super().get_commission_str()}. Their total pay is {self.get_pay()}."
         

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, 600)
