from current_values import source_destiny
from dotenv import dotenv_values
import requests

env = dotenv_values(".env")

url = env["LOGIN_URL"]
user_info = {"user": env["USER"], "password": env["PASSWORD"]}
headers = {"Content-Type": "application/json"}

logIn_response = requests.post(f"{url}/3dves/user/logIn", user_info, headers)
token = logIn_response.json().get("token")

sankey = {"type": "energy", "sourceDestiny": source_destiny()}
auth_headers = {"Authorization": token, "Content-Type": "application/json"}


def handler(event, context):
    water_sankey = requests.post(
        f"{url}/3dves/project/996/energyFlowDiagram/energy",
        json=sankey,
        headers=auth_headers,
    )
    if water_sankey.status_code == 200:
        print(
            f"status code: {water_sankey.status_code}, event: {event}, context: {context}"
        )
    else:
        print("error escribiendo energy sankey")


handler("test", "manual")
