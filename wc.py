# This Python program prints a personal profile to the console.

def personal_profile():
    name = "官育安"
    age = 19  # Replace with your age
    profession = "no"
    hobbies = ["sadge"]  # Replace with your hobbies

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Profession: {profession}")
    print("Hobbies:")
    for hobby in hobbies:
        print(f" - {hobby}")

if __name__ == "__main__":
    personal_profile()