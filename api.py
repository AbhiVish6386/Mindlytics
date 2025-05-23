import requests
import json

# Replace with your actual token
url = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/ffe1312f-edaf-4fd7-8eb1-0ac84870b226/predictions?version=2021-05-01"
bearer_token = "eyJraWQiOiIyMDI1MDMzMTA4NDUiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02OTQwMDBUWUNIIiwiaWQiOiJJQk1pZC02OTQwMDBUWUNIIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNTljN2UzMDQtZDQ2MS00NjE1LWJjZWEtYmYyNzIyZWVhNmU1IiwiaWRlbnRpZmllciI6IjY5NDAwMFRZQ0giLCJnaXZlbl9uYW1lIjoiQWJoaXNoZWsiLCJmYW1pbHlfbmFtZSI6IlZpc2h3YWthcm1hIiwibmFtZSI6IkFiaGlzaGVrIFZpc2h3YWthcm1hIiwiZW1haWwiOiJwYW5rYWp2aXNod2FrYXJtYW1lMTVAZ21haWwuY29tIiwic3ViIjoicGFua2FqdmlzaHdha2FybWFtZTE1QGdtYWlsLmNvbSIsImF1dGhuIjp7InN1YiI6InBhbmthanZpc2h3YWthcm1hbWUxNUBnbWFpbC5jb20iLCJpYW1faWQiOiJJQk1pZC02OTQwMDBUWUNIIiwibmFtZSI6IkFiaGlzaGVrIFZpc2h3YWthcm1hIiwiZ2l2ZW5fbmFtZSI6IkFiaGlzaGVrIiwiZmFtaWx5X25hbWUiOiJWaXNod2FrYXJtYSIsImVtYWlsIjoicGFua2FqdmlzaHdha2FybWFtZTE1QGdtYWlsLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiI0MzVkYmMyNjY3NmQ0ZmZmODA4OTAxY2NhZGM2YzQ3OCIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTc0NTA2NzUwNSwiZXhwIjoxNzQ1MDcxMTA1LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.gbKgFIQsOeGdvCUN6CrM13BFupqxOFC7rxQJbsMyyrdqe8Awv7b1U77jUr2xRd3-ZLhmskIdWRq03sLKhUZ6eSFAAlgtSnaZF03geqD-Ubvh1pMsHxXuNkFQ1C5-T-KMyDxs2Fpk8hnZhmh2Vv2xaLfJlW7noyNN22X-8SAgq8BsZtEW3UYYul1oKgURUO0xZzqVsV3y3VUlpFOjMbZnysg5Nr342s27pYsxHavAf9q0MW_a4Ev03AJ_NhsU9tSH9hQ6lPpPobHKmLmk8UF9ulhiGwhKMMoFPPyJaWZfKgAEScJ0O9jmCv3eU3noQA4qBUonn1A6qd_GTLJhaHYsLQ"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

payload = {
   "input_data": [
        {
            "fields": [
                "1. In a semester, how often you felt nervous, anxious or on edge due to academic pressure? ",
                "2. In a semester, how often have you been unable to stop worrying about your academic affairs? ",
                "3. In a semester, how often have you had trouble relaxing due to academic pressure? ",
                "6. In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?",
                "7. In a semester, how often have you felt afraid, as if something awful might happen?"
            ],
            "values": [[1,1,1,2,1]]  # 👈 yeh line tumhare answers honge
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("API response:", response.json())
