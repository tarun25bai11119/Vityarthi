import json
import os
from datetime import datetime

class PatientRecordManager:
    def __init__(self, data_file='patients.json'):
        self.data_file = data_file
        self.patients = {}
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.patients = json.load(file)
    
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.patients, file, indent=2)
    
    def add_patient(self):
        pid = input("Patient ID: ")
        if pid in self.patients:
            print("ID exists!")
            return
        self.patients[pid] = {
            'name': input("Name: "),
            'age': input("Age: "),
            'gender': input("Gender: "),
            'contact': input("Contact: "),
            'medical_history': [],
            'visits': []
        }
        self.save_data()
        print("Patient added!")
    
    def view_patient(self):
        pid = input("Enter Patient ID: ")
        patient = self.patients.get(pid)
        if not patient:
            print("Not found!")
            return
        print(f"\n--- Patient {pid} ---")
        for key, value in patient.items():
            if key not in ['medical_history', 'visits']:
                print(f"{key}: {value}")
    
    def update_patient(self):
        pid = input("Enter Patient ID: ")
        if pid not in self.patients:
            print("Not found!")
            return
        field = input("Field to update (name/age/gender/contact): ")
        if field in self.patients[pid]:
            self.patients[pid][field] = input(f"New {field}: ")
            self.save_data()
            print("Updated!")
    
    def delete_patient(self):
        pid = input("Enter Patient ID to delete: ")
        if pid in self.patients:
            del self.patients[pid]
            self.save_data()
            print("Deleted!")
        else:
            print("Not found!")
    
    def list_patients(self):
        print("\n--- All Patients ---")
        for pid, data in self.patients.items():
            print(f"{pid}: {data['name']} ({data['age']})")
    
    def add_medical_record(self):
        pid = input("Patient ID: ")
        if pid not in self.patients:
            print("Not found!")
            return
        condition = input("Medical condition: ")
        self.patients[pid]['medical_history'].append({
            'condition': condition,
            'date': datetime.now().strftime("%Y-%m-%d")
        })
        self.save_data()
        print("Record added!")
    
    def record_visit(self):
        pid = input("Patient ID: ")
        if pid not in self.patients:
            print("Not found!")
            return
        self.patients[pid]['visits'].append({
            'date': datetime.now().strftime("%Y-%m-%d"),
            'doctor': input("Doctor: "),
            'reason': input("Reason: ")
        })
        self.save_data()
        print("Visit recorded!")
    
    def search_patient(self):
        term = input("Search (name/ID): ").lower()
        found = False
        for pid, data in self.patients.items():
            if term in pid.lower() or term in data['name'].lower():
                print(f"{pid}: {data['name']} - {data['contact']}")
                found = True
        if not found:
            print("No matches!")

def main():
    manager = PatientRecordManager()
    while True:
        print("\n" + "="*40)
        print("   HOSPITAL RECORD MANAGER")
        print("="*40)
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. List All Patients")
        print("6. Add Medical Record")
        print("7. Record Visit")
        print("8. Search Patient")
        print("9. Exit")
        
        choice = input("Choose option (1-9): ")
        
        if choice == '1': manager.add_patient()
        elif choice == '2': manager.view_patient()
        elif choice == '3': manager.update_patient()
        elif choice == '4': manager.delete_patient()
        elif choice == '5': manager.list_patients()
        elif choice == '6': manager.add_medical_record()
        elif choice == '7': manager.record_visit()
        elif choice == '8': manager.search_patient()
        elif choice == '9': 
            print("Goodbye!")
            break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()