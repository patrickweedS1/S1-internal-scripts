import httpx

from typing import Optional

URL = ""
TOKEN = ""
ACCOUNT_ID = ""

HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}

CLIENT = httpx.Client(base_url=URL, headers=HEADERS, timeout=None)


def get_account(account_id: str) -> dict:
    res = CLIENT.get(f"/web/api/v2.1/accounts/{account_id}")
    res.raise_for_status()

    data = res.json()["data"]

    return data


def set_ranger_consolidation(
    account_id: str,
    account_body: dict,
    level: Optional[str] = "Site",
) -> dict:
    path = f"/web/api/v2.1/accounts/{account_id}"

    for setting_entry in account_body["licenses"]["settings"]:
        if setting_entry["groupName"] == "account_level_ranger":
            setting_entry["setting"] = level

    body = {"data": account_body}

    res = CLIENT.put(path, json=body)
    res.raise_for_status()

    return res.json()["data"]


def main() -> None:
    account: dict = get_account(ACCOUNT_ID)

    current_config = [
        x["setting"]
        for x in account["licenses"]["settings"]
        if x["groupName"] == "account_level_ranger"
    ][0]

    print(f"Current value: {current_config}")

    new_account = set_ranger_consolidation(ACCOUNT_ID, account, "Site")

    new_config = [
        x["setting"]
        for x in new_account["licenses"]["settings"]
        if x["groupName"] == "account_level_ranger"
    ][0]

    print(f"New value: {new_config}")


if __name__ == "__main__":
    main()
