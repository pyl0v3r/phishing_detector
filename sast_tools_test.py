import hashlib

def vulns():
    #Eval function security hotspot
    user_input = input("Enter something here: ")
    result = eval(user_input) 
    print(result)
     
    API_KEY = "my_super_secret_api_key"  # Intentional security flaw
    print(f"API Key: {API_KEY}")  

     # Insecure Hash Function
    password = "mypassword"
    hash = hashlib.md5(password.encode()).hexdigest() 
    print(hash)


