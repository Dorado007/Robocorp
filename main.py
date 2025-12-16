import requests
import sys

def main():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            print("La API no devolvió resultado exitoso")
            print(data)
            sys.exit(1)

        rate = data["rates"]["COP"]
        print(f"USD - COP: {rate}")

    except Exception as e:
        print("ERROR ejecutando el robot:")
        print(str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
