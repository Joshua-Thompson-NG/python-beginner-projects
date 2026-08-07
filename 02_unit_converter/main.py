# --- UNIT CONVERTER ---

# Converts temperature from Celsius to Fahrenheit and vice versa


# temperature convertor
def celsius_to_fahrenheit(cels):
    return (cels * 9/5) + 32
def fahrenheit_to_celsius(fare):
    return (fare - 32) * 5/9

def main():
    while True:
        print('---- TEMPERATURE CONVERTOR ----')
        print('1. Convert Celsius and Fahrenheit')
        print('2. Quit')
        print()

        try:
            user_input = int(input('Enter your choice: '))


            if user_input < 1 or user_input > 2:
                print("Enter a number between 1 and 2")
                continue

            if user_input == 1:
                print("1. Celsius to Fahrenheit: ")
                print("2. Fahrenheit to Celsius: ")


                ask_user = int(input('Enter your choice: '))


                if ask_user < 1 or ask_user > 2:
                    print("Enter a number between 1 and 2")
                    continue



                if ask_user == 1:
                    cels = float(input('Enter temperature in Celsius: '))
                    result = celsius_to_fahrenheit(cels)
                    print(f"{cels} in Fahrenheit is {result}F")

                else:
                    fare = float(input('Enter temperature in Fahrenheit: '))
                    result = fahrenheit_to_celsius(fare)
                    print(f"{fare} in Celsius is {result}C")

            else:
                break
        except Exception as e:
            print('Enter a valid number')
            print()




if __name__ == "__main__":
    main()


