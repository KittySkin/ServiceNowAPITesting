# ServiceNow API Wrapper
This is a quick and simple API Wrapper around the REST API provided by 
ServiceNow.

The system provides the following:

An UserCredentials class that stores user and password.  
An APIWrapper class that can be instantiated and stores UserCredentials as well
as the instance url for ServiceNow along with a system to call generic functions
that automatically pass username, password and instance url as the first 3 args.  
The call can take extra arguments in a variadic way and pass them to the called
function.  
Generic REST API functions that can be called using the APIWrapper class or by 
themselves providing flexibility to lib user.

For example usage check the main.py file.