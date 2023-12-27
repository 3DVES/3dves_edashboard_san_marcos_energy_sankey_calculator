def hp_to_BTU_h(hp):
    return hp*2544.43

def MBTU_to_kWh(MBTU):
    return MBTU*(1000000/3412.14)

def Therm_to_kWh(Therm):
    return Therm/0.0341296

def MMBTU_to_kWh(MMBTU):
    return 293.071*MMBTU

def hp_to_kWh(hp):
    return hp_to_BTU_h(hp)*0.00072*293.07

def natural_gas_to_heat(NGBC,NGSBC):
    #NGBC Natural Gas Boiler Consumption kWh
    #NGSBC Natural Gas Steam Boiler Consumption  kWh
    #TC Trigen Consumption kWh
    return NGBC + NGSBC

def chiller_to_cooling(CE):
    #CE Cooling Efficiency kW
    return CE*576

def absorption_chiller_to_cooling(CE):
    #CE Cooling Efficiency kW
    return CE*144
