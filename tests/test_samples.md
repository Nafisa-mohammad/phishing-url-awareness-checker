
# Phishing URL Checker - Test Results

## Testing Environment

- Programming Language: Python
- Operating System: Windows
- Testing Method: Manual testing using sample URLs
- Network Access: Not used

## Test Cases
## Test Results

| Test | Sample URL | Expected Warning Count | Actual Warning Count | Status |
|---|---|---:|---:|---|
| 1 | https://www.example.com/login | 0 | 0 | PASS |
| 2 | http://192.0.2.10/account | 2 | 2 | PASS |
| 3 | http://example.com@sample.invalid/login | 2 | 2 | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | 1 | 1 | PASS |
| 5 | https://xn--example.invalid/ | 1 | 1 | PASS |

## Additional Improvements Tested

1. Multiple URL Checking:
   The program accepts multiple URLs without restarting.
   The user can type q to exit.

2. Warning Count:
   The program displays the total number of warning signs
   detected for each entered URL.

## Conclusion

The program performs the six specified URL text checks
and includes two additional improvements.

A zero-warning result does not guarantee that a URL is safe.

