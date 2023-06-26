# Text-to-SQL Conversion
This project demonstrates a Text-to-SQL conversion system using ClickHouse and OpenAI GPT model. The system takes user prompts or questions, generates SQL queries, executes them on a ClickHouse database, and returns the query results.

## Installation
Clone the repository:

 ```bash
 git clone https://github.com/your-username/text-to-sql-conversion.git
 ```


Install the required dependencies:
 ```bash
pip install -r requirements.txt
 ```

Configuration
Open the config.py file and provide the necessary configuration settings:

# ClickHouse database configuration
host = 'n5kuudqxis.eu-central-1.aws.clickhouse.cloud'
port = 8443
username = 'default'
password = 'vzKIqa77MsfN_'

# OpenAI GPT model configuration
gpt_model = 'juierror/text-to-sql-with-table-schema'
Save the config.py file.


Usage
To use the Text-to-SQL conversion system, follow these steps:

Run the main.py file:

python main.py


Choose a table from the available options:

Please choose one option:
1. bing_ads
2. customers_data
3. daily_website_visits
...
Enter a prompt or question when prompted:

Please enter a prompt: How many clicks were there on '2022-01-01' in the bing_ads table?

The system will generate an SQL query based on the prompt and the selected table:

SELECT clicks FROM bing_ads WHERE date = '2022-01-01'


The generated SQL query will be executed on the ClickHouse database and the results will be displayed.

[('100',)]

Limitations
The system currently supports ClickHouse as the database backend. It may not be compatible with other database systems.
The system relies on the provided ClickHouse database schema and may not handle complex queries or schema changes.
The performance and accuracy of the Text-to-SQL conversion depend on the underlying GPT model and the training data.
