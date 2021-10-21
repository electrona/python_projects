import input_output


def main():
    total_before_tax = 0
    response = "y"

    input_output.header()

    while response == "y":

        input_output.menu_header()

        while True:
            item_cost = float(input("Cost of items: "))

            if item_cost == 0:
                input_output.totals(total_before_tax)
                response = str(input("Again? (y/n): "))
                break

            else:
                total_before_tax = total_before_tax + item_cost
                item_cost = 0

    else:
        input_output.exit_greeting()


if __name__ == "__main__":
    main()
