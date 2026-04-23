# My Hacking Journey: From Curiosity to Code

## Introduction

This document chronicles my journey into the world of cybersecurity and ethical hacking. It's a space to track my learning, experiments, and projects as I delve deeper into understanding how systems work, how they can be secured, and yes, how they can be (ethically) probed.

My goal is not to cause harm, but to learn, build, and contribute to a more secure digital world. This is about understanding vulnerabilities to build stronger defenses.

## Getting Started: The Fundamentals

Before diving into complex exploits, I'm focusing on the foundational building blocks.

### Core Concepts I'm Learning:

*   **Networking:** How data travels, TCP/IP, DNS, ports, protocols (HTTP, HTTPS, SSH).
*   **Operating Systems:** Linux (especially command-line interface), Windows internals.
*   **Programming Languages:**
    *   **Python:** My primary tool for scripting, automation, and building small utilities. Essential for custom tools and exploit development.
    *   **Bash Scripting:** For automating tasks on Linux systems.
    *   *(Future: JavaScript for web app understanding, C/C++ for lower-level concepts)*
*   **Web Technologies:** HTML, CSS, JavaScript, how web servers work, common web vulnerabilities (XSS, SQL Injection - theoretical for now).

## My First Project: The Login Server & Brute-Force Test

This is where my journey truly began in practice. I wanted to understand how authentication works and how a simple password protection could be bypassed.

### Project Overview:

1.  **Building a Basic Flask Login Server:**
    *   **Goal:** To create a simple web server that accepts username and password via POST requests.
    *   **Tech:** Python, Flask.
    *   **Learning:** Setting up a web server, handling routes, receiving POST data, basic JSON handling.

2.  **Enhancing to a Functional Login Server:**
    *   **Goal:** To add actual (though simple) credential validation.
    *   **Tech:** Python, Flask, a hardcoded user dictionary.
    *   **Learning:** Storing credentials (even if basic), comparing inputs, returning different HTTP status codes (200 OK, 401 Unauthorized).

3.  **Creating a Password Testing Script:**
    *   **Goal:** To write a client-side script that attempts to guess passwords from a list against the login server.
    *   **Tech:** Python, `requests` library.
    *   **Learning:** Making HTTP requests from a script, iterating through files, parsing server responses, understanding common pitfalls in client-side scripting.

### Key Takeaways from Project 1:

*   **Server-Side Logic is Crucial:** The security of the login process relies heavily on how the server validates credentials, not just on the client-side attempt.
*   **Client-Side vs. Server-Side:** I learned to differentiate between the client making requests and the server processing them.
*   **The Importance of Good Error Handling:** Both on the server (to give appropriate feedback) and on the client (to correctly interpret responses and handle network issues).
*   **Ethical Boundaries:** This exercise reinforced that testing systems requires permission and a focus on learning, not exploitation.

## Tools I'm Using:

*   **Code Editor:** VS Code (with Python, Jinja, and other relevant extensions)
*   **Terminal:** Integrated terminal in VS Code, iTerm2 (macOS)
*   **Python Environment:** Virtual environments (`venv`)
*   **Version Control:** Git & GitHub (for tracking progress and collaboration)
*   **Testing Utilities:** `curl` (for manual API testing), Python `requests` library.

## Next Steps & Future Explorations:

*   **Deeper Dive into Web Vulnerabilities:** Exploring OWASP Top 10 (SQLi, XSS, CSRF, etc.) with practical labs.
*   **Network Scanning:** Learning tools like Nmap.
*   **More Advanced Python Scripting:** Automating more complex tasks, interacting with APIs.
*   **Capture The Flag (CTF) Challenges:** Participating in beginner-friendly CTFs to apply learned skills in simulated environments.
*   **Cryptography Basics:** Understanding encryption, hashing, and their role in security.

## Ethical Hacking Manifesto:

I commit to using my skills responsibly and ethically.
*   I will always seek explicit permission before testing any system.
*   I will not cause harm, disruption, or data loss.
*   My goal is to learn, improve security, and share knowledge constructively.
*   I understand that unauthorized access is illegal and unethical.

---

*(This document will be updated as my journey progresses!)*
