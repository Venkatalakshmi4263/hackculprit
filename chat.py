import re
import pandas as pd

# Load the exported chat file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# Preprocess the data
def preprocess_data(data):
    # Split messages based on date and time pattern
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[AP]M)\s-\s'
    messages = re.split(pattern, data)[1:]
    
    # Separate dates and messages
    dates = messages[::2]
    messages_content = messages[1::2]
    
    # Create a DataFrame
    df = pd.DataFrame({'date': dates, 'message': messages_content})
    
    # Convert date format
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y, %I:%M %p')
    
    # Separate user and message
    user_message = df['message'].str.split(':', n=1, expand=True)
    df['user'] = user_message[0]
    df['message'] = user_message[1]
    
    return df

# Analyze the data
def analyze_data(df):
    # Count messages per user
    message_counts = df['user'].value_counts()
    print("Messages per user:\n", message_counts)
    
    # Find the most active day
    most_active_day = df['date'].dt.date.value_counts().idxmax()
    print("\nMost active day:", most_active_day)
    
    # Extract time-based features
    df['hour'] = df['date'].dt.hour
    
    # Count messages per hour
    hourly_counts = df['hour'].value_counts().sort_index()
    print("\nMessages per hour:\n", hourly_counts)
    
    return df
    
# Main function
def main():
    file_path = 'chat.txt'
    data = load_data(file_path)
    df = preprocess_data(data)
    df = analyze_data(df)
    print(df.head())

if _name_ == "_main_":
    main()