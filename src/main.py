
from data_analysis import analyse_data
from api_data import fetch_api_data

def main():

    print("================================")
    print(" PYTHON DATA & APIs APPLICATION")
    print("================================")

    print("\n1. Starting Data Analysis...")
    analyse_data()

    print("\n2. Connecting to REST API...")
    fetch_api_data()

    print("\n================================")
    print(" PROJECT COMPLETED SUCCESSFULLY")
    print("================================")

if __name__ == "__main__":
    main()
