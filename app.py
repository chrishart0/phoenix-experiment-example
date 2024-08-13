import phoenix as px

from phoenix.experiments.evaluators import ContainsAnyKeyword
from phoenix.experiments import run_experiment
from phoenix.experiments.types import Example

import pandas as pd

phoenix_client = px.Client(endpoint="http://localhost:6006")

df = pd.DataFrame(
    [
        {
            "question": "What is your name?",
            "answer": "My name is TestAgent.",
            "metadata": {"name": "TestAgent"},
        }
    ]
)

# Delete dataset if it exists
dataset_name = "test-dataset"

try:
    dataset = phoenix_client.get_dataset(name=dataset_name)
    print("Dataset:")
    print(dataset)
except ValueError:
    print("Dataset does not exist, creating new dataset")
    dataset = phoenix_client.upload_dataset(
        dataframe=df,
        dataset_name=dataset_name,
        input_keys=["question"],
        output_keys=["answer"],
        metadata_keys=["metadata"],
    )
    print("Dataset uploaded successfully")
    print(dataset)


def task(example: Example) -> str:
    print("task!")
    return "My name is ExampleAgent."

### Setup Evaluators ###
contains_keyword = ContainsAnyKeyword(keywords=["ExampleAgent", "name"])

experiment = run_experiment(
    dataset,
    task,
    experiment_name="initial-experiment",
    evaluators=[contains_keyword],
    # dry_run=True,
)

print(experiment)
#######################
