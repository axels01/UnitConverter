l = {"m": 1, "km": 1000, 
        "cm": 0.01, "mm": 0.001, 
        "mi": 1609.344, "yd": 0.9144, 
        "ft": 0.3048, "in": 0.0254}

t = {"s": 1, "min": 60, 
        "h": 3600, "d": 86400,
        "week": 604800, "month": 2629746,
        "year": 31556952}

m = {"kg": 1, "g": 0.001, 
        "mg": 0.000001, "t": 1000,
        "lb": 0.453592, "oz": 0.0283495}

te = {"C": 1, "F": 1.8, 
        "K": 273.15}

a = {"m2": 1, "km2": 1000000,
        "cm2": 0.0001, "mm2": 0.000001,
        "ha": 10000, "a": 100,
        "ft2": 0.09290304}

v = {"m3": 1, "km3": 1000000000,
        "cm3": 0.000001, "mm3": 0.000000001,
        "l": 0.001, "ml": 0.000001}

p = {"Pa": 1, "kPa": 1000,
        "MPa": 1000000, "hPa": 100,
        "bar": 100000, "atm": 101325}

s = {"m/s": 1, "km/h": 3.6,
        "km/s": 1000, "m/h": 2.23694,
        "m/min": 0.0166667, "km/min": 0.06,
        "ft/s": 3.28084, "ft/min": 196.85,
        "ft/h": 11811.02, "knot": 1.94384,
        "mach": 340.29, "c": 299792458}

e = {"J": 1, "kJ": 1000, 
        "MJ": 1000000, "GJ": 1000000000,
        "eV": 1.602176634e-19, "Wh": 3600,
        "kWh": 3600000, "MWh": 3600000000,
        "GWh": 3600000000000, "cal": 4.184,
        "kcal": 4184, "BTU": 1055.05585}

quantites = {"l": l, "t": t, "m": m, 
            "te": te, "a": a, "v": v, 
            "p": p, "s": s, "e": e}

names = {"l": "Length     ", "t": "Time       ",
        "m": "Mass       ", "te": "Temperature",
        "a": "Area       ", "v": "Volume     ",
        "p": "Pressure   ", "s": "Speed      ",
        "e": "Energy     "}

def main():
    print("Welcome to the unit converter!", "\n")
    for name in names:
        print(names[name], ":", name)
        originQuanitity = input("Please enter quantity to convert from: ")
    


    destinationUnit = input("Please enter unit to convert to: ")
    value = float(input("Please enter value to convert: "))



if __name__ == "__main__":
    main()