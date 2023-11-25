from fastapi import FastAPI
import pandas as pd

app = FastAPI()

file_path = "sales_data_1.csv"
data = pd.read_csv(file_path)

@app.get('/overall-gross-margin')
def o_g_m():
    total_revenue = (data['Selling price'] * data['Quantity sold']).sum()
    total_cost = (data['Buying price'] * data['Quantity sold']).sum()
    overall_gross_margin = (total_revenue - total_cost) / total_revenue
    return {'overall_gross_margin': overall_gross_margin}


@app.get('/most-profitable-vendor')
def most_profitable_vendor():
    vendor_profit = data.groupby('Firm bought from')['Selling price'].sum() - data.groupby('Firm bought from')['Buying price'].sum()
    most_profitable_vendor = vendor_profit.idxmax()
    return {'most_profitable_vendor': most_profitable_vendor}


@app.get('/least-profitable-customer')
def least_profitable_customer():
    customer_profit = data.groupby('Customer')['Selling price'].sum() - data.groupby('Customer')['Buying price'].sum()
    least_profitable_customer = customer_profit.idxmin()
    return {'least_profitable_customer': least_profitable_customer}


@app.get('/most-profitable-day')
def most_profitable_day():
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')
    data['DayOfWeek'] = data['Date'].dt.dayofweek
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    data['DayOfWeek'] = data['DayOfWeek'].map(days)
    day_profit = data.groupby('DayOfWeek')['Selling price'].sum() - data.groupby('DayOfWeek')['Buying price'].sum()
    most_profitable_day = day_profit.idxmax()
    return {'most_profitable_day': most_profitable_day}



@app.get('/least-profitable-day')
def least_profitable_day():
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')
    data['DayOfWeek'] = data['Date'].dt.dayofweek
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    data['DayOfWeek'] = data['DayOfWeek'].map(days)
    day_profit = data.groupby('DayOfWeek')['Selling price'].sum() - data.groupby('DayOfWeek')['Buying price'].sum()
    least_profitable_day = day_profit.idxmin()
    return {'least_profitable_day': least_profitable_day}