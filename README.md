# Text-to-SQL Conversion
This project demonstrates a Text-to-SQL conversion system using ClickHouse and transformer-based model. The system takes user prompts or questions, generates SQL queries, executes them on a ClickHouse database, and returns the query results.

## Installation
Clone the repository:

 ```bash
git clone https://github.com/your-username/text-to-sql-conversion.git
 ```

Install the required dependencies:
 ```bash
pip install -r requirements.txt
 ```

## Usage
To use the Text-to-SQL conversion system, follow these steps:

Run the main.py file

Choose a table from the available options:

Please choose one option:
1. bing_ads
2. customers_data
3. daily_website_visits
...

Enter a prompt or question when prompted:

Please enter a prompt: How many clicks were there on '2022-01-01' in the bing_ads table?

The system will generate an SQL query based on the prompt and the selected table:

 ```bash
SELECT clicks FROM bing_ads WHERE date = '2022-01-01'
 ```

The generated SQL query will be executed on the ClickHouse database and the results will be displayed.

## Current Progress
1. The tool interacts with the Clickhouse database.
2. The tool asks the user to input table name and a prompt.
3. The tool converts the prompt to SQL.
4. The tool uses generated SQL to pull data from Clickhouse database and return the result to the user.
5. Generated a dataset (dataset.txt) with 100 prompt-sql pairs in order to fine-tune the model in the future.


## Limitations
The system doesn't perform well in converting natural language to SQL yet.
The system relies on the provided ClickHouse database schema and may not handle complex queries or schema changes.
The performance and accuracy of the Text-to-SQL conversion depend on the underlying transformer model.


## Further Improvements
1. Fine-tune the model using the collected dataset.
2. Develop testing methods to evaluate the model and calculate score metrics.
3. Develop validation techniques to prevent errors while converting text to SQL.
