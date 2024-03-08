from google.cloud import aiplatform
from predict_model_sample import predict_model_sample


if __name__ == "__main__":
    predict_model_sample(
        project="35914197091",
        endpoint_id="492783519383158784",
        location="europe-west2",
        instances={ "instance_key_1": "Name a car brand"}
    )