# json-db
A simple thread-safe database that persists data as a single json file, with a key-value abstraction. Tjson-db uses file-level locking and was motivated by situations where worker threads (as in WSGI deployments) cause problems with global state. It is good for applications with few concurrent users.
