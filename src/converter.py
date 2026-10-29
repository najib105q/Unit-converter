while True:
    print("\n=== UNIT CONVERTER ===")
    print("1. Fahrenheit -> Celsius")
    print("2. Celsius -> Fahrenheit")
    print("3. Miles -> Kilometers")
    print("4. Kilometers -> Miles")
    print("5. Pounds -> Kilograms")
    print("6. Kilograms -> Pounds")
    print("7. Gallons -> Liters")
    print("8. Liters -> Gallons")
    print("9. Feet -> Meters")
    print("10. Meters -> Feet")
    print("11. Inches -> Centimeters")
    print("12. Centimeters -> Inches")
    print("13. Ounces -> Grams")
    print("14. Grams -> Ounces")
    print("15. Hours -> Minutes")
    print("16. Minutes -> Hours")
    print("17. Minutes -> Seconds")
    print("18. Seconds -> Minutes")
    print("19. TB -> GB")
    print("20. GB -> TB")
    print("21. GB -> MB")
    print("22. MB -> GB")
    print("23. MB -> KB")
    print("24. KB -> MB")
    print("25. KB -> Bytes")
    print("26. Bytes -> KB")
    print("27. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        value = float(input("Fahrenheit: "))
        print(f"{value:.2f} °F = {(value - 32) * 5 / 9:.2f} °C")

    elif choice == "2":
        value = float(input("Celsius: "))
        print(f"{value:.2f} °C = {value * 9 / 5 + 32:.2f} °F")

    elif choice == "3":
        value = float(input("Miles: "))
        print(f"{value:.2f} mi = {value * 1.60934:.2f} km")

    elif choice == "4":
        value = float(input("Kilometers: "))
        print(f"{value:.2f} km = {value / 1.60934:.2f} mi")

    elif choice == "5":
        value = float(input("Pounds: "))
        print(f"{value:.2f} lb = {value / 2.20462:.2f} kg")

    elif choice == "6":
        value = float(input("Kilograms: "))
        print(f"{value:.2f} kg = {value * 2.20462:.2f} lb")

    elif choice == "7":
        value = float(input("Gallons: "))
        print(f"{value:.2f} gal = {value * 3.78541:.2f} L")

    elif choice == "8":
        value = float(input("Liters: "))
        print(f"{value:.2f} L = {value / 3.78541:.2f} gal")

    elif choice == "9":
        value = float(input("Feet: "))
        print(f"{value:.2f} ft = {value * 0.3048:.2f} m")

    elif choice == "10":
        value = float(input("Meters: "))
        print(f"{value:.2f} m = {value / 0.3048:.2f} ft")

    elif choice == "11":
        value = float(input("Inches: "))
        print(f"{value:.2f} in = {value * 2.54:.2f} cm")

    elif choice == "12":
        value = float(input("Centimeters: "))
        print(f"{value:.2f} cm = {value / 2.54:.2f} in")

    elif choice == "13":
        value = float(input("Ounces: "))
        print(f"{value:.2f} oz = {value * 28.3495:.2f} g")

    elif choice == "14":
        value = float(input("Grams: "))
        print(f"{value:.2f} g = {value / 28.3495:.2f} oz")

    elif choice == "15":
        value = float(input("Hours: "))
        print(f"{value:.2f} h = {value * 60:.2f} min")

    elif choice == "16":
        value = float(input("Minutes: "))
        print(f"{value:.2f} min = {value / 60:.2f} h")
        
    elif choice == "17":
        value = float(input("Minutes: "))
        print(f"{value:.2f} min = {value * 60:.2f} sec")
        
    elif choice == "18":
        value = float(input("Seconds: "))
        print(f"{value:.2f} sec = {value / 60:.2f} min")    
        
    elif choice == "19":
        value = float(input("TB: "))
        print(f"{value:.2f} TB = {value * 1024:.2f} GB")
        
    elif choice == "20":
        value = float(input("GB: "))
        print(f"{value:.2f} GB = {value / 1024:.2f} TB")

    elif choice == "21":
        value = float(input("GB: "))
        print(f"{value:.2f} GB = {value * 1024:.2f} MB")

    elif choice == "22":
        value = float(input("MB: "))
        print(f"{value:.2f} MB = {value / 1024:.2f} GB")

    elif choice == "23":
        value = float(input("MB: "))
        print(f"{value:.2f} MB = {value * 1024:.2f} KB")

    elif choice == "24":
        value = float(input("KB: "))
        print(f"{value:.2f} KB = {value / 1024:.2f} MB")

    elif choice == "25":
        value = float(input("KB: "))
        print(f"{value:.2f} KB = {value * 1024:.2f} Bytes")

    elif choice == "26":
        value = float(input("Bytes: "))
        print(f"{value:.2f} Bytes = {value / 1024:.2f} KB")

    elif choice == "27":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")