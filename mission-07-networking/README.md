# Mission 7 — How computers communicate

## 1. Task / objective
Explain key networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server), run safe connectivity and DNS lookup tests in Terminal against `example.com`, and describe step by step what happens when a user opens a website.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A Local Area Network connects devices within a small, single location so they can share files and internet access quickly. | Devices connected to a home Wi-Fi router or a college computer lab network. |
| **MAN** | A Metropolitan Area Network links multiple nearby LANs across a city or large campus. | High-speed fiber linking several buildings across a university campus or city offices. |
| **WAN** | A Wide Area Network spans large geographical regions, countries, or continents by connecting many smaller networks. | The global Internet or a bank's network connecting branches in different cities. |
| **DNS** | The Domain Name System works like a phonebook that translates human-readable website names into numeric IP addresses. | Translating `example.com` into IP addresses such as `104.20.23.154`. |
| **Router** | A networking device that connects separate networks and forwards data packets along paths toward their destination. | A home Wi-Fi router forwarding web requests between local devices and the ISP network. |
| **Protocol** | An agreed set of formatting and timing rules that devices follow so they can communicate reliably. | `HTTPS` for encrypted web pages or `ICMP` used by `ping`. |
| **Packet switching** | Breaking messages into small numbered packets that travel independently across the network and are reassembled at the destination. | Downloading a web page as small data packets routed across internet links. |
| **Client-server** | A communication model where a client device requests a resource or service and a server listens and sends back the response. | A web browser (client) requesting a page from GitHub's web server. |

---

### Task 7.2 — Observe network information
Ran `ping -c 3 example.com` and `nslookup example.com` in Terminal (local DNS resolver details redacted):
- `ping -c 3 example.com` sent 3 packets and received 3 replies (`0.0%` packet loss) with round-trip times between `5.452 ms` and `19.384 ms` (average `10.623 ms`).
- `nslookup example.com` returned the domain's public IPv4 addresses (`172.66.147.243` and `104.20.23.154`).

**Answers:**
- **What a connectivity test helps you check:** A connectivity test like `ping` checks whether your computer can reach a remote host over the network, whether packets are being lost along the way, and how long a round trip takes (latency).
- **What information a DNS lookup displays:** A DNS lookup shows which DNS resolver answered the query (redacted here for privacy) along with the domain name and the IP address(es) mapped to it.
- **Role of DNS when entering a website name in a browser:** Humans remember domain names like `example.com`, but network routing uses numeric IP addresses. DNS translates the typed domain name into the server's IP address so the browser knows where to send its request.

---

### Task 7.3 — What happens when you open a website?
1. **User enters a URL in the client:** You type `https://example.com` into your web browser, which acts as the **client** requesting a web page.
2. **DNS resolution:** Before the client can contact the website, it asks **DNS** to translate the domain name `example.com` into a numeric IP address (`104.20.23.154`).
3. **Packet routing across the network:** Your computer packages the connection setup request and sends it through your local **router** and internet service provider across networks toward the destination IP address.
4. **Protocol handshake and request:** Using standard communication **protocols** (TCP/TLS and HTTP/HTTPS), the client establishes a secure connection and sends an HTTP request asking the destination **server** for the page.
5. **Server processing:** The remote web **server** receives the request, locates or generates the requested HTML page and assets, and prepares a response.
6. **Response and display to the user:** The **server** sends the response back as packets across the network to the **client**, and the browser reassembles the data and renders the visible webpage on your screen.

## 3. Commands / tools used
- `ping -c 3 example.com` — Sent 3 ICMP echo requests to verify reachability, packet loss, and round-trip latency.
- `nslookup example.com` — Queried DNS to observe the IP addresses mapped to `example.com`.

## 4. My understanding
Opening a simple webpage relies on several layers working together: DNS translates names into IP addresses, routers forward packets across LANs and WANs, and standard protocols allow a client browser and a remote server to exchange requests and responses reliably.

## 5. Difficulties faced
No major difficulties. I needed to redact the DNS server IP printed by `nslookup` so no local network configuration details were published.

## 6. How I resolved them
Replaced the local DNS resolver address lines with `[redacted]` in the saved output while keeping the public `example.com` lookup and `ping` statistics.

## 7. Evidence / files
- [README.md](README.md) — Network concepts table, safe observations, and 6-step website communication flow.
- [../evidence/mission-07-network-output.txt](../evidence/mission-07-network-output.txt) — Redacted `ping` and `nslookup` output for `example.com`.

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Status:** Committed on `main` and pushed to GitHub.
