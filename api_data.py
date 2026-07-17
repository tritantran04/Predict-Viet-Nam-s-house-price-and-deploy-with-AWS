import pandas as pd

def create_data_for_api(new_data, population, province_region):
    use_cols = [
                'average_area_by_density', 'average_floors_by_density', 
                'average_price_by_region_grouped', 'region_grouped', 'region'
                ]
    new_data = new_data[use_cols]
    new_data = new_data.drop_duplicates(subset='region', keep='last')
    population = population.merge(province_region, on='province', how='left')
    population = population.merge(new_data, on='region', how='left')
    return population

if __name__ == "__main__":
    new_data = pd.read_csv('data/new_data.csv')
    population = pd.read_csv('data/population.csv')
    province_region = pd.read_csv('data/province_region.csv')
    data = create_data_for_api(new_data, population, province_region)
    data.to_csv('data_for_api.csv', index=False)