import pandas as pd

def logic_function(price):
    # Your logic function implementation here
    # Example: Buy if price is below a certain threshold, sell otherwise
    if price < 120:
        return "Buy"
    else:
        return "Sell"

def apply_logic_to_dataset(dataset):
    # Apply logic function to each price in the dataset
    dataset['Action'] = dataset['close'].apply(logic_function)
    return dataset

# Load the dataset from a CSV file
dataset = pd.read_csv('AAPL_data.csv')

# Apply the logic function to the dataset
dataset_with_actions = apply_logic_to_dataset(dataset)

# Print the updated dataset with actions
dataset_with_actions[['close', 'Action']].to_csv('new_dataset.csv', index=False)

def calculate_moving_average(dataset):
    dataset['Moving Average'] = dataset['close'].rolling(window=22).mean()
    return dataset

# Calculate the moving average on the dataset
dataset_with_moving_average = calculate_moving_average(dataset)

# Print the updated dataset with moving average
dataset['Moving Average'] = dataset_with_moving_average['Moving Average']
print(dataset[['close', 'Moving Average']])