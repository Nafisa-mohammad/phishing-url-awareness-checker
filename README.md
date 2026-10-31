# EWB Phishing URL Awareness Checker

## 1. Project Overview

The **Phishing URL Awareness Checker** is a beginner-friendly cybersecurity mini-project developed using Python. The main purpose of this project is to identify selected warning signs in a URL that may indicate a suspicious or potentially misleading link.

Phishing is a type of cyberattack in which attackers create fake websites, emails, or messages to trick users into sharing sensitive information. This information may include usernames, passwords, banking details, and other personal data.

Attackers sometimes use misleading URLs to make fake websites appear similar to genuine websites. Therefore, checking the visible structure of a URL before trusting a link is an important cybersecurity awareness practice.

This project provides a simple command-line tool that accepts a URL as text, examines its structure, checks for six selected warning signs, and displays the findings to the user.

**Important:** This program only analyzes the text entered by the user. It does not open websites, visit URLs, communicate with external servers, or download any content.

## 2. Project Objectives

The main objectives of this project are:

- To understand basic phishing techniques and suspicious URL characteristics.
- To develop a simple cybersecurity awareness tool using Python.
- To identify selected warning signs commonly associated with suspicious URLs.
- To understand URL parsing and regular expressions.
- To practice Python functions, conditional statements, lists, and user input.
- To display understandable warning messages to users.
- To encourage users to examine links carefully before sharing sensitive information.

## 3. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python | Programming language used to develop the application. |
| Visual Studio Code | Code editor used to write and execute the program. |
| `re` module | Used for regular expression pattern matching. |
| `urllib.parse` module | Used to parse URLs and extract their components. |
| Git | Version control for tracking project changes. |
| GitHub | Used to publish and share the completed project. |

The project uses Python's built-in modules. Therefore, no additional Python packages or API keys are required.

## 4. Program Requirements

- Python version 3.10 or later.
- Visual Studio Code or another Python-compatible code editor.
- Windows, Linux, or macOS operating system.
- Basic knowledge of running Python programs.

## 5. Working of the Program

The program follows a simple sequence of operations to inspect the URL entered by the user.

### Step 1: Importing Required Modules

The program begins by importing two Python modules.

**1. `re` module**

The `re` module provides regular expression functionality. It is used to identify whether the hostname follows an IPv4-style address pattern.

**2. `urlparse` from `urllib.parse`**

The `urlparse` function separates a URL into different components, such as:

- Scheme (HTTP or HTTPS)
- Hostname (website domain or IP address)
- Path (specific location or resource on the website)

These components help the program examine the URL structure.

### Step 2: Defining the URL Inspection Function

The program contains a function named `inspect_url(raw_url)`.

This function is responsible for checking the entered URL for the selected warning signs.

It performs the following operations:

- Receives the URL entered by the user.
- Removes unnecessary spaces using the `strip()` function.
- Creates an empty list named `findings` to store detected warning messages.
- Checks whether the user has entered an empty URL.
- Prepares the URL for parsing.

If the URL does not contain a scheme, the program temporarily adds `http://` so that the URL can be parsed.

### Step 3: Extracting the Hostname

The program uses `urlparse()` to separate the URL into its components.

It then extracts the hostname using the `hostname` attribute.

The hostname represents the domain name or IP address specified in the URL.

The program converts the hostname to lowercase using `lower()` so that checks are not affected by uppercase or lowercase letters.

### Step 4: Checking the Six Warning Signs

The program performs six checks on the entered URL.

#### 1. Presence of the @ Symbol

The program checks whether the URL contains the `@` symbol.

Why is this important?

In a URL, the `@` symbol can separate user information from the hostname. Attackers may use it to make a URL appear as though it belongs to a familiar website.

For example:

`http://example.com@sample.invalid/login`

The actual hostname in this example is `sample.invalid`, not `example.com`.

The program displays a warning if it detects the `@` symbol.

#### 2. URL Length Greater Than 100 Characters

The program checks the length of the entered URL using Python's `len()` function.

If the URL contains more than 100 characters, it displays a warning.

Why is this important?

Some suspicious URLs use long and complicated text to hide misleading information or make their actual destination less obvious.

However, a long URL is not automatically malicious.

#### 3. IP Address Instead of a Familiar Domain Name

The program uses a regular expression to identify an IPv4-style hostname.

The regular expression used is:

`(?:\d{1,3}\.){3}\d{1,3}`

Explanation:

- `\d` represents a digit.
- `{1,3}` means one to three digits.
- `\.` represents a dot.
- The pattern identifies four groups of digits separated by dots.

Example:

`http://192.0.2.10/account`

The program identifies that the hostname is written as an IP address instead of a familiar domain name and displays a warning.

Note: This pattern checks the general IPv4-style format. It does not fully validate whether every numerical group is within the valid IPv4 range.

#### 4. Five or More Hostname Segments

The program divides the hostname into separate parts using the `split(".")` method.

These parts are called hostname labels.

For example:

`a.b.c.d.e.example.invalid`

The hostname contains seven labels separated by dots.

If the hostname contains five or more labels, the program displays a warning.

Why is this important?

A hostname containing many subdomains or segments may make a URL more complicated and difficult for users to understand.

However, legitimate websites can also have multiple subdomains.

#### 5. Presence of the Punycode Marker

The program checks whether the hostname contains the text `xn--`.

Punycode is a method used to represent internationalized domain names using ASCII-compatible characters.

Some attackers may misuse similar-looking characters in domain names to create misleading website addresses.

For this reason, the program displays a warning when it identifies the `xn--` marker.

