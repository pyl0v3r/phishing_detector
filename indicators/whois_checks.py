import whois
from urllib.parse import urlparse

def check_domain_age(domain):
    try:
        domain_info = whois.whois(domain)
        
        # Handle lists and extract the earliest date
        creation_date = domain_info.creation_date
        updated_date = domain_info.updated_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(updated_date, list):
            updated_date = updated_date[0]

        if creation_date and updated_date:
            age = (updated_date - creation_date).days
            if age < 180:
                return ["Domain age is less than 6 months"]
    except Exception as e:
        return [f"Error retrieving domain age: {str(e)}"]
    
    return []
