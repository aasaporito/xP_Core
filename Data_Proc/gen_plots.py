import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

FOLDER_NAME = "run11"
os.mkdir(f"plots_{FOLDER_NAME}")
def read_json_files(directory):
    """
    Reads all JSON files from the specified directory and returns a list of dictionaries.
    Each dictionary corresponds to the contents of a JSON file.
    """
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                subdata = []
                for line in f:
                    line = line.strip()
                    if line != "":
                        try:
                            subdata.append(json.loads(line))
                        except:
                            pass
            data.append(subdata)
                #file_data = f.read()
                #data.append(file_data)
    return data

def convert_to_dataframe(data):
    """
    Converts a list of dictionaries into a pandas DataFrame.
    """
    dfs = []
    for subdata in data:
        df = pd.DataFrame(subdata)
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df


def plot_all(directory):
    """
    """
    BULK_DF = pd.DataFrame(columns=['Quadrant', 'Chromosome', 'Score', 'Iteration'])

    plt.figure(figsize=(80, 20))  # Adjust the width and height as needed
    for filename in os.listdir(directory):
        data = []
        print(filename)
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                subdata = []
                for line in f:
                    line = line.strip()
                    if line != "":
                        try:
                            subdata.append(json.loads(line))
                        except:
                            pass
            data.append(subdata)
            # file_data = f.read()
            # data.append(file_data)

        for subdata in data:
            df = pd.DataFrame(subdata)

        df.columns = ["Quadrant", "Chromosome", "Score"]

        # Shift scores up by 1 as it corresponds to the previous life.
        df['Score'] = df['Score'].shift(-1)
        df['Score'] = df['Score'].astype(float)  # Cast scores to integers
        df['Score'] = df['Score'].round()  # Round
        df = df[df['Score'] != 0.0]
        df.dropna(inplace=True)  # Drop rows with missing values

        df['Chromosome'] = [','.join(map(str, l)) for l in df['Chromosome']]
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)
        df['Iteration'] = df.index

        # Plot
        plt.scatter(df.index, df['Score'], label=filename)
        BULK_DF = pd.concat([BULK_DF, df], ignore_index=True)

    plt.xlabel('Index')
    plt.ylabel('Score')
    plt.title('Line Plot of Scores')
    plt.legend()
    plt.grid(True)
    print(BULK_DF)

    x = list(BULK_DF.Iteration.to_numpy())
    y = list(BULK_DF['Score'].to_numpy())

    # m, b = np.polyfit(x, y, 1)

    corr, p = pearsonr(x, y)
    print(f"Bulk Pearson: {corr}")
    # print(f"P-Value: {p}")
    # plt.plot(x, m * x + b, color="red", linewidth=4, label=f'm={m}')

    plt.savefig(f'plots_{FOLDER_NAME}/scores.png')
    return df


plot_all(FOLDER_NAME)


def sub_plots(directory):
    """
    """
    for filename in os.listdir(directory):
        plt.figure(figsize=(40, 20))  # Adjust the width and height as needed

        data = []
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                subdata = []
                for line in f:
                    line = line.strip()
                    if line != "":
                        try:
                            subdata.append(json.loads(line))
                        except:
                            pass
            data.append(subdata)
            # file_data = f.read()
            # data.append(file_data)

        for subdata in data:
            df = pd.DataFrame(subdata)

        df.columns = ["Quadrant", "Chromosome", "Score"]

        # Shift scores up by 1 as it corresponds to the previous life.
        df['Score'] = df['Score'].shift(-1)
        df['Score'] = df['Score'].astype(float)  # Cast scores to integers
        df['Score'] = df['Score'].round()  # Round
        df.dropna(inplace=True)  # Drop rows with missing values
        df = df[df['Score'] != 0.0]

        df['Chromosome'] = [','.join(map(str, l)) for l in df['Chromosome']]
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)

        subset_df = df.iloc[::10]
        try:
            x = df.index.to_numpy()
            y = df['Score'].to_numpy()

            m, b = np.polyfit(x, y, 1)
        except Exception as e:
            continue
        corr, p = pearsonr(x, y)
        print(f"Pearson: {corr}")
        print(f"P-Value: {p}")
        plt.plot(x, m * x + b, color="red", linewidth=4, label=f'm={m}')

        # Plot
        plt.scatter(x, y, label=filename)
        # plt.plot(subset_df.index, subset_df['Score'], marker='x', linestyle='-', label=filename)
        plt.xlabel('Iteration')
        plt.ylabel('Score')
        plt.title(f'Line Plot of Scores: {filename}')
        # plt.title(f'Line Plot of every 10 iteration Scores: {filename}')

        # Fit the trend line
        # z = np.polyfit(df.index, df['Score'], 1)
        # p = np.poly1d(z)
        # plt.plot(df.index,p(df['Score']),"r--")

        plt.legend()
        plt.grid(True)
        plt.savefig(f'plots_{FOLDER_NAME}/{filename.split(".")[0]}.png')
    return df


sub_plots(FOLDER_NAME)
