classes = [["Alice", "Ben"], ["Chloe", "David"]]

for class_number, classroom in enumerate(classes, start=1):
    print(f"\nClass {class_number}")

    for student in classroom:
        print(f"Student: {student}")
