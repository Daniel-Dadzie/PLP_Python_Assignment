# Ubuntu Image Fetcher

A simple Python tool that **mindfully collects images from the web** while respecting Ubuntu principles of **Community, Respect, Sharing, and Practicality**.

This script allows users to fetch an image from a given URL, store it locally in a dedicated folder, and handle errors gracefully.

---

## ✨ Features
- Prompts the user for an image URL
- Creates a directory called **Fetched_Images** (if it doesn’t already exist)
- Downloads the image and saves it with an appropriate filename
- Handles connection and HTTP errors gracefully
- Default fallback filename if none is provided in the URL

---

## 🛠 Requirements
- Python 3.7+
- `requests` library

Install dependencies:
```bash
pip install requests
🚀 Usage
Clone this repository:

bash
Copy code
git clone https://github.com/Daniel-Dadzie/Ubuntu_Requests.git
cd Ubuntu_Requests
Run the script:

bash
Copy code
python3 fetch_image.py
Enter an image URL when prompted:

arduino
Copy code
Please enter the image URL: https://example.com/sample.jpg
Your image will be saved in the Fetched_Images directory.

📂 Project Structure
bash
Copy code
Ubuntu_Requests/
│── fetch_image.py   # Main script
│── README.md        # Project documentation
└── Fetched_Images/  # Downloaded images (created at runtime)
⚠️ Error Handling
Network issues → handled with requests.exceptions.RequestException

Invalid URLs or empty filenames → fallback filename: downloaded_image.jpg

Other exceptions → caught and printed without crashing

🔒 Precautions
Always verify the source of URLs before downloading files

Script checks for failed requests and won’t save incomplete files

Can be extended to check Content-Type headers before saving

🌍 Ubuntu Principles
Community: Connects users to the wider web

Respect: Handles errors without crashing

Sharing: Stores images in an organized folder for later use

Practicality: A lightweight, real-world tool for everyday use

📝 Future Improvements
Support multiple URLs at once

Prevent duplicate downloads

Validate Content-Type header to confirm it’s an image

Add logging for better tracking

👨‍💻 Author
Daniel Yaw Dadzie
 

