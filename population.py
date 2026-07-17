import pandas as pd
def create_population_df(dict_data: dict) -> pd.DataFrame:
    data = [
        {"province": province, "population": values["population"], "population_density": values["population_density"]}
        for province, values in dict_data.items()
    ]
    # Tạo DataFrame
    df = pd.DataFrame(data)
    # Lưu thành file CSV
    df.to_csv('population.csv', index=False)
    return df

if __name__ == '__main__':
    population_dict = {
    'Hà Nội': {'population': 8435650, 'population_density': 2511},
    'Vĩnh Phúc': {'population': 1197620, 'population_density': 969},
    'Bắc Ninh': {'population': 1488200, 'population_density': 1809},
    'Quảng Ninh': {'population': 1362880, 'population_density': 220},
    'Hải Dương': {'population': 1946820, 'population_density': 1167},
    'Hải Phòng': {'population': 2088020, 'population_density': 1368},
    'Hưng Yên': {'population': 1290850, 'population_density': 1388},
    'Thái Bình': {'population': 1878540, 'population_density': 1185},
    'Hà Nam': {'population': 878000, 'population_density': 1019},
    'Nam Định': {'population': 1876850, 'population_density': 1125},
    'Ninh Bình': {'population': 1010700, 'population_density': 716},
    'Hà Giang': {'population': 892720, 'population_density': 113},
    'Cao Bằng': {'population': 543050, 'population_density': 81},
    'Bắc Kạn': {'population': 324350, 'population_density': 67},
    'Tuyên Quang': {'population': 805780, 'population_density': 137},
    'Lào Cai': {'population': 770590, 'population_density': 121},
    'Yên Bái': {'population': 847250, 'population_density': 123},
    'Thái Nguyên': {'population': 1335990, 'population_density': 379},
    'Lạng Sơn': {'population': 802090, 'population_density': 97},
    'Bắc Giang': {'population': 1890930, 'population_density': 485},
    'Phú Thọ': {'population': 1516920, 'population_density': 429},
    'Điện Biên': {'population': 635920, 'population_density': 67},
    'Lai Châu': {'population': 482100, 'population_density': 53},
    'Sơn La': {'population': 1300130, 'population_density': 92},
    'Hòa Bình': {'population': 875380, 'population_density': 191},
    'Thanh Hóa': {'population': 3722060, 'population_density': 335},
    'Nghệ An': {'population': 3419990, 'population_density': 207},
    'Hà Tĩnh': {'population': 1323750, 'population_density': 221},
    'Quảng Bình': {'population': 913860, 'population_density': 114},
    'Quảng Trị': {'population': 650950, 'population_density': 138},
    'Thừa Thiên Huế': {'population': 1160220, 'population_density': 235},
    'Đà Nẵng': {'population': 1220190, 'population_density': 950},
    'Quảng Nam': {'population': 1519380, 'population_density': 144},
    'Quảng Ngãi': {'population': 1245650, 'population_density': 242},
    'Bình Định': {'population': 1504290, 'population_density': 248},
    'Phú Yên': {'population': 876620, 'population_density': 174},
    'Khánh Hòa': {'population': 1253970, 'population_density': 241},
    'Ninh Thuận': {'population': 598680, 'population_density': 178},
    'Bình Thuận': {'population': 1252060, 'population_density': 158},
    'Kon Tum': {'population': 579910, 'population_density': 60},
    'Gia Lai': {'population': 1590980, 'population_density': 103},
    'Đắk Lắk': {'population': 1918440, 'population_density': 147},
    'Đắk Nông': {'population': 670560, 'population_density': 103},
    'Lâm Đồng': {'population': 1332530, 'population_density': 136},
    'Bình Phước': {'population': 103467, 'population_density': 151},
    'Tây Ninh': {'population': 1188760, 'population_density': 294},

    'Bình Dương': {'population': 2763120, 'population_density': 1025},
    'Đồng Nai': {'population': 3255810, 'population_density': 555},
    'Bà Rịa Vũng Tàu': {'population': 1178700, 'population_density': 595},
    'Hồ Chí Minh': {'population': 9389720, 'population_density': 4481},
    'Long An': {'population': 1734260, 'population_density': 386},
    'Tiền Giang': {'population': 1785240, 'population_density': 698},
    'Bến Tre': {'population': 129801, 'population_density': 545},
    'Trà Vinh': {'population': 101926, 'population_density': 426},
    'Vĩnh Long': {'population': 102882, 'population_density': 674},
    'Đồng Tháp': {'population': 160017, 'population_density': 473},
    'An Giang': {'population': 190552, 'population_density': 539},
    'Kiên Giang': {'population': 1751760, 'population_density': 276},
    'Cần Thơ': {'population': 1252350, 'population_density': 869},
    'Hậu Giang': {'population': 729470, 'population_density': 450},
    'Sóc Trăng': {'population': 1197820, 'population_density': 363},
    'Bạc Liêu': {'population': 921810, 'population_density': 346},
    'Cà Mau': {'population': 1207630, 'population_density': 229}
    }
    print(create_population_df(population_dict))
