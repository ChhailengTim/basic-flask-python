def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of year: "))


    monhtly_interest_rate = apr/12000
    amount_of_months = years * 12
    monthly_payment = principal * monhtly_interest_rate / (1 - (1+ monhtly_interest_rate)**(-amount_of_months))


    print("The monthly payment for this loan is: " + "{:.2f}%".format(monthly_payment))

main()