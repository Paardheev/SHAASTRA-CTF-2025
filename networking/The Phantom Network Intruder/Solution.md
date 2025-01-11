the log file started with "salted.." which means it's a aes encryption

the password.txt has algorithm and password

openssl enc -d -aes-256-cbc -in key.log -out decryptred_key.log
this looks like ssl keys, we can load it in pcapng file.

question says they have logged in somewhere, hence lets check http packets.
since the http packets are encrypted we have to use the previously decrypted log files to decrypt the requests.
apply http filter, go to edit preferences > go to protocols > go to tls and load the ssl keys log file.
now we can read the http request.

one request contains password feild with flag, Shaastra{NE3W0RK!NG}

![Screenshot 2025-01-11 184413](https://github.com/user-attachments/assets/c361db02-31de-4d04-a3f4-53bab8603c07)
![Screenshot 2025-01-11 184500](https://github.com/user-attachments/assets/50c36940-47be-4b29-a1b3-d0ba3edaf590)
![Screenshot 2025-01-11 184519](https://github.com/user-attachments/assets/0b651ccb-0e31-49ba-a61d-b3bb21e7720d)
![Screenshot 2025-01-11 184348](https://github.com/user-attachments/assets/ae678176-f564-400e-b889-7af829373aac)
