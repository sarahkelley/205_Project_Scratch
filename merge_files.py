import pandas as pd

all_files = ["tweet_output_1.csv", "tweet_output_2.csv", "tweet_output_3.csv", "tweet_output_4.csv" ]
final = (pd.concat((pd.read_csv(f) for f in all_files)))

final.to_csv("merged_output.csv")