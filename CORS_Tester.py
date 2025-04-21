import requests
import argparse

def test_cors(target_url, method, output_file=None):
    test_origins = [
        "https://evil.com",
        "null",
        "http://localhost",
        "https://subdomain.example.com",
        target_url,
    ]

    results = []
    print(f"[*] Testing CORS on: {target_url} using {method} method\n")

    for origin in test_origins:
        headers = {
            "Origin": origin
        }

        try:
            if method == "GET":
                response = requests.get(target_url, headers=headers, timeout=10)
            elif method == "POST":
                response = requests.post(target_url, headers=headers, data={}, timeout=10)

            acao = response.headers.get("Access-Control-Allow-Origin")
            acac = response.headers.get("Access-Control-Allow-Credentials")

            result = f"Origin: {origin}\n"
            if acao:
                result += f"  [+] Access-Control-Allow-Origin: {acao}\n"
            else:
                result += f"  [-] No ACAO header in response\n"

            if acac:
                result += f"  [+] Access-Control-Allow-Credentials: {acac}\n"

            result += "-" * 40
            print(result)
            results.append(result)

        except Exception as e:
            err_msg = f"[!] Error testing origin {origin}: {e}"
            print(err_msg)
            results.append(err_msg)

    if output_file:
        with open(output_file, "w") as f:
            f.write("\n".join(results))
        print(f"\n[+] Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CORS Misconfiguration Tester")
    parser.add_argument("url", help="Target URL to test")
    parser.add_argument("-m", "--method", choices=["GET", "POST"], default="GET", help="HTTP method to use")
    parser.add_argument("-o", "--output", help="File to save the output")

    args = parser.parse_args()

    test_cors(args.url, args.method, args.output)
