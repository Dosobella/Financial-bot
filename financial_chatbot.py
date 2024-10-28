# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:21:56 2024

@author: Dosobella
"""

# Load your financial data into a Pandas DataFrame (replace with your actual file path)
import pandas as pd  # Importing the Pandas library for data manipulation
df = pd.read_csv(r'C:\Users\toms\OneDrive\Desktop\CEPHAS\Python\Practice mode\financial_data.csv')


def simple_chatbot(user_query):
    """
    A simple chatbot function to handle predefined financial queries.

    Parameters:
    user_query (str): The user's query to be processed by the chatbot.

    Returns:
    str: The result of the query or a predefined response.
    """
    user_query = user_query.lower(
    )  # Convert user query to lowercase for case-insensitive comparison

    # Handle query for total revenue
    if user_query == "what is the total revenue?":
        total_revenue = df['Total Revenue'].sum()
        return f"The total revenue is $ {total_revenue}"

    # Handle query for Apple's net income for a specific year
    elif user_query == "what was the net income for apple in 2022?":
        years = [2021, 2022, 2023]
        while True:
            year = input('Enter year: ')
            try:
                year = int(year)  # Ensure the year is converted to an integer
                if year in years:
                    net_income = df[(df['Company'] == 'Apple') & (
                        df['Year'] == year)]['Net Income'].values[0]
                    return f"The net income for Apple in {year} was $ {net_income:.2f}"
                else:
                    print("Please enter a valid year from 2021, 2022, or 2023.")
            except ValueError:
                print("Please enter a valid integer for the year.")

    # Handle query for Microsoft's total liabilities over three years
    elif user_query == "what was the total liabilities for microsoft over the three years?":
        total_liabilities = df[(df['Company'] == 'Microsoft') & (
            df['Year'].isin([2021, 2022, 2023]))]['Total Liabilities'].sum()
        return f"The total liabilities for Microsoft from 2021 to 2023 was $ {total_liabilities}"

    # Handle query for the company with the highest cash flow in 2021
    elif user_query == "which company had the highest cash flow in 2021?":
        df_2021 = df[df['Year'] == 2021]
        best_company = df_2021.loc[df_2021['Cash Flow'].idxmax()]
        return f"{best_company['Company']} had the highest cash flow in 2021 with a value of $ {best_company['Cash Flow']}."

    # Handle query for Tesla's total revenue in 2023
    elif user_query == "what was the total revenue that tesla generated in 2023?":
        total_revenue_tesla_2023 = df[(df['Company'] == 'Tesla') & (
            df['Year'] == 2023)]['Total Revenue'].sum()
        return f"The total revenue that Tesla generated in 2023 was $ {total_revenue_tesla_2023}"

    # Handle query for the difference between total assets of Tesla and Apple
    elif user_query == "what is the difference between the value of total assets for tesla and apple?":
        total_assets_tesla = df[(df['Company'] == 'Tesla')
                                ]['Total Assets'].sum()
        total_assets_apple = df[(df['Company'] == 'Apple')
                                ]['Total Assets'].sum()
        difference = total_assets_tesla - total_assets_apple
        return f"The difference between the total assets of Tesla and Apple is $ {difference}"

    # Default response for unrecognized queries
    else:
        return "Sorry, I can only provide information on predefined queries."


if __name__ == "__main__":
    """
    Main loop to keep the chatbot running and handle user input until 'quit' is entered.
    """
    while True:
        query = input("Enter your query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        response = simple_chatbot(query)
        print(response)
        print()
