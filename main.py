import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV loaded:", df.columns.tolist())
        return df
    except:
        print("Error reading file")
        return None

def create_bar_plot(df):
    plt.figure(figsize=(8, 5))
    plt.bar(df["Product"], df["Sales"])
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.savefig("bar_plot.png")
    plt.close()

def create_line_plot(df):
    plt.figure(figsize=(8, 5))
    plt.plot(df["Month"], df["Sales"])
    plt.title("Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.savefig("line_plot.png")
    plt.close()

df = read_data("sales_data.csv")
if df is not None:
    create_bar_plot(df)
    create_line_plot(df)
    print("Plots saved: bar_plot.png, line_plot.png")