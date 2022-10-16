import webscraper
import csv
import pandas as pd
import nums_from_string

# with open('local_house_info.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

df = pd.read_csv("local_house_info.csv")
with open('local_house_info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if len(df) == line_count:
            break
        sqft = nums_from_string.get_nums(df.at[line_count, 'Size'])
        sqft_range = 0
        if len(sqft) > 0:
            for val in sqft:
                sqft_range += abs(val)
            sqft_range /= len(sqft)
        df.at[line_count, 'Size'] = sqft_range
        line_count += 1
    df.to_csv("local_house_info.csv", index=False)

    
# Check if the given house size is within 20% of the given size then adds the price to a list if that is the case,
# then averages that out


