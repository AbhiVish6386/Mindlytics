import requests

def generate_bearer_token(api_key, env_file_path):
    token_url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": api_key,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }

    try:
        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()
        bearer_token = response.json().get("access_token")

        if bearer_token:
            with open(env_file_path, 'w') as f:
                f.write(f'API_KEY="{api_key}"\n')
                f.write(f'BEARER_TOKEN="{bearer_token}"\n')
            print(f"✅ Token written successfully to: {env_file_path}")
        else:
            print("❌ Token not found in response.")

    except Exception as e:
        print("❌ Error while generating token:", e)

# 👇 Replace this path if needed
api_key = "b5aaf9LiD4QmedzXXkSgxQbKfabM3XQYHJZM80vok2iG"
env_file_path = r"C:\Users\av828\VSPrograms\PythonVS\Predictiv_analysis\predictive_dashboard\.env"

generate_bearer_token(api_key, env_file_path)
