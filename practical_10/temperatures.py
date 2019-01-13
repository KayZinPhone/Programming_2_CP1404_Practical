from flask import Flask

app = Flask(__name__)


# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()

@app.route("/F/<c>")
def celsius_to_fahrenheit(c=0):
    fahrenheit = c * 9.0 / 5 + 32
    return "Result: {:.2f} F".format(fahrenheit)

@app.route("/C/<f>")
def fahrenheit_to_celsius(f=0):
    celsius = (f - 32) * 5 / 9
    return "Result {:.2f} C".format(celsius)


# def main():
#     global celsius, fahrenheit, choice
#     while choice != "Q":
#         if choice == "C":
#             celsius = float(input("Celsius: "))
#             celsius_to_fahrenheit(celsius)
#         elif choice == "F":
#             fahrenheit = float(input("Fahrenheit: "))
#             fahrenheit_to_celsius(fahrenheit)
#         else:
#             print("Invalid option")
#         print(MENU)
#         choice = input(">>>").upper()
#     print("Thank you.")
#
# main()

if __name__ == '__main__':
    app.run()



