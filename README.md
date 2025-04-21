## USE Option
## Advanced Usage

# Use POST instead of GET:
python cors_tester.py https://target.com -m POST
# CORS-Finder
Simple CORS misconfiguration tester in Python
#Save output to a file:
python cors_tester.py https://target.com -o result.txt 
# Example:
python cors_tester.py https://target.com -m POST -o cors_report.txt
