from zxcvbn import zxcvbn


def analyze_password(password):
    """
    Analyze password strength using zxcvbn.
    Returns a dictionary with password details.
    """

    result = zxcvbn(password)

    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    return {
        "score": result["score"],
        "strength": levels[result["score"]],
        "warning": result["feedback"]["warning"],
        "suggestions": result["feedback"]["suggestions"],
        "crack_time": result["crack_times_display"]["offline_fast_hashing_1e10_per_second"]
    }



# Test this file directly

if __name__ == "__main__":

    password = input("Enter Password: ")

    report = analyze_password(password)

    print("\n------ PASSWORD REPORT ------")

    print("Score      :", report["score"], "/4")
    print("Strength   :", report["strength"])
    print("Crack Time :", report["crack_time"])

    if report["warning"]:
        print("\nWarning:")
        print(report["warning"])

    if report["suggestions"]:
        print("\nSuggestions:")
        for suggestion in report["suggestions"]:
            print("•", suggestion)