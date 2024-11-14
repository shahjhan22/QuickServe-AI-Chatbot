import re
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


if __name__=="__main__":
    print(extract_session_id("projects/shah-chatbot-for-food-del-yh9a/agent/sessions/86e334ab-ba79-851f-1333-dd7ed3dc1c47/contexts/ongoing-order"))