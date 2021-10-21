import salestax

def header():
    print("Sales Tax Calculator")
    print()

def totals(total_before_tax):
    print()
    print(f"Total: {round(total_before_tax,2)}")
    print(f"Sales tax: {round(salestax.sales_tax(total_before_tax),2)}")
    print(f"Total after tax: {round(salestax.total_after_tax(total_before_tax),2)}")
    print()

def menu_header():
    print("ENTER ITEMS (ENTER 0 TO END)")
    print()

def exit_greeting():
    print("Thanks, bye!")