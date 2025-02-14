# Automated-Security-Policy-Recommendation-System
## 📌 Project Overview  

The **Automated Security Policy Recommendation System** is a cybersecurity tool that analyzes network firewall rules and detects unsafe configurations. It uses **Gemini API** to suggest security improvements, helping organizations maintain robust firewall policies and mitigate vulnerabilities.

---

## ⚡ Features  

✅ **Firewall Rule Analysis** – Reads and evaluates network firewall configurations.  
✅ **Risk Detection** – Identifies unsafe rules based on cybersecurity best practices.  
✅ **Automated Recommendations** – Leverages AI to suggest security enhancements.  

---

## 🛠️ Installation & Setup  

### **Prerequisites**  
Ensure you have the following installed on your system:  
- **Python 3.x**  
- **pip (Python Package Manager)**
- **Libraries - pandas, regex, openai**
- **Sample Network/Firewall rules text file (network_logs.txt - available here)**

### **Step 1: Step-Up API Credentials**  
1. Login to Gemini
2. Create API Key
3. Copy the key to Notepad for further use

### **Step 2: Open any Python IDE and run the code**  
1. Paste the code as given in the securityRecommender.py file
2. Copy and Paste the path of the newtork_log.txt file in for attribute "YOUR_NETWORK_FILE_PATH"
3. Copy and Paste the API Key for "YOUR_API_KEY"
4. Run the code 

### **Ouput**
1. The program listed all the Network Rules found in the network_log.txt
2. The program then listed Unsafe Network Rules it found in the network_log.txt
3. With the help of Gemini, it recommended the changes that needs to be done for each unsafe rule in a tabular format

![image](https://github.com/user-attachments/assets/6a97a980-e716-4361-8a5d-afee0243bbf0)

