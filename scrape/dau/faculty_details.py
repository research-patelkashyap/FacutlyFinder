import requests
from bs4 import BeautifulSoup

def facultyDetails(faculty_url, verbose=False):
    try:
        html = requests.get(faculty_url).text
        
        soup = BeautifulSoup(html, "html.parser")
        
        name = soup.select_one("div.field--name-field-faculty-names")
        name = name.get_text(strip=True) if name else None
        
        education = soup.select_one("div.field--name-field-faculty-name")
        education = education.get_text(strip=True) if education else None
        
        phone = soup.select_one("div.field--name-field-contact-no")
        phone = phone.get_text(strip=True) if phone else None
        
        address = soup.select_one("div.field--name-field-address")
        address = address.get_text(strip=True) if address else None
        
        email = soup.select_one("div.field--name-field-email")
        email = email.get_text(strip=True) if email else None
        
        faculty_website = soup.select_one("div.field--name-field-sites")
        faculty_website = faculty_website.get_text(strip=True) if faculty_website else None
        
        bio = soup.select_one("div.field--name-field-biography")
        bio = bio.get_text("\n", strip=True) if bio else None
        
        spec = soup.find("h2", string="Specialization")
        if spec:
            spec = spec.find_next("div", class_="work-exp")
            spec = spec.get_text(strip=True)
        
        teaching = soup.find("h2", string="Teaching")
        if teaching:
            teaching = [
                li.get_text(strip=True)
                for li in teaching.find_next("ul").find_all("li")
            ]
        
        research = soup.find("h2", string="Research")
        if research:
            research = research.find_next(
                "div", class_="work-exp1"
            )
            research = research.get_text("\n", strip=True) if research else None

        faculty_details = {
            "Name": name,
            "Education": education,
            "Phone": phone,
            "Address": address,
            "Email": email,
            "FacultyWebsite": faculty_website,
            "Bio": bio,
            "specialization": spec,
            "Teaching": teaching,
            "Research": research
        }
        
        if verbose:
            print(faculty_details)
        
        return faculty_details

    except Exception as e:
        print(f"Failed on {faculty_url}: {e}")
