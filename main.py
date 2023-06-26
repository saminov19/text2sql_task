import clickhouse_connect
from typing import List
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Retrieve table names from the ClickHouse database
client = clickhouse_connect.get_client(host='n5kuudqxis.eu-central-1.aws.clickhouse.cloud', port=8443, username='default', password='vzKIqa77MsfN_')
tokenizer = AutoTokenizer.from_pretrained("juierror/text-to-sql-with-table-schema")
model = AutoModelForSeq2SeqLM.from_pretrained("juierror/text-to-sql-with-table-schema")
query_tables = "SELECT table FROM system.columns WHERE database = 'default' GROUP BY table"
result_tables = client.command(query_tables)
table_names = result_tables.split('\n')
print(table_names)
    
# Display the options
print("Please choose one option:")
for i, option in enumerate(table_names):
    print(f"{i+1}. {option}")

# Prompt for user input and validate
table_name = None
while table_name is None:
    user_input = input("Enter the number corresponding to your choice: ")
    try:
        choice_index = int(user_input) - 1
        if 0 <= choice_index < len(table_names):
            table_name = table_names[choice_index]
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Print the chosen option
print("You chose the table:", table_name)


prompt = input("Please enter a prompt: ")

columns_query = f"SELECT name FROM system.columns WHERE database = 'default' AND table = '{table_name}'"
columns = client.command(columns_query)
columns = columns.split('\n')
print("Columns in the chosen table:", columns)


def prepare_input(question: str, table: List[str]):
    table_prefix = "table:"
    question_prefix = "question:"
    join_table = ",".join(table)
    inputs = f"{question_prefix} {question} {table_prefix} {join_table}"
    input_ids = tokenizer(inputs, max_length=700, return_tensors="pt").input_ids
    return input_ids

def inference(question: str, table: List[str]) -> str:
    input_data = prepare_input(question=question, table=table)
    input_data = input_data.to(model.device)
    outputs = model.generate(inputs=input_data, num_beams=10, top_k=10, max_length=700)
    result = tokenizer.decode(token_ids=outputs[0], skip_special_tokens=True)
    return result


query = inference(question=prompt, table=columns)
print(query)

result = client.command("SELECT clicks FROM bing_ads WHERE date = '2022-01-01'") #explicitly specified query to be replaced by the query variable above
print(result)


