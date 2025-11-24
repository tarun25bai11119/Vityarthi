🏥 Patient Record Manager (Python CLI)

A straightforward command-line application built in Python for managing basic patient information, medical history, and visits. Data is automatically saved to a local file (patients.json).

✨ Key Features

Patient Management: Add, View, Update, Delete, List, and Search patients by ID or Name.

Records: Log new medical conditions (automatically dated).

Visits: Record clinical visits with doctor and reason details (automatically dated).

Data Persistence: Uses the json module to save and load all records, ensuring data is kept between sessions.

🚀 Getting Started

Prerequisites

You must have Python 3 installed on your system.

Execution

Save the Code: Save the Python code as patient_manager.py.

Run in Terminal: Execute the script from your command line:

python patient_manager.py


Follow the Menu: Use the numbered menu (1-9) to interact with the application.

🗃️ Data Storage

The application uses patients.json to store all data. Records are indexed by unique Patient IDs, which serve as the primary key.