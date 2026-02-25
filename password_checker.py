import re  

def check_password(password):   
     score = 0   
     suggestions = [] 

     if len(password) >= 8: 
         score += 1
     else:
         suggestions.append("password must be at least 8 characters long") 
     if re.search(r'[A-Z]', password):
         score += 1  
     else:
         suggestions.append("Add at least one uppercase letter (A-Z)") 
     if re.search(r'[a-z]', password):   
        score  += 1 
     else:
         suggestions.append("Add at least one lowercase letter (a-z)")
     if re.search(r'[0-9]',password):
        score += 1
     else:
         suggestions.append("Add at least one number (0-9)")
     if re.search(r'[!@#$%^&*]',password):
        score += 1
     else:
         suggestions.append("Add at least one special character (!@#$%^&*)")
     if score <= 2:
         strength = "❌ WEAK Password"
     elif score <= 4:
         strength = "⚠️ MEDIUM Password"
     else:
         strength = "✅ STRONG Password"
     print(f"\nPassword Strength: {strength}")
     if suggestions:
            print("\nSuggestions to improve your password:")
            for s in suggestions:
                print(f"  --> {s}")

password = input("Enter your password: ")
check_password(password)

