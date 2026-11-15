# Mission 7 — How computers communicate

## 1. Task / objective
The objective of this mission is to explore how computer networks function by:
- Defining and providing examples of core networking models and concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server).
- Conducting privacy-safe network diagnostics from the terminal using connectivity tools (`ping`) and DNS lookup tools (`nslookup`).
- Explaining the end-to-end 5–7 step lifecycle of what occurs when a user accesses a website in a browser.

---

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
|---|---|---|
| **LAN** (Local Area Network) | A network interconnecting computing devices within a geographically limited area, offering high data-transfer rates. | A home Wi-Fi network connecting a laptop, smartphone, and smart TV; or a university computer lab. |
| **MAN** (Metropolitan Area Network) | A communication network spanning a larger geographical region than a LAN, typically covering an entire city, municipal area, or sprawling multi-campus facility. | A city-wide fiber optic network connecting municipal government offices, police stations, and public libraries. |
| **WAN** (Wide Area Network) | A telecommunications network spanning large geographical distances, connecting disparate local networks across states, nations, or continents. | The global Internet, connecting millions of private and public networks worldwide via transoceanic fiber cables. |
| **DNS** (Domain Name System) | The distributed directory service that translates human-friendly domain names into computer-routable IP addresses. | Translating `example.com` into the numeric IP address `104.20.23.154`. |
| **Router** | A specialized networking device that inspects destination IP addresses and forwards data packets across different subnets. | A home Wi-Fi gateway router forwarding outbound traffic from home devices to the Internet Service Provider (ISP). |
| **Protocol** | An agreed-upon set of standardized rules, syntax, and error-handling procedures governing how devices format and exchange data. | HTTP/HTTPS for web traffic, TCP for reliable packet delivery, and IP for network addressing. |
| **Packet switching** | A communication methodology where data messages are broken into individual chunks (packets) that travel independently along optimal paths before reassembly. | Transferring an image file over the Internet split into hundreds of TCP/IP packets routed across diverse paths. |
| **Client-server** | A distributed computing model where service requesters (clients) initiate requests, and centralized providers (servers) respond with resources or computation. | A web browser (client) requesting an HTML web page from an Apache or Nginx web server. |

---

### Task 7.2 — Observe network information
Network diagnostic tools were run against the public test domain `example.com`.

#### 1. Connectivity Test (`ping`):
```bash
ping -c 3 example.com
```
- **Observations:**
  - 3 packets transmitted, 3 packets received, **0.0% packet loss**.
  - Average round-trip time (RTT): **~5.01 ms**.
- **What a connectivity test helps you check:**
  A connectivity test verifies whether the local computer can establish basic network-layer communication with a remote host across routers and gateways, measures latency (how long it takes for a signal to travel back and forth), and detects packet loss indicating network congestion or dropouts.

#### 2. DNS Lookup (`nslookup`):
```bash
nslookup example.com
```
- **Observations:**
  - Non-authoritative answer returned IP addresses: `104.20.23.154` and `172.66.147.243`.
- **What information a DNS lookup displays:**
  A DNS lookup reveals which DNS resolver server handled the query, whether the response is authoritative, and most importantly, the corresponding IP addresses (A/AAAA records) bound to that domain name.
- **The role of DNS when you enter a website name in a browser:**
  Humans remember alphabetical domain names (e.g., `google.com`), but network routers exclusively route packets using numerical IP addresses. When a URL is entered, DNS immediately acts as a phonebook, resolving the domain into an IP address so the browser knows where to direct the connection.

*(Note: In compliance with privacy guidelines, local private network IP addresses and Wi-Fi SSIDs have been excluded.)*

---

### Task 7.3 — What happens when you open a website?

Here is the step-by-step process of what happens from the moment a user requests a website to when it renders:

1. **User Request & URL Parsing (Client):**
   The user types a URL (e.g. `https://example.com`) into the web browser (the client) and presses Enter. The browser parses the protocol (`https://`), domain name (`example.com`), and path.
2. **DNS Resolution (Domain Name System):**
   The client checks its local DNS cache. If not found, it queries the operating system resolver, home router, and ISP recursive DNS servers to translate `example.com` into its destination IP address (e.g., `104.20.23.154`).
3. **Establishing Connection via Protocols (TCP/TLS Handshake):**
   Using the resolved IP address, the client initiates a reliable connection across intermediate routers using the **TCP** (Transmission Control Protocol) 3-way handshake (`SYN`, `SYN-ACK`, `ACK`). For secure HTTPS, a **TLS** handshake negotiates cryptographic keys to encrypt subsequent communication.
4. **Packet Switching across the Network:**
   The connection request and subsequent data are segmented into discrete packets. Each packet contains source and destination IP headers. Network routers analyze these headers and dynamically forward the packets along optimal routes toward the target server.
5. **HTTP Request to the Server:**
   Once connected, the browser sends an HTTP `GET` request packet asking for the resource (e.g., `GET / HTTP/2`).
6. **Server Processing and Response:**
   The destination web server receives the request, processes it, retrieves required assets, and returns an HTTP response status code (e.g., `200 OK`) accompanied by the HTML, CSS, JavaScript, and image payloads.
7. **Client Rendering (Output Displayed to User):**
   The browser client receives the response packets, reassembles them, constructs the Document Object Model (DOM) and CSSOM, executes scripts, and renders the visual web page on the user's screen.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested network packet transmission, packet loss, and round-trip latency.
- `nslookup example.com`: Queried DNS servers to discover the IP addresses mapped to the domain.

---

## 4. My understanding
Computer networking relies on layered abstractions and modular protocols working in unison. Devices do not transmit whole files as single monoliths; instead, packet switching allows communication channels to be shared efficiently. DNS seamlessly decouples human-readable names from physical machine addresses, and standardized protocols (IP, TCP, HTTP) ensure interoperability across heterogeneous computers worldwide.

---

## 5. Difficulties faced
No major difficulties. Network connectivity was reliable and DNS resolution completed cleanly with zero packet loss.

---

## 6. How I resolved them
Not applicable.

---

## 7. Evidence / files
- `mission-07-networking/README.md`: This comprehensive report including networking tables, command outputs, and the 7-step website loading lifecycle.

---

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
