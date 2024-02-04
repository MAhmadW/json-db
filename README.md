# json-db
A simple thread-safe database that persists data as a single json file, with a key-value abstraction. json-db uses file-level locking and was motivated by situations where worker threads (as in WSGI deployments) cause problems with global state. It is good for applications with few concurrent users.

Currently it is built with portalocker, which provides for OS file locks, but future versions of json-db will move away from this requirement. This is to ensure little to no dependency issues.

Further refinement of this tool that I plan: 
- Documentation
- Refactoring based on OOP principles
- A cleaner API with better dev experience