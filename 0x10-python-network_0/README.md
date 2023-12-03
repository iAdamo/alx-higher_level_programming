### **Python - Network #0**
**`Bash`** **`Python`** **`Scripting`** **`Back-end`** **`API`**

**Read or watch:**

- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

#### **0. cURL body size**

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use curl
```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `0-body_size.sh`

#### **1. cURL to the end**
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

- Display only body of a `200` status code response
- You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `1-body.sh`

#### **2. cURL Method**

Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

- You have to use `curl`
- Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- File: `2-delete.sh`

#### **3. cURL only methods**

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- You have to use `curl`
- Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
```

##### Author: **`Adam Sanusi Babatunde`**
