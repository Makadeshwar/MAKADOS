# MAKADOS

**MAKADOS BY MAKADESHWAR** is an advanced HTTP DoS tool written in Python 3.
###### MAKE SURE YOU YOUSE THIS TOOL ETHICALLY AND DONT EXPLOIT IT 
###### WHOEVER USES THIS TOOL IS RESPONSIBLE FOR OF THERE OWN
It features GET/POST flooding, proxy rotation, Tor support, multithreading, logging, and silent mode.

---

## 🚀 Features

- GET and POST attack support
- Multi-threaded (default 1000 threads)
- Proxy rotation support
- Tor routing support (`torsocks`)
- Logging requests to file
- Silent output mode

---

## 🛠️ Usage

### Example Commands:

- Basic GET attack:
  ```bash
- python3 MAKADOS.py https://target.com
### Post attack 

- python3 MAKADOS.py https://target.com --post

### USING PROXIES
 
- python3 MAKADOS.py https://target.com --proxies proxy.txt

### Using TOR

- python3 MAKADOS.py https://target.com --tor

### RUN SILENTLY

- python3 MAKADOS.py https://target.com --silent

| Option      | Description                              |
| ----------- | ---------------------------------------- |
| `--post`    | Use POST instead of GET                  |
| `--threads` | Number of threads (default: 1000)        |
| `--proxies` | Path to proxy list file                  |
| `--tor`     | Route traffic through Tor using torsocks |
| `--log`     | Log sent requests to a file              |
| `--silent`  | Hide terminal output                     |


### YOU CAN USE ALL THE COMMANDS TOGETHER TOO. BUT MAKE SURE YOU HAVE GOOD SPECS IN YOUR PC YOU WILL ALSO NEED TO START TOR BEFORE INITIATING TOR COMMAND 
### DONT USE IT ON LIVE WEBSITES AS IT WILL CRASH THEM EASILY
### --THREADS COMMAND WILL USE YOUR RAM AND CPU CORES TO ATTACK SO MAKE SURE YOU OPERATE CAREFULL BY DEFAULT ITS MIN 1000 THREADS DONT MORE THAN YOU COMPUTER'S CAPACITY  
