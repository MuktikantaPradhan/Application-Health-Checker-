import requests
import time

def check_application_status(url, timeout=5):
   
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        elapsed_time = time.time() - start_time
        if response.status_code == 200:
            return f"Application is up. Response time: {elapsed_time:.2f} seconds."
        else:
            return f"Application is up, but returned a non-200 status code: {response.status_code}."
    except requests.exceptions.RequestException as e:
        return f"Application is down. Error: {str(e)}."

if __name__ == "__main__":
    url = input("Enter the URL of the application to check: ")
    print(check_application_status(url))