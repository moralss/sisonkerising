class Employee:
    
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname   
               
    def set_first_name(fname,self):
        self.first_name = fname   

    def get_first_name(self):
        return(fname)

    def set_last_name(lname,self):
        self.last_name = lname
        
    def get_last_name(self):
        return(lname)

####    


class SalaryCalculator:
    def __init__(self,msalary):
        self.monthly_salary = msalary
        if (msalary < 0.0):
            monthly_salary = 0.0


    def set_monthly_salary(self,msalary):
        monthly_salary = msalary

    def get_monthly_salary(self):
        return(monthly_salary)

    
    def get_yearly_salary(self):
        yearly_salary = monthly_salary *12
        return(yearly_salary)
    

        
    def get_raise_salary(self):
        salary_increase = montly_salary * 0.1
        salary_raise = (monthly_salary + salary_increase) * 12
        return(salary_raise)
                






    

    
            
