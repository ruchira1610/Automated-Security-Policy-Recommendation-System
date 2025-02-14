import requests
import json
import pandas as pd
import re

# This function reads our "network_logs.txt" file and returns a list of rules.
def read_rules(file_path):
    with open(file_path, 'r') as file:
        rules = file.readlines()
    return rules

# This function looks for unsafe rules.
def find_unsafe_rules(rules):
    unsafe = []
    for rule in rules:
        if "Allow all" in rule:
            unsafe.append(rule.strip())
    return unsafe

# This function asks Google AI for advice on how to fix the unsafe rules.
def get_recommendations(unsafe_rules):
    api_key = "YOUR_API_KEY"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    prompt = "I found these unsafe network rules:\n"
    for rule in unsafe_rules:
        prompt += f"- {rule}\n"
    prompt += "\nFor each rule, categorize the threat as High, Medium, or Low and suggest a fix in this structured format:\n"
    prompt += "**| Rule | Threat Level | Suggested Fix |**"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        response_data = response.json()
        response_text = extract_ai_response(response_data)

        # ✅ Debugging Step: Print the Raw AI Response
        print("\n🔍 Raw AI Response:\n", response_text)
        
        return parse_response_to_table(response_text)
    else:
        return f"❌ Error: {response.status_code}, {response.text}"

# Extract AI response correctly
def extract_ai_response(response_data):
    candidates = response_data.get("candidates", [])
    if candidates and "content" in candidates[0]:
        return candidates[0]["content"]["parts"][0]["text"]
    return "No response received."

# Parses the AI response into a structured table format.
def parse_response_to_table(response_text):
    # ✅ Extract only the table portion using regex
    table_match = re.search(r"(\|.*?\|.*?\|.*?\|)", response_text, re.DOTALL)
    if not table_match:
        return "⚠️ AI Response was empty or incorrectly formatted."

    table_text = table_match.group(1)
    
    # ✅ Convert table text into structured rows
    lines = table_text.strip().split('\n')
    data = []
    
    for line in lines[1:]:  # Skip the header row
        parts = [col.strip() for col in line.split('|') if col.strip()]
        if len(parts) == 3:
            data.append(parts)
    
    if not data:
        return "⚠️ AI Response did not contain valid table data."

    df = pd.DataFrame(data, columns=["Rule", "Threat Level", "Suggested Fix"])
    return df

# The main function ties all the steps together.
def main():
    rules_file = r"YOUR_NETWORK_FILE_PATH"
    rules = read_rules(rules_file)
    
    print("📌 Network Rules:")
    for rule in rules:
        print(rule.strip())
    
    unsafe_rules = find_unsafe_rules(rules)
    
    if not unsafe_rules:
        print("\n✅ No unsafe rules found!")
    else:
        print("\n⚠️ Unsafe Rules Found:")
        for rule in unsafe_rules:
            print(rule)
        
        recommendations_df = get_recommendations(unsafe_rules)
        
        if isinstance(recommendations_df, pd.DataFrame):
            print("\n📊 Recommendations to Fix Unsafe Rules:")
            print(recommendations_df.to_string(index=False))


if __name__ == "__main__":
    main()
