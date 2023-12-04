import pandas as pd
from googlesearch import search
import time
import random


# Function to perform a Google search and get the first 3 URLs
def get_google_search_results(query):
    urls = []
    try:
        for url in search(query, num_results=3):  # num replaces stop in some versions
            urls.append(url)
    except Exception as e:
        print(f"Error in Google search: {str(e)}")
    return urls

# Load the Excel file into a pandas dataframe
excel_file_path = 'companies.xlsx'
df = pd.read_excel(excel_file_path, sheet_name=0)  # Assuming the first sheet is used


# List of user agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    # Add more user agents if needed
]
#207
total_group = 440
counter = 300
df_results = pd.DataFrame(columns=['company_name', 'URL1', 'URL2', 'URL3'])

for counter in range(counter,total_group):

    # Perform the search
    for i in range(10):  # Number of searches to perform
        index = counter*10 + i
        print(f'index: {index}')
        selected_row = df.loc[index]
        user_agent = random.choice(user_agents)
        company_name = selected_row['company_name']
        query = f"{company_name} "
        
        try:
            # Get the first 3 URLs from the Google search
            urls = get_google_search_results(query)
            
            # Update the dataframe with the URLs
            df_results.at[index, 'company_name'] = company_name
            df_results.at[index, 'URL1'] = urls[0] if len(urls) >= 1 else ''
            df_results.at[index, 'URL2'] = urls[1] if len(urls) >= 2 else ''
            df_results.at[index, 'URL3'] = urls[2] if len(urls) >= 3 else ''
            
            print(f"Processed {company_name} - URLs: {urls}")
            time.sleep(15)
        except Exception as e:
                print(f"Error processing {company_name}: {str(e)}")
                time.sleep(15)
    # Save the updated dataframe to a new csv file
    output_excel_file_path = f'result/companies_completed_{counter}.csv'
    df_results.to_csv(output_excel_file_path, index=False)
    df_results = pd.DataFrame(columns=['company_name', 'URL1', 'URL2', 'URL3'])
    time.sleep(15)

    











# Iterate through rows and perform Google search for each company
# for index, row in df.iterrows():
#     company_name = row['company_name']
#     query = f"{company_name} official website"
    
#     try:
#         # Get the first 3 URLs from the Google search
#         urls = get_google_search_results(query)
        
#         # Update the dataframe with the URLs
#         df.at[index, 'URL1'] = urls[0] if len(urls) >= 1 else ''
#         df.at[index, 'URL2'] = urls[1] if len(urls) >= 2 else ''
#         df.at[index, 'URL3'] = urls[2] if len(urls) >= 3 else ''
        
#         print(f"Processed {company_name} - URLs: {urls}")
#         time.sleep(2)
#     except Exception as e:
#         print(f"Error processing {company_name}: {str(e)}")

# # Save the updated dataframe to a new Excel file
# output_excel_file_path = 'companies_completed.xlsx'
# df.to_excel(output_excel_file_path, index=False)
