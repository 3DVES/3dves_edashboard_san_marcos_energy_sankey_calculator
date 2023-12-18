def hp_to_BTU_h(hp):
    return hp*2544.43

def MBTU_to_kWh(MBTU):
    return MBTU*0.293071

def Therm_to_kWh(Therm):
    return Therm/0.0341296

def MMBTU_to_kWh(MMBTU):
    return 293.071*MMBTU

def NaturalGasB_SB(hp):
    return hp_to_BTU_h(hp)*0.00072*293.07

def NaturalGas_Heat(NGBC,NGSBC):
    #NGBC Natural Gas Boiler Consumption kWh
    #NGSBC Natural Gas Steam Boiler Consumption  kWh
    return NGBC + NGSBC

def Chiller_Cooling(CE):
    #CE Cooling Efficiency kW
    return CE*576
