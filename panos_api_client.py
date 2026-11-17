class PANOSClient:
    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key

    def get_system_info(self):
        print(f"Querying PAN-OS System Information from https://{self.host}/api...")
        return {"model": "PA-VM", "uptime": "45 days", "version": "10.2.3"}

if __name__ == "__main__":
    client = PANOSClient("192.168.1.254", "mock_key")
    print(client.get_system_info())
