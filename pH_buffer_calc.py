### PH BUFFER CALCULATOR

def get_data():

    while True:
        try:
            target_ph = float(input("Enter target pH: "))
            break
        except ValueError as val_error:
            print(f"{val_error}\nValue must be a NUMBER")
        
    while True:
        try:
            Conjugateacid_name = str(input("Enter conjugate acid name: "))
            Conjugatebase_name = str(input("Enter conjugate base name: "))
            break
        except Exception as excp:
            print(excp)

    while True:
        try:
            A_molarmass = float(input("Enter the conjugated acid molar mass: "))
            HA_molarmass = float(input("Enter the conjugated base molar mass: "))
            break
        except ValueError as val_error:
            print(f"{val_error}\nValue must be a NUMBER")
    
    while True:
        try:
            pKa = float(input("Enter pKa of the acid: "))
            Total_buffer_conc = float(input("Enter the total buffer concentration: "))
            Volume = float(input("Enter the total volume: "))
            break
        except ValueError as val_error:
            print(f"{val_error}\nAll values must be NUMBERS")
                                    
    return target_ph,Conjugateacid_name,Conjugatebase_name,A_molarmass, HA_molarmass, pKa, Total_buffer_conc, Volume

target_ph,Conjugateacid_name,Conjugatebase_name,A_molarmass, HA_molarmass, pKa, Total_buffer_conc, Volume = get_data()

def get_ratio(pKa,target_ph):
    return 10**(target_ph-pKa)

def get_ind_concentration(Total_buffer_conc,conjugate_ratio):
    A_conc = Total_buffer_conc*(conjugate_ratio/(1+conjugate_ratio))
    HA_conc = Total_buffer_conc - A_conc

    return A_conc, HA_conc

def get_moles(A_conc,HA_conc,Volume):
    A_moles = A_conc*Volume
    HA_moles = HA_conc*Volume
    
    return A_moles, HA_moles

def convert_moles_to_mass(A_moles,HA_moles,A_molarmass,HA_molarmass):
    A_mass = A_moles*A_molarmass
    HA_mass = HA_moles*HA_molarmass

    return A_mass, HA_mass

get_ratio(pKa,target_ph)
A_conc = get_ind_concentration(Total_buffer_conc,get_ratio(pKa,target_ph))[0]
HA_conc = get_ind_concentration(Total_buffer_conc,get_ratio(pKa,target_ph))[1]

A_moles = get_moles(A_conc,HA_conc,Volume)[0]
HA_moles = get_moles(A_conc,HA_conc,Volume)[1]

A_mass = convert_moles_to_mass(A_moles,HA_moles,A_molarmass,HA_molarmass)[0]
HA_mass = convert_moles_to_mass(A_moles,HA_moles,A_molarmass,HA_molarmass)[1]

print(f"\n")
print(f"Mass of {Conjugateacid_name} and {Conjugatebase_name} needed to achieve the target pH of {target_ph} is:\n{Conjugateacid_name}: {A_mass:.4f}\n{Conjugatebase_name}: {HA_mass:.4f}")
print(f"Dilute first the {Conjugateacid_name} in a volume of {Volume}, then add the {Conjugatebase_name}\n")
