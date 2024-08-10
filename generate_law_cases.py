import pandas as pd
import random

# Define the data structure
case_categories = ["Criminal", "Civil", "Family Law", "Intellectual Property", "Employment Law"]
case_titles = ["Case Title " + str(i) for i in range(1, 501)]
case_descriptions = ["Description of case " + str(i) for i in range(1, 501)]
example_questions = ["What was the outcome of Case Title " + str(i) + "?" for i in range(1, 501)]
example_responses = ["The case resulted in a decision for the plaintiff." for i in range(1, 501)]

# Generate random category for each case
random_categories = [random.choice(case_categories) for _ in range(500)]

# Create the DataFrame
df = pd.DataFrame({
    "Case ID": range(1, 501),
    "Case Title": case_titles,
    "Case Description": case_descriptions,
    "Category": random_categories,
    "Example Question": example_questions,
    "Example Response": example_responses
})

# Save to CSV
df.to_csv("law_cases_dataset_large.csv", index=False)
