from .faculty_url import facultyUrls
from .faculty_details import facultyDetails
import pandas as pd
from pathlib import Path

urls = [
    "https://www.daiict.ac.in/faculty",
    "https://www.daiict.ac.in/adjunct-faculty",
    "https://www.daiict.ac.in/adjunct-faculty-international",
    "https://www.daiict.ac.in/distinguished-professor",
    "https://www.daiict.ac.in/professor-practice"
]

faculty_urls = []

for url in urls:
    temp_faculty_urls = facultyUrls(url, True)
    faculty_urls.extend(temp_faculty_urls)

faculty_details = []

for faculty_url in faculty_urls:
    temp_faculty_details = facultyDetails(faculty_url, True)
    faculty_details.append(temp_faculty_details)

df = pd.DataFrame(faculty_details)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(DATA_DIR / "dau-faculty.csv", index=False)
