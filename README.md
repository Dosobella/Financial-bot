# Financial-chat-bot

## Overview
This project showcases a simple financial data chatbot developed using Python. The chatbot uses the Pandas library to manipulate and analyze financial data stored in a CSV file. It can respond to specific user queries related to financial metrics such as net income, total assets, total revenue among others of different companies like Apple, Microsoft and Tesla as provided in their 10-K filing.

## Features
- **Total Revenue Calculation**: Computes the sum of total revenue for all the companies from 2021 to 2023.
- **Net Income Inquiry**: Provides the net income for Apple in a specific years.
- **Liabilities Analysis**: Returns the total liabilities of Microsoft over a three-year period.
- **Cash Flow Comparison**: Identifies the company with the highest cash flow in a given year.
- **Dynamic User Interaction**: Handles incorrect inputs and prompts users to re-enter valid data.
- **Revenue Generation and Asset Comparison**: Provides revenue data for Tesla in 2023 and compares total assets of Tesla and Apple.

## Code Explanation
(# -*- coding: utf-8 -*- 
""" 
Created on Tue Oct  1 11:22:32 2024 
@author: Dosobella 
"""

import pandas as pd  # Importing the Pandas library for data manipulation

# Load your financial data into a Pandas DataFrame (replace with your actual file path)
df = pd.read_csv(r'C:\Users\toms\OneDrive\Desktop\CEPHAS\Python\Practice mode\financial_data.csv')

def simple_chatbot(user_query):
    """
    A simple chatbot function to handle predefined financial queries.
    
    Parameters:
    user_query (str): The user's query to be processed by the chatbot.
    
    Returns:
    str: The result of the query or a predefined response.
    """
    user_query = user_query.lower()  # Convert user query to lowercase for case-insensitive comparison

    # Handle query for total revenue
    if user_query == "what was the overall total revenue for the companies over the three years?":
        total_revenue = df['Total Revenue'].sum()
        return f"The overall total revenue was ${total_revenue}"

    # Handle query for Apple's net income for a specific year
    elif user_query == "what was the net income for apple in 2022?":
        years = [2021, 2022, 2023]
        while True:
            year = input('Enter year: ')
            try:
                year = int(year)  # Ensure the year is converted to an integer
                if year in years:
                    net_income = df[(df['Company'] == 'Apple') & (df['Year'] == year)]['Net Income'].values[0]
                    return f"The net income for Apple in {year} was $ {net_income:.2f}"
                else:
                    print("Please enter a valid year from 2021, 2022, or 2023.")
            except ValueError:
                print("Please enter a valid integer for the year.")

    # Handle query for Microsoft's total liabilities over three years
    elif user_query == "what was the total liabilities for microsoft over the three years?":
        total_liabilities = df[(df['Company'] == 'Microsoft') & (df['Year'].isin([2021, 2022, 2023]))]['Total Liabilities'].sum()
        return f"The total liabilities for Microsoft from 2021 to 2023 was $ {total_liabilities}"

    # Handle query for the company with the highest cash flow in 2021
    elif user_query == "which company had the highest cash flow in 2021, and what was the value?":
        df_2021 = df[df['Year'] == 2021]
        best_company = df_2021.loc[df_2021['Cash Flow'].idxmax()]
        return f"{best_company['Company']} had the highest cash flow in 2021 with a value of $ {best_company['Cash Flow']}."

    # Handle query for Tesla's total revenue in 2023
    elif user_query == "what was the total revenue that tesla generated in 2023?":
        total_revenue_tesla_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Total Revenue'].values[0]
        return f"The total revenue that Tesla generated in 2023 was $ {total_revenue_tesla_2023}"

    # Handle query for the difference between total assets of Tesla and Apple
    elif user_query == "how much value of total assets did apple own than tesla in 2022?":
        total_assets_tesla = df[(df['Company'] == 'Tesla') & (df['Year'] == 2022)]['Total Assets'].values[0]
        total_assets_apple = df[(df['Company'] == 'Apple') & (df['Year'] == 2022)]]['Total Assets'].values[0]
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


##Project Highlights
- **Dynamic Error Handling**: The chatbot is equipped to handle invalid user inputs gracefully, prompting for corrections.
- **Predefined and Specific Queries**: Allows for specific, predefined queries ensuring accurate and relevant responses.
- **Extensible Design**: New queries can be added easily by defining additional conditions within the simple_chatbot function.

## Prerequisites
- **Python**: Make sure you have Python installed on your machine.
- **Pandas Library**: Install Pandas using `pip install pandas`.
- **CSV File**: Have a properly formatted CSV file with relevant financial data.

## Setup
1. **Clone the Repository**: `git clone https://github.com/yourusername/financial-bot.git`
2. **Navigate to Directory**: `cd Financial-bot`
3. **Install Dependencies**: `pip install pandas`

## Usage
1. **Run the Script**: Execute the script in a Python environment.
2. **Interaction**: Input your queries as prompted. Use 'quit' to exit the interaction.

## Future Enhancements
- **Natural Language Processing**: Implement NLP to handle a wider range of queries.
- **Data Visualization**: Integrate data visualization for more insightful responses.
- **Web Interface**: Develop a web interface for easier interaction with the chatbot.
