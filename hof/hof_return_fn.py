def email_builder(domain): #outer fn
    def build_email(username): #inner fn
        return f"{username}@{domain}"
    return build_email # returning outer fn returns inner fn

# Check if the script is being run as the main program
gmail = email_builder("gmail.com") # function call This creates a function that takes a username and returns an email address with the domain "gmail.com" => build_email function is returned and assigned to gmail variable. Now we can use gmail variable to create email addresses with the domain "gmail.com".
yahoo = email_builder("yahoo.com")
hotmail = email_builder("hotmail.com")
example = email_builder("example.com")

# Example usage
print(gmail("john.doe"))  # Output: john.doe@gmail.com
print(yahoo("jane.smith"))  # Output: jane.smith@yahoo.com
print(hotmail("alice"))  # Output:
print(example("bob"))  # Output: bob@example.com