import json
from mercor import fetch_user_repo, most_complex
def handler(request):
    # Parse the request body to extract the necessary data
    data = json.loads(request.body)

    # Extract the input data from the request
    input_data = data.get("Please enter your github url: ")

    # Invoke your existing Python code using the input data
    repositories= fetch_user_repo(input_data)
    result = most_complex(repositories)

    # Return the result as the HTTP response
    response = {
        "statusCode": 200,
        "body": result
    }

    return response
