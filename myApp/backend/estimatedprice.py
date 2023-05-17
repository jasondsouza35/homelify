import myApp.backend.webscraper as webscraper
import csv
import pandas as pd
import nums_from_string

df = pd.read_csv("local_house_info.csv")
with open('local_house_info.csv') as csv_file:
    for ind in df.index:
        sqft = nums_from_string.get_nums(df.at[ind, 'Size'])
        sqft_range = 0
        if len(sqft) > 0:
            for val in sqft:
                sqft_range += abs(val)
            sqft_range /= len(sqft)
        df.at[ind, 'Size'] = sqft_range
    df.to_csv("local_house_info.csv", index=False)

    similar_prices = []
    for ind in df.index:
        if webscraper.house_sqft * 0.8 < df.at[ind, 'Size'] < webscraper.house_sqft * 1.2:
            similar_prices.append(int(df.at[ind, 'Price']))

    if len(similar_prices) == 0:
        estimated_price = "Not available"
    else:
        estimated_price = int(sum(similar_prices) / len(similar_prices))
    print(estimated_price)
