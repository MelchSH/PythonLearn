### data

target_ph = 5.0
pKa = 4.76
Total_buffer_conc = 0.1 #M
Volume = 1 #L
Conjugateacid_name = "Acetic acid (CH3COOH)"
Conjugatebase_name = "Sodium acetate (CH3COONa)"
A_molarmass = 60.05 # Acetic acid (CH3COOH) g/mol
HA_molarmass = 82.03 # Sodium Acetate (CH3COONa) g/mol



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

print(f"Mass of {Conjugateacid_name} and {Conjugatebase_name} needed to achieve the target pH of {target_ph} is:\n{Conjugateacid_name}: {A_mass}\n{Conjugatebase_name}: {HA_mass}")
print(f"Dilute first the {Conjugateacid_name} in a volume of {Volume}, then add the {Conjugatebase_name}\n")
