def search_by_disease(patients, disease):
    result = []  
    for p in patients:
        if p["Disease"] == disease:
            result.append(p["Name"])
    return result

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

res = search_by_disease(patients, search_disease)

print("Patients with", search_disease, ":", res)
