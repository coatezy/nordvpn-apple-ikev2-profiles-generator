import os
import json
import textwrap
import uuid
from urllib import request, error

def fetch_nordvpn_servers(api_url):
    try:
        response = request.urlopen(api_url)
        servers_data = json.loads(response.read().decode("utf-8"))
        return servers_data
    except error.URLError as e:
        print(f"Error fetching NordVPN servers: {e}")
        return None

def generate_mobileconfig(username, password, server, output_directory):
    vpn_name = server.get("name")
    vpn_domain = server.get("domain")

    # Generate new UUIDs
    payload_uuid = str(uuid.uuid4())
    main_payload_uuid = str(uuid.uuid4())

    # Prepare the XML content
    xml_content = textwrap.dedent(f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
          <dict>
            <key>PayloadContent</key>
            <array>
              <dict>
                <key>IKEv2</key>
                <dict>
                  <key>AuthName</key>
                  <string>{username}</string>
                  <key>AuthPassword</key>
                  <string>{password}</string>
                  <key>AuthenticationMethod</key>
                  <string>None</string>
                  <key>ChildSecurityAssociationParameters</key>
                  <dict>
                    <key>DiffieHellmanGroup</key>
                    <integer>20</integer>
                    <key>EncryptionAlgorithm</key>
                    <string>AES-256</string>
                    <key>IntegrityAlgorithm</key>
                    <string>SHA2-384</string>
                    <key>LifeTimeInMinutes</key>
                    <integer>1440</integer>
                  </dict>
                  <key>DeadPeerDetectionRate</key>
                  <string>Medium</string>
                  <key>DisableMOBIKE</key>
                  <integer>0</integer>
                  <key>DisableRedirect</key>
                  <integer>0</integer>
                  <key>EnableCertificateRevocationCheck</key>
                  <integer>0</integer>
                  <key>EnablePFS</key>
                  <true />
                  <key>ExtendedAuthEnabled</key>
                  <true />
                  <key>IKESecurityAssociationParameters</key>
                  <dict>
                    <key>DiffieHellmanGroup</key>
                    <integer>20</integer>
                    <key>EncryptionAlgorithm</key>
                    <string>AES-256-GCM</string>
                    <key>IntegrityAlgorithm</key>
                    <string>SHA2-384</string>
                    <key>LifeTimeInMinutes</key>
                    <integer>1440</integer>
                  </dict>
                  <key>RemoteAddress</key>
                  <string>{vpn_domain}</string>
                  <key>RemoteIdentifier</key>
                  <string>{vpn_domain}</string>
                  <key>UseConfigurationAttributeInternalIPSubnet</key>
                  <integer>0</integer>
                </dict>
                <key>PayloadDescription</key>
                <string>Configures VPN settings</string>
                <key>PayloadDisplayName</key>
                <string>VPN</string>
                <key>PayloadIdentifier</key>
                <string>com.apple.vpn.managed.{payload_uuid}</string>
                <key>PayloadType</key>
                <string>com.apple.vpn.managed</string>
                <key>PayloadUUID</key>
                <string>{payload_uuid}</string>
                <key>PayloadVersion</key>
                <integer>1</integer>
                <key>Proxies</key>
                <dict>
                  <key>HTTPEnable</key>
                  <integer>0</integer>
                  <key>HTTPSEnable</key>
                  <integer>0</integer>
                </dict>
                <key>UserDefinedName</key>
                <string>NordVPN - {vpn_name}</string>
                <key>VPNType</key>
                <string>IKEv2</string>
              </dict>
              <dict>
                <key>PayloadCertificateFileName</key>
                <string>root.der</string>
                <key>PayloadContent</key>
                <data>
                  MIIFCjCCAvKgAwIBAgIBATANBgkqhkiG9w0BAQ0FADA5MQswCQYDVQQGEwJQQTEQ
                  MA4GA1UEChMHTm9yZFZQTjEYMBYGA1UEAxMPTm9yZFZQTiBSb290IENBMB4XDTE2
                  MDEwMTAwMDAwMFoXDTM1MTIzMTIzNTk1OVowOTELMAkGA1UEBhMCUEExEDAOBgNV
                  BAoTB05vcmRWUE4xGDAWBgNVBAMTD05vcmRWUE4gUm9vdCBDQTCCAiIwDQYJKoZI
                  hvcNAQEBBQADggIPADCCAgoCggIBAMkr/BYhyo0F2upsIMXwC6QvkZps3NN2/eQF
                  kfQIS1gql0aejsKsEnmY0Kaon8uZCTXPsRH1gQNgg5D2gixdd1mJUvV3dE3y9FJr
                  XMoDkXdCGBodvKJyU6lcfEVF6/UxHcbBguZK9UtRHS9eJYm3rpL/5huQMCppX7kU
                  eQ8dpCwd3iKITqwd1ZudDqsWaU0vqzC2H55IyaZ/5/TnCk31Q1UP6BksbbuRcwOV
                  skEDsm6YoWDnn/IIzGOYnFJRzQH5jTz3j1QBvRIuQuBuvUkfhx1FEwhwZigrcxXu
                  MP+QgM54kezgziJUaZcOM2zF3lvrwMvXDMfNeIoJABv9ljw969xQ8czQCU5lMVmA
                  37ltv5Ec9U5hZuwk/9QO1Z+d/r6Jx0mlurS8gnCAKJgwa3kyZw6e4FZ8mYL4vpRR
                  hPdvRTWCMJkeB4yBHyhxUmTRgJHm6YR3D6hcFAc9cQcTEl/I60tMdz33G6m0O42s
                  Qt/+AR3YCY/RusWVBJB/qNS94EtNtj8iaebCQW1jHAhvGmFILVR9lzD0EzWKHkvy
                  WEjmUVRgCDd6Ne3eFRNS73gdv/C3l5boYySeu4exkEYVxVRn8DhCxs0MnkMHWFK6
                  MyzXCCn+JnWFDYPfDKHvpff/kLDobtPBf+Lbch5wQy9quY27xaj0XwLyjOltpiST
                  LWae/Q4vAgMBAAGjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgEGMA0GCSqG
                  SIb3DQEBDQUAA4ICAQC9fUL2sZPxIN2mD32VeNySTgZlCEdVmlq471o/bDMP4B8g
                  nQesFRtXY2ZCjs50Jm73B2LViL9qlREmI6vE5IC8IsRBJSV4ce1WYxyXro5rmVg/
                  k6a10rlsbK/eg//GHoJxDdXDOokLUSnxt7gk3QKpX6eCdh67p0PuWm/7WUJQxH2S
                  DxsT9vB/iZriTIEe/ILoOQF0Aqp7AgNCcLcLAmbxXQkXYCCSB35Vp06u+eTWjG0/
                  pyS5V14stGtw+fA0DJp5ZJV4eqJ5LqxMlYvEZ/qKTEdoCeaXv2QEmN6dVqjDoTAo
                  k0t5u4YRXzEVCfXAC3ocplNdtCA72wjFJcSbfif4BSC8bDACTXtnPC7nD0VndZLp
                  +RiNLeiENhk0oTC+UVdSc+n2nJOzkCK0vYu0Ads4JGIB7g8IB3z2t9ICmsWrgnhd
                  NdcOe15BincrGA8avQ1cWXsfIKEjbrnEuEk9b5jel6NfHtPKoHc9mDpRdNPISeVa
                  wDBM1mJChneHt59Nh8Gah74+TM1jBsw4fhJPvoc7Atcg740JErb904mZfkIEmojC
                  VPhBHVQ9LHBAdM8qFI2kRK0IynOmAZhexlP/aT/kpEsEPyaZQlnBn3An1CRz8h0S
                  PApL8PytggYKeQmRhl499+6jLxcZ2IegLfqq41dzIjwHwTMplg+1pKIOVojpWA==
                </data>
                <key>PayloadDescription</key>
                <string>CA-Stammzertifikat hinzufügen</string>
                <key>PayloadDisplayName</key>
                <string>NordVPN Root CA</string>
                <key>PayloadIdentifier</key>
                <string
                  >com.apple.security.root.8F5CE61E-1C3F-45AE-9A93-A38C05C566EA</string
                >
                <key>PayloadType</key>
                <string>com.apple.security.root</string>
                <key>PayloadUUID</key>
                <string>8F5CE61E-1C3F-45AE-9A93-A38C05C566EA</string>
                <key>PayloadVersion</key>
                <integer>1</integer>
              </dict>
            </array>
            <key>PayloadDisplayName</key>
            <string>IKEv2 VPN configuration ({vpn_domain})</string>
            <key>PayloadIdentifier</key>
            <string>com.artembrening.vpn.{main_payload_uuid}</string>
            <key>PayloadRemovalDisallowed</key>
            <false />
            <key>PayloadType</key>
            <string>Configuration</string>
            <key>PayloadUUID</key>
            <string>{main_payload_uuid}</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
          </dict>
        </plist>
    """)

    # Create directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Save to a .mobileconfig file
    file_path = os.path.join(output_directory, f"{vpn_domain}.mobileconfig")
    with open(file_path, "w") as file:
        file.write(xml_content)

    print(f"File saved to {file_path}")

def main():
    api_url = "https://nordvpn.com/api/server"
    nordvpn_servers = fetch_nordvpn_servers(api_url)

    if nordvpn_servers:
        username = input("NordVPN service username: ").strip()
        password = input("NordVPN service password: ").strip()

        if not username or not password:
            print("Both username and password are required.")
            return

        output_directory = input("Output Directory (or press Enter for default 'profiles'): ") or 'profiles'

        # Filter IKEv2 servers
        ikev2_servers = [server for server in nordvpn_servers if server.get("features", {}).get("ikev2", False)]

        # Sort the IKEv2 servers by name
        ikev2_servers.sort(key=lambda server: server.get("name"))

        # Generate configurations for IKEv2 servers
        for server in ikev2_servers:
            generate_mobileconfig(username, password, server, output_directory)

if __name__ == "__main__":
    main()
