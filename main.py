from analyzer import analyze_password
from generator import generate_password


def check_generated_password():

    password = generate_password(12)

    print("\nGenerated Password:")
    print(password)

    result = analyze_password(password)

    print("\nPassword Analysis:")
    print("------------------")

    print("Score:", result["score"])
    print("Strength:", result["strength"])
    print("Crack Time:", result["crack_time"])

    print("\nSuggestions:")

    for suggestion in result["suggestions"]:
        print("-", suggestion)



if __name__ == "__main__":

    print("Password Strength Analyzer")
    print("========================")

    choice = input(
        "\n1. Analyze your password\n2. Generate strong password\n\nEnter choice: "
    )


    if choice == "1":

        password = input("\nEnter password: ")

        result = analyze_password(password)

        print("\nAnalysis Result")
        print("----------------")
        print("Score:", result["score"])
        print("Strength:", result["strength"])
        print("Crack Time:", result["crack_time"])

        print("\nSuggestions:")
        for suggestion in result["suggestions"]:
            print("-", suggestion)



    elif choice == "2":

        check_generated_password()


    else:
        print("Invalid choice")