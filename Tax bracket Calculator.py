#Tax Bracket Calculator

def tax_bracket_calculator(monthly_gross_salary):
    gross = monthly_gross_salary*12
    taxed_amount = 0
    
    if gross > 1 and gross <= 237100:
        x = gross * 0.18
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{monthly_gross_salary - taxed_amount:.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket R{1:.2f} - R{237100/12:.2f}")
    
    elif gross > 237100 and gross <= 370500:
        x = (gross * 0.26) - 42678
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{(monthly_gross_salary - taxed_amount):.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket R{237101/12:.2f} - R{370500/12:.2f}")
    
    elif gross > 370500 and gross <= 512800:
        x = (gross * 0.31) - 77362
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{(monthly_gross_salary - taxed_amount):.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket R{370501/12:.2f} - R{512800/12:.2f}")
    
    elif gross > 512800 and gross <= 673000:
        x = (gross * 0.36) - 121475
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{(monthly_gross_salary - taxed_amount):.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket R{512801:.2f} - R{673000/12:.2f}")
    
    elif gross > 673000 and gross <= 857000:
        x = (gross * 0.39) - 179147
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{(monthly_gross_salary - taxed_amount):.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket R{673001/12:.2f} - R{857000/12:.2f}")
    
    elif gross > 857000 and gross <= 1817000:
        x = (gross * 0.41) - 251258
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{(monthly_gross_salary - taxed_amount):.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket R{857001:.2f} - R{1817000/12:.2f}")
    
    else:
        x = (gross * 0.45) - 644489
        taxed_amount = x/12
        print(f"Your monthly taxed amount is R{taxed_amount:.2f} from R{monthly_gross_salary:.2f} \nYour Actual Monthly Salary is R{(monthly_gross_salary - taxed_amount):.2f}")
        print("\n_______________________________________________________________\n")
        print(f"Your tax bracket > R{1817001:.2f}")
    
        
monthly_gross_salary = float(input("Enter your monthly earning(before deductions) in ZAR: "))
tax_bracket_calculator(monthly_gross_salary)