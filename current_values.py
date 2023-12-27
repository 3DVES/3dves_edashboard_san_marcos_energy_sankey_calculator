from getting_data import attribute_current_value, attribute_value, search_histories
from getting_dates import first_of_this_month
from units_convertion import MBTU_to_kWh, Therm_to_kWh, hp_to_kWh, natural_gas_to_heat, chiller_to_cooling

# Current Values

natural_gas_usage_kWh = Therm_to_kWh(float(attribute_current_value(106)))
electricity_usage_kWh = float(attribute_current_value(105))
total_energy = natural_gas_usage_kWh + electricity_usage_kWh

natural_gas_consumed_by_boilers = hp_to_kWh(239)+(2*1547)
natural_gas_consumed_by_steam_boilers = hp_to_kWh(5 * 50)
natural_gas_consumed_by_cells = float(attribute_current_value(55)) / 0.52
natural_gas_consumed_by_miscellaneous = (
    natural_gas_usage_kWh
    - natural_gas_consumed_by_boilers
    - natural_gas_consumed_by_steam_boilers
    - natural_gas_consumed_by_cells
)

cells_thermal_losses = 0.48 * natural_gas_consumed_by_cells
natural_gas_heat_losses = natural_gas_to_heat(
    natural_gas_consumed_by_boilers,
    natural_gas_consumed_by_steam_boilers
)
electricity_heat_losses = (
    total_energy
    - natural_gas_consumed_by_miscellaneous
    - natural_gas_heat_losses
    - cells_thermal_losses
)

cooling_plant_efficiency = float(attribute_current_value(194))
cooling_plant_energy = cooling_plant_efficiency * float(attribute_current_value(189))
electricity_usage_hospital = 0.6956 * (electricity_heat_losses - chiller_to_cooling(cooling_plant_energy))
electricity_usage_by_others = 0.3043 * (electricity_heat_losses - chiller_to_cooling(cooling_plant_energy))
heat_used_by_hospital = 0.85 * natural_gas_heat_losses

def get_list_element(Source, Destiny, Value):
    return {"Source": Source, "destiny": Destiny, "value": Value}


ls_current_values = []

ls_current_values.append(
    get_list_element("Billings", "Electricity Grid", round(electricity_usage_kWh, 2))
)

ls_current_values.append(
    get_list_element("Billings", "Natural Gas", round(natural_gas_usage_kWh, 2))
)

ls_current_values.append(
    get_list_element("Natural Gas", "Miscellaneous", round(natural_gas_consumed_by_miscellaneous, 2))
)

ls_current_values.append(
    get_list_element("Natural Gas", "Boilers", round(natural_gas_consumed_by_boilers, 2))
)

ls_current_values.append(
    get_list_element("Natural Gas", "Steam Boilers", round(natural_gas_consumed_by_steam_boilers, 2))
)

ls_current_values.append(
    get_list_element("Natural Gas", "Cells", round(natural_gas_consumed_by_cells, 2))
)

ls_current_values.append(
    get_list_element("Steam Boilers", "Heating", round(0.85 * natural_gas_consumed_by_steam_boilers, 2))
)

ls_current_values.append(
    get_list_element("Boilers", "Heating", round(0.85 * natural_gas_consumed_by_boilers, 2))
)

ls_current_values.append(
    get_list_element("Boilers", "Thermal Losses", round(0.145 * natural_gas_consumed_by_boilers, 2))
)

ls_current_values.append(
    get_list_element("Heating", "Hospital (Heat)",
        round(0.7 * ((natural_gas_consumed_by_boilers + natural_gas_consumed_by_steam_boilers)), 2))
)

ls_current_values.append(
    get_list_element("Heating", "Others (Heat)",
        round(0.1 * ((natural_gas_consumed_by_boilers + natural_gas_consumed_by_steam_boilers)), 2))
)

ls_current_values.append(
    get_list_element("Cells", "Thermal Losses", round(cells_thermal_losses, 2))
)

ls_current_values.append(
    get_list_element("Cells", "Electricity", round(0.52 * natural_gas_consumed_by_cells, 2))
)

ls_current_values.append(
    get_list_element("Electricity Grid", "Electricity", round(electricity_usage_kWh, 2))
)

ls_current_values.append(
    get_list_element("Electricity", "Chillers", round(chiller_to_cooling(cooling_plant_energy), 2))
)

ls_current_values.append(
    get_list_element("Chillers", "Cooling", round(chiller_to_cooling(cooling_plant_energy), 2))
)

ls_current_values.append(
    get_list_element("Electricity", "Hospital Main",
        round(0.6956 * (electricity_usage_kWh + 0.52 * natural_gas_consumed_by_cells - chiller_to_cooling(cooling_plant_energy)), 2))
)

ls_current_values.append(
    get_list_element("Electricity", "Others",
        round(0.3043 * (electricity_usage_kWh + 0.52 * natural_gas_consumed_by_cells - chiller_to_cooling(cooling_plant_energy)), 2))
)

def source_destiny():
    return ls_current_values
