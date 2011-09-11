from datetime import date


colleges = {
    'College of Agriculture': {
        'AGB' : 'Agribusiness',
        'AGSC': 'Agricultural Science',
        'ASM' : 'Agricultural Systems Management',
        'AEPS': 'Agriculture and Environmental Plant Sciences',
        'ASCI': 'Animal Science',
        'BRAE': 'Bioresource and Agricultural Engineering',
        'CRSC': 'Crop Science',
        'DSCI': 'Dairy Science',
        'ERSC': 'Earth Sciences',
        'EHS' : 'Environmental Horticultural Science',
        'ENVM': 'Environmental Management Protection',
        'FSN' : 'Food Science',
        'FS'  : 'Forestry Sciences',
        'FNR' : 'Forestry and Natural Resources',
        'FRSC': 'Fruit Science',
        'NUT' : 'Nutrition ',
        'RPTA': 'Recreation, Parks & Tourism Administration',
        'SOIL': 'Soil Science',
        'WVIT': 'Wine & Viticulture',
    },
    'College of Architecture & Environmental Design': {
        'ARCE': 'Architectural Engineering',
        'ARCH': 'Architecture ',
        'CRP' : 'City and Regional Planning',
        'CM'  : 'Construction Management',
        'LA'  : 'Landscape Architecture',
    },
    'Orfalea College of Business': {
        'BT'  : 'Business & Technology',
        'BUS' : 'Business Administration',
        'ECON': 'Economics',
        'IT'  : 'Industrial Technology',
    },
    'College of Engineering': {
        'AERO': 'Aerospace Engineering',
        'CE'  : 'Civil Engineering',
        'CEENVE': 'Civil and Environmental Engineering',
        'CPE' : 'Computer Engineering',
        'CSC' : 'Computer Science',
        'EE'  : 'Electrical Engineering',
        'ENVE': 'Environmental Engineering',
        'FPE' : 'Fire Protection Engineering',
        'GENE': 'General Engineering',
        'IE'  : 'Industrial Engineering',
        'MFGE': 'Manufacturing Engineering',
        'MATE': 'Materials Engineering',
        'ME'  : 'Mechanical Engineering',
        'SE'  : 'Software Engineering',
    },
    'College of Liberal Arts': {
        'ANTGEOG': 'Anthropology and Geography',
        'CD'  : 'Child Development',
        'COMS': 'Communication Studies',
        'ES'  : 'Comparative Ethnic Studies',
        'ENGL': 'English',
        'GRC' : 'Graphic Communications',
        'HIST': 'History',
        'JOUR': 'Journalism',
        'MLL' : 'Modern Languages & Literatures',
        'MU'  : 'Music',
        'PHIL': 'Philosophy',
        'POLS': 'Political Science',
        'PSY' : 'Psychology',
        'SOCS': 'Social Sciences',
        'SOC' : 'Sociology',
    },
    'College of Science and Mathematics': {
        'BCHM': 'Biochemistry',
        'BIO' : 'Biological Sciences',
        'CHEM': 'Chemistry',
        'KINE': 'Kinesiology',
        'LS'  : 'Liberal Studies',
        'MATH': 'Mathematics',
        'MICRO': 'Microbiology',
        'PCS' : 'Polymers & Coatings Science',
        'PHYS': 'Physics',
        'STAT': 'Statistics',
    },
}


def majors():
    """
    Returns a list of tuples of Cal Poly majors
    """
    majors = sum(college for college in colleges.values())
    majors.sort(key=lambda m: m[1])
    return majors


def years():
    """
    Generates a list of possible Cal Poly graduation years
    """
    years = range(1901, date.today().year + 7)
    years = zip(years, years)
    years.reverse()
    return years

