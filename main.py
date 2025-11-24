complaints = []   # In-memory storage
next_id = 1       # Auto-increment complaint ID


# -------------------------------
# USER SIDE FUNCTIONS
# -------------------------------
def register_complaint():
    global next_id

    print("\n--- Register a Complaint ---")
    title = input("Enter Title: ")
    description = input("Enter Description: ")
    category = input("Enter Category (hostel/electric/water/cleanliness/mess-food/dispute/wifi/classroom/room maintainance/security/any other): ")
    priority = input("Enter Priority (Low/Medium/High): ")
    raised_by = input("Your Name: ")
    registeration_number = input("Your Registration Number: ")

    complaint = {
        "id": next_id,
        "title": title,
        "description": description,
        "category": category,
        "priority": priority,
        "status": "Pending",
        "raised_by": raised_by,
        "registration_number": registeration_number,
        "remarks": []
    }

    complaints.append(complaint)
    print(f"\nComplaint Registered Successfully! Complaint ID = {next_id}\n")
    next_id += 1


def view_my_complaints():
    name = input("\nEnter your name to view your complaints: ")
    registration_no = input("Enter your registration number: ")

    print(f"\n--- Complaints Raised by {name},{registration_no} ---")
    found = False
    for c in complaints:
        if c["raised_by"].lower() == name.lower() and c["registration_number"] == registration_no:
            found = True
            print(f"\nComplaint ID: {c['id']}")
            print(f"Title: {c['title']}")
            print(f"Category: {c['category']}")
            print(f"Status: {c['status']}")
            print(f"Remarks: {c['remarks']}")
    if not found:
        print("No complaints found.")


# -------------------------------
# ADMIN SIDE FUNCTIONS
# -------------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"   # Only for running program (no file)


def admin_login():
    print("\n--- Admin Login ---")
    user = input("Username: ")
    pw = input("Password: ")

    if user == ADMIN_USERNAME and pw == ADMIN_PASSWORD:
        print("Admin Login Successful!")
        return True
    else:
        print("Incorrect Username or Password!")
        return False


def view_all_complaints():
    print("\n--- All Complaints ---")
    if not complaints:
        print("No complaints available.")
        return

    for c in complaints:
        print(f"\nComplaint ID: {c['id']}")
        print(f"Title: {c['title']}")
        print(f"Category: {c['category']}")
        print(f"Priority: {c['priority']}")
        print(f"Status: {c['status']}")
        print(f"Raised By: {c['raised_by']}")
        print(f"Registration Number: {c['registration_number']}")
        print(f"Remarks: {c['remarks']}")


def update_status():
    cid = int(input("\nEnter Complaint ID to update: "))
    for c in complaints:
        if c["id"] == cid:
            print("\n1. Pending\n2. In-Progress\n3. Resolved")
            choice = input("Choose new status: ")

            if choice == "1":
                c["status"] = "Pending"
            elif choice == "2":
                c["status"] = "In-Progress"
            elif choice == "3":
                c["status"] = "Resolved"
            else:
                print("Invalid option")
                return

            print("Status updated successfully!")
            return

    print("Complaint ID not found!")


def add_remark():
    cid = int(input("\nEnter Complaint ID to add remark: "))
    for c in complaints:
        if c["id"] == cid:
            remark = input("Enter remark: ")
            c["remarks"].append(remark)
            print("Remark added successfully!")
            return

    print("Complaint ID not found!")


# -------------------------------
# ANALYTICS
# -------------------------------
def analytics():
    print("\n--- Complaint Analytics ---")

    total = len(complaints)
    pending = sum(1 for c in complaints if c["status"] == "Pending")
    resolved = sum(1 for c in complaints if c["status"] == "Resolved")

    print(f"Total Complaints: {total}")
    print(f"Pending: {pending}")
    print(f"Resolved: {resolved}")


# -------------------------------
# MAIN MENU
# -------------------------------
def main_menu():
    while True:
        print("\n=== Smart Campus Complaint System ===")
        print("1. Register a Complaint")
        print("2. View My Complaints")
        print("3. Admin Login")
        print("4. Analytics")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_complaint()
        elif choice == "2":
            view_my_complaints()
        elif choice == "3":
            if admin_login():
                admin_menu()
        elif choice == "4":
            analytics()
        elif choice == "0":
            print("Program Ended. All data erased.")
            break
        else:
            print("Invalid choice!")


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View All Complaints")
        print("2. Update Complaint Status")
        print("3. Add Remark")
        print("0. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_all_complaints()
        elif choice == "2":
            update_status()
        elif choice == "3":
            add_remark()
        elif choice == "0":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice!")


# -------------------------------
# RUN PROGRAM
# -------------------------------
main_menu()
