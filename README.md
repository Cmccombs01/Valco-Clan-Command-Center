
# 🛡️ VALCO Clan Command Center: Data Pipeline & Analytics
The VALCO Command Center is a high-level strategic tool built to optimize clan performance in World of Tanks. By automating data extraction from the Wargaming API, this dashboard provides real-time insights into player activity, combat effectiveness, and recruitment needs, ensuring the VALCO clan remains a dominant force on the battlefield.

![Valco Dashboard](valco%20dashboard.png)

## 🚀 Overview
This project automates the extraction of player statistics from the **Wargaming API**, processes the data in **Python**, and pushes it to a **Google Sheets** cloud database. The final results are visualized in a live, interactive **Tableau Dashboard**.

### 🛠️ The Tech Stack
* **Language:** Python 3
* **API:** Wargaming.net API (World of Tanks)
* **Cloud Database:** Google Sheets API
* **Infrastructure:** Google Cloud Platform (Service Accounts)
* **Visualization:** Tableau Public

## 📊 Features
* **Performance Matrix:** A scatter plot identifying clan "Carriers" vs. "Support" players based on Win Rate and Avg Damage.
* **Master Roster:** A searchable list of all 97 members with real-time stats.
* **Top 10 Heavy Hitters:** A dynamic bar chart showing the clan's top damage dealers.
* **Inactivity Radar:** Automatically flags players who haven't battled in over 14 days.
