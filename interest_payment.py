def main():
    print("This is a monthly loan payment calculator")
    print('')

    principal = float(input("Input the loan amount:"))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interst_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interst_rate / (1 - (1 + monthly_interst_rate) ** (-amount_of_months))

    print("the monthly payment for this loan is: %.2f" %monthly_payment)

main()