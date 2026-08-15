import os
from dotenv import load_dotenv
from retell import Retell

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
    
    client = Retell(
        api_key=api_key
)
        

    print("Pretty Good AI patient bot starting...")
    print("Retell API key loaded successfully!")
    print(f"Calling from: {from_number}")
    print(f"Assessment number: {test_number}")
    print("Connecting to Retell...")

    try:
        call = client.call.create_phone_call(
            from_number=from_number,
            to_number=test_number,
        )

        print("Call initiated successfully!")
        print(f"Call ID: {call.call_id}")

    except Exception as error:
        print(f"ERROR starting call: {error}")

if __name__ == "__main__":
    main()