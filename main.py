import pandas as pd
import matplotlib.pyplot as plt

# Define the path to my CSV file
file_path = 'owid-covid-data.csv'

# Load the CSV file
try:
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    print("COVID-19 data loaded successfully!")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()
except Exception as e:
    print(f" An error occurred: {e}")
    exit()

def get_country_data(df, country_name):
    country_name_lower = country_name.lower()
    country_data = df[df['location'].str.lower() == country_name_lower].copy()
    if country_data.empty:
        print(f" Warning: No data for '{country_name}'.")
    return country_data

if __name__ == "__main__":
    print("\n")
    print("###########################################################################################################")
    print("\n")
    print("                 ## Welcome to the COVID-19 Data Analysis Tool! ##               ")
    print("\n")
    print("                               Perform Analysis Now!                   ")
    print("\n")
    print("                  If you want to analyze data for multiple countries separate them with commas.") 
    print("\n")
    countries_input = input("                  Enter countries for analysis (comma-separated): ").split(',')
    selected_countries = [c.strip() for c in countries_input]
    country_dfs = {country: get_country_data(df, country) for country in selected_countries}
    valid_countries = {country: data for country, data in country_dfs.items() if not data.empty}

    if not valid_countries:
        print("⚠️ No valid country data entered.")
        exit()

    print("\n📈 Generating visualizations...")
    print(country_dfs)

    # 1. Plot total cases over time
    plt.figure(figsize=(12, 6))
    for country, data in valid_countries.items():
        plt.plot(data['date'], data['total_cases'], label=country)
    plt.title("Total COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 2. Plot total deaths over time
    plt.figure(figsize=(12, 6))
    for country, data in valid_countries.items():
        plt.plot(data['date'], data['total_deaths'], label=country)
    plt.title("Total COVID-19 Deaths Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 3. Plot total vaccinations over time
    plt.figure(figsize=(12, 6))
    for country, data in valid_countries.items():
        if 'total_vaccinations' in data.columns and not data['total_vaccinations'].isnull().all():
            plt.plot(data['date'], data['total_vaccinations'], label=country)
        else:
            print(f"⚠️ No vaccination data for {country}.")
    plt.title("Total COVID-19 Vaccinations Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Vaccinations")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\n✅ Visualizations generated. Now, let's look at some insights.")

    # You would now manually analyze the generated plots and potentially the data
    # in a Jupyter Notebook to derive insights and identify anomalies.
    # The following is a placeholder to remind you of the next step.

    print("\n➡️ To see key insights and anomalies, please run this script in conjunction with a Jupyter Notebook.")
    print("   You can then examine the generated plots and the 'valid_countries' dataframes.")
    print("   Use Markdown cells in your notebook to write your observations.")