The presence of Punycode does not automatically mean that a domain is malicious.

#### 6. Use of HTTP Instead of HTTPS

The program checks the URL scheme using the `scheme` attribute of the parsed URL.

If the scheme is `http`, the program displays a warning.

**Difference between HTTP and HTTPS:**

- HTTP stands for Hypertext Transfer Protocol.
- HTTPS stands for Hypertext Transfer Protocol Secure.
- HTTPS uses encryption through TLS to protect data exchanged between the browser and website.

HTTPS provides a protected connection, but it does not guarantee that a website is genuine or trustworthy.

Therefore, users should not trust a website only because it uses HTTPS.

### Step 5: Storing the Findings

Whenever the program identifies a warning sign, it adds a corresponding message to the `findings` list using the `append()` method.

This allows the program to collect multiple warning signs from a single URL.

For example, a URL may contain both an IP address and HTTP.

In that situation, the program stores and displays both warning messages.

### Step 6: Handling URLs Without Listed Warning Signs

After completing all six checks, the program examines whether the `findings` list is empty.

If no warning signs are identified, the program displays:

`No listed warning signs found. This does NOT prove safety.`

This message is important because the program checks only six selected characteristics.

A phishing URL may still exist without containing any of these warning signs.

### Step 7: Displaying the Results

The program uses a function named `main()` to control the execution.

The function:

1. Displays the project title.
2. Displays a message explaining that the program performs text-only checks.
3. Accepts a URL from the user using `input()`.
4. Calls the `inspect_url()` function.
5. Displays all the findings using a `for` loop.
6. Displays a final cybersecurity awareness message.

The following condition is used at the end of the program:

`if __name__ == "__main__":`

It ensures that the `main()` function is executed when the Python file is run directly.

## 6. Six Warning Signs at a Glance

| No. | Warning Sign | Detection Method |
|---|---|---|
| 1 | Presence of @ symbol | Checks for `@` in the URL text. |
| 2 | URL length over 100 characters | Uses `len()` to calculate URL length. |
| 3 | IP address hostname | Uses regular expression matching. |
| 4 | Five or more hostname labels | Splits hostname using dots and counts the labels. |
| 5 | Punycode marker | Checks for `xn--` in the hostname. |
| 6 | HTTP scheme | Checks the parsed URL scheme. |

## 7. Project Structure

The project is organized into the following files and folders:


phishing-url-awareness/
│
├── phishing_checker.py
│
├── README.md
│
├── requirements.txt
│
├── tests/
│   └── test_samples.md
│
└── screenshots/
    ├── sample_run.png
    └── test_results.png


**File descriptions:**

- `phishing_checker.py`: Contains the main Python program and URL inspection logic.
- `README.md`: Provides project information, working explanation, setup instructions, and documentation.
- `requirements.txt`: Specifies the external package requirements. No additional packages are needed.
- `tests/test_samples.md`: Documents the sample URLs, expected results, actual results, and testing status.
- `screenshots/`: Stores screenshots showing program execution and test results.

## 8. How to Run the Project

Follow these steps to execute the application.

**Step 1:** Install Python 3.10 or later.

**Step 2:** Download or clone this GitHub repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the integrated terminal.

**Step 5:** Execute the following command:

```bash
python phishing_checker.py
```

**Step 6:** Enter a sample URL when the program requests input.

**Step 7:** Read the warning messages displayed in the terminal.

## 9. Sample Program Execution

**Input URL:**

`http://192.0.2.10/account`

**Output:**

```text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.
Enter a sample URL to inspect: http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

Never enter passwords from unexpected links.
```

**Explanation:**

In this example, the program identifies two warning signs:

1. The hostname is an IP address instead of a familiar domain name.
2. The URL uses HTTP instead of HTTPS.

Both findings are displayed to the user.

## 10. Testing and Verification

The program was tested manually using the sample URLs specified in the project workbook and an additional long-URL test.

The testing process verifies whether each warning-sign condition produces the expected output.

The test results are documented in:

`tests/test_samples.md`

The program successfully displayed the expected warning messages during the initial testing.

## 11. Project Improvements

Additional improvements will be documented here after they have been implemented and tested.

The final version will describe:

- What additional functionality was introduced.
- Why the improvements were needed.
- How the updated program was tested.

## 12. Limitations of the Project

Although the project identifies selected URL warning signs, it has some limitations:

1. It checks only six predefined URL characteristics.
2. It does not visit or access the entered website.
3. It does not check website reputation or domain registration information.
4. It does not detect malware or malicious website content.
5. It may not identify phishing URLs that do not contain the selected warning signs.
6. A URL without detected warning signs is not necessarily safe.
7. A legitimate website may also contain one or more of the listed warning signs.

Therefore, this application should be considered an educational URL awareness tool, not a complete phishing detection system.

## 13. Ethical and Safe Usage

This project is developed for educational and cybersecurity awareness purposes.

The following safety practices are followed:

- Only sample URLs are used for testing.
- The program examines URL text without visiting websites.
- No passwords or confidential information are collected.
- No network requests are made.
- The tool is not used to deceive users or conduct unauthorized testing.

Users should always verify the actual website address before entering personal or financial information.

## 14. Conclusion

The Phishing URL Awareness Checker demonstrates how Python programming can be applied to a basic cybersecurity problem.

Through this project, we learned how to accept user input, parse URLs, use regular expressions, apply conditional statements, work with lists, and display meaningful results.

The project also demonstrates the importance of understanding suspicious URL characteristics and following safe browsing practices.

Although the tool cannot detect every phishing attack, it provides a simple introduction to URL inspection and phishing awareness.