import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    api_key = os.getenv("RETELL_API_KEY")
    from_number = os.getenv("RETELL_FROM_NUMBER")
    test_number = os.getenv("PGAI_TEST_NUMBER")

    missing = []
    if not api_key:
        missing.append("RETELL_API_KEY")
    if not from_number:
        missing.append("RETELL_FROM_NUMBER")
    if not test_number:
        missing.append("PGAI_TEST_NUMBER")

    if missing:
        print(f"ERROR: Missing environment variable(s): {', '.join(missing)}")
        return

    print("Pretty Good AI patient bot starting...")
    print("Retell API key loaded successfully!")
    print(f"Calling from: {from_number}")
    print(f"Assessment number: {test_number}")


if __name__ == "__main__":
    main()