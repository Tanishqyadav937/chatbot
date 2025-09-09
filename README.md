Financial Analysis Chatbot 🤖📊

A Python-based prototype chatbot designed for financial data analysis. This chatbot can answer predefined financial queries and analyze key metrics of companies like Apple, Tesla, and Microsoft.

Overview 📝

This project is a prototype financial analysis chatbot created for the Forage task submission. It responds to predefined financial queries using a simple pattern matching approach.

It also includes a sample dataset of Apple, Tesla, and Microsoft (2022–2024) for trend analysis.

Features ✨

Answer predefined financial queries:

Revenue and sales questions

Net income and profit questions

Operating expenses questions

Total assets questions

General financial performance questions

Handle basic greetings, help requests, and exit commands.

Simple command-line interface for easy interaction.

Financial dataset analysis: Revenue, Net Income, Total Assets, Liabilities, Profit Margin, and Cash Flow trends.

Can be extended with more advanced AI/NLP features in the future.

Implementation Details ⚙️

Built using Python (no external dependencies required)

Uses regular expressions for pattern matching

Includes static financial data for Apple, Tesla, and Microsoft

Simple CLI-based interface

Optional: Can integrate Pandas/Matplotlib for data visualizations

Sample Financial Data 📊
Company	Fiscal Year	Total Revenue (USD mn)	Net Income (USD mn)	Total Assets (USD mn)	Total Liabilities (USD mn)	Profit Margin (%)	Cash Flow from Operations (USD mn)
Apple	2022	394000	99900	352000	302000	25.4	122000
Apple	2023	383000	96900	354000	310000	25.3	110000
Apple	2024	385000	100000	360000	315000	26.0	118000
Tesla	2022	81500	12500	62000	31000	15.3	14500
Tesla	2023	96300	12550	85000	42000	13.0	13500
Tesla	2024	123000	15000	118000	53000	12.2	17500
Microsoft	2022	198000	72700	364000	198000	36.7	89000
Microsoft	2023	212000	72000	395000	210000	34.0	91500
Microsoft	2024	236000	80000	420000	225000	33.9	94000
How to Use 🚀

Ensure Python is installed on your system.

Run the chatbot script:

python financial_chatbot.py


Type your financial query when prompted.

Type 'help' to see available options.

Type 'exit' to quit the program.

Predefined Queries 💬

The chatbot recognizes variations of these questions:

"What is the total revenue?"

"How has net income changed?"

"What are the operating expenses?"

"Tell me about total assets"

"How is the company's financial performance?"

Limitations ⚠️

Only handles predefined financial queries

Uses simple pattern matching, not AI/NLP

Contains static financial data

Cannot handle complex or follow-up questions

Project Structure 🗂️
financial-chatbot/
│
├─ data/                 # Sample financial dataset (CSV/Excel)
├─ scripts/              # Python scripts (chatbot & analysis)
├─ notebooks/            # Optional Jupyter notebooks for visualization
├─ requirements.txt      # Optional dependencies
└─ README.md             # Project documentation

How to Contribute 🤝

Fork the repository

Create a new branch: git checkout -b feature/your-feature

Make your changes and commit: git commit -m "Add some feature"

Push to the branch: git push origin feature/your-feature

Open a Pull Request
