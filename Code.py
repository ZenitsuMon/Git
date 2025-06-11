def main():
    print("This is a currency converter")
    amount_of_dollars = eval(input("How much dollar do you want to convert? "))
    pounds = convert_to_pounds(amount_of_dollars)
    print(pounds)

convert_to_pounds = lambda amount_of_dollars: amount_of_dollars*0.82
main()
