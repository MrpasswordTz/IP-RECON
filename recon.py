import requests
import pyfiglet
import os
from colorama import Fore, init

results = " === Show Information IP ADDRESS ===\n"
logo = pyfiglet.figlet_format('IP-RECON')
def get_ip_info(ip_address, api_key):
    url = f"https://geo.ipify.org/api/v2/country,city,vpn?apiKey={api_key}&ipAddress={ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def print_ip_info(data):
    print("Target IP:", data.get("ip", "False"))
    
    print("Country:", data.get("location", {}).get("country", "False"))
    
    print("Region:", data.get("location", {}).get("region", "False"))
    
    print("City:", data.get("location", {}).get("city", "False"))
    
    print("Postal Code:", data.get("location", {}).get("postalCode", "False"))
    
    print("Timezone:", data.get("location", {}).get("timezone", "False"))
    
    print("Geoname ID:", data.get("location", {}).get("geonameId", "False"))
    
    print("ASN:", data.get("as", {}).get("asn", "False"))
    
    print("ASN Name:", data.get("as", {}).get("name", "False"))
    
    print("ASN Route:", data.get("as", {}).get("route", "False"))
    
    print("ASN Domain:", data.get("as", {}).get("domain", "False"))
    
    print("ASN Type:", data.get("as", {}).get("type", "False"))
    
    print("ISP:", data.get("isp", "False"))
    
    print("Proxy:", data.get("proxy", {}).get("proxy", "False"))
    
    print("VPN:", data.get("proxy", {}).get("vpn", "False"))
    
    print("TOR:", data.get("proxy", {}).get("tor", "False"))
    
    lat = data.get("location", {}).get("lat", "False")
    
    lon = data.get("location", {}).get("lng", "False")
    
    print("Location.:", f"{lat}, {lon}")
    print("Google Maps Link:", f"https://www.google.com/maps/@?api=1&map_action=map&center={lat},{lon}&zoom=20")
    
    country_name = data.get("location", {}).get("country", "False")
    

def main():
    api_key = "at_BFePrsj5R5xI9sPpoYQarq8SxwHib"
    print(Fore.CYAN + logo + Fore.RESET)
    print('''Author: MrpasswordTz.             V1\n''')
    ip_address = input("Enter target IP address: ")
    print("\n")
    data = get_ip_info(ip_address, api_key)
    if data:
        print(Fore.GREEN + results+ Fore.RESET)
        print_ip_info(data)
    else:
        print(Fore.GREEN + results + Fore.RESET)
        print("Failed to retrieve IP address information")

if __name__ == "__main__":
    main()
