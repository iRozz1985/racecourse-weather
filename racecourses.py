"""Coordinates for every active horse racing course in the UK and Ireland.

Each entry is (name, country, latitude, longitude). Country is one of:
    ENG  - England
    SCO  - Scotland
    WAL  - Wales
    IRE  - Ireland (Republic of Ireland + Northern Ireland tracks)

Latitude/longitude are decimal degrees (WGS84), rounded to ~4 dp which puts
them within a few hundred metres of the track - plenty accurate for a weather
forecast. Used by weather_at_racecourses.py.

Breakdown: 52 in England, 5 in Scotland, 3 in Wales (60 in Great Britain) and
26 in Ireland (24 Republic + 2 Northern Ireland), giving 86 courses in total.
"""

# name, country, lat, lon
RACECOURSES = [
    # ---- England (ENG) ----
    ("Aintree",            "ENG", 53.4760, -2.9440),
    ("Ascot",              "ENG", 51.4100, -0.6790),
    ("Ayr",                "SCO", 55.4590, -4.6230),
    ("Bangor-on-Dee",      "WAL", 52.9960, -2.9170),
    ("Bath",               "ENG", 51.3870, -2.4290),
    ("Beverley",           "ENG", 53.8470, -0.4480),
    ("Brighton",           "ENG", 50.8300, -0.1010),
    ("Carlisle",           "ENG", 54.9230, -2.9560),
    ("Cartmel",            "ENG", 54.2010, -2.9570),
    ("Catterick",          "ENG", 54.3760, -1.6470),
    ("Chelmsford City",    "ENG", 51.7560,  0.4660),
    ("Cheltenham",         "ENG", 51.9250, -2.0580),
    ("Chepstow",           "WAL", 51.6360, -2.6790),
    ("Chester",            "ENG", 53.1860, -2.8980),
    ("Doncaster",          "ENG", 53.5180, -1.1130),
    ("Epsom Downs",        "ENG", 51.3140, -0.2560),
    ("Exeter",             "ENG", 50.6710, -3.4720),
    ("Fakenham",           "ENG", 52.8160,  0.8690),
    ("Fontwell Park",      "ENG", 50.8530, -0.6480),
    ("Goodwood",           "ENG", 50.8990, -0.7310),
    ("Hamilton Park",      "SCO", 55.7920, -4.0410),
    ("Haydock Park",       "ENG", 53.4790, -2.6300),
    ("Hereford",           "ENG", 52.0580, -2.7420),
    ("Hexham",             "ENG", 54.9540, -2.1300),
    ("Huntingdon",         "ENG", 52.3410, -0.1920),
    ("Kelso",              "SCO", 55.6060, -2.4440),
    ("Kempton Park",       "ENG", 51.4160, -0.4080),
    ("Leicester",          "ENG", 52.6000, -1.0960),
    ("Lingfield Park",     "ENG", 51.1700, -0.0160),
    ("Ludlow",             "ENG", 52.3760, -2.7390),
    ("Market Rasen",       "ENG", 53.3860, -0.3220),
    ("Musselburgh",        "SCO", 55.9440, -3.0520),
    ("Newbury",            "ENG", 51.3990, -1.3010),
    ("Newcastle",          "ENG", 55.0170, -1.6210),
    ("Newmarket",          "ENG", 52.2410,  0.3870),
    ("Newton Abbot",       "ENG", 50.5330, -3.6020),
    ("Nottingham",         "ENG", 52.9540, -1.0920),
    ("Perth",              "SCO", 56.4260, -3.4150),
    ("Plumpton",           "ENG", 50.9230, -0.0530),
    ("Pontefract",         "ENG", 53.6980, -1.3010),
    ("Redcar",             "ENG", 54.6150, -1.0680),
    ("Ripon",              "ENG", 54.1420, -1.5150),
    ("Salisbury",          "ENG", 51.0540, -1.8420),
    ("Sandown Park",       "ENG", 51.3760, -0.3620),
    ("Sedgefield",         "ENG", 54.6450, -1.4360),
    ("Southwell",          "ENG", 53.0810, -0.9540),
    ("Stratford-on-Avon",  "ENG", 52.1870, -1.7210),
    ("Taunton",            "ENG", 51.0000, -3.0890),
    ("Thirsk",             "ENG", 54.2340, -1.3600),
    ("Towcester",          "ENG", 52.1290, -0.9970),
    ("Uttoxeter",          "ENG", 52.8970, -1.8640),
    ("Warwick",            "ENG", 52.2730, -1.5970),
    ("Wetherby",           "ENG", 53.9360, -1.3900),
    ("Wincanton",          "ENG", 51.0540, -2.4030),
    ("Windsor",            "ENG", 51.4830, -0.6090),
    ("Wolverhampton",      "ENG", 52.5870, -2.1250),
    ("Worcester",          "ENG", 52.1990, -2.2300),
    ("Yarmouth",           "ENG", 52.6050,  1.7210),
    ("York",               "ENG", 53.9430, -1.0960),

    # ---- Wales (WAL) : Bangor-on-Dee & Chepstow listed above ----
    ("Ffos Las",           "WAL", 51.7360, -4.2600),

    # ---- Republic of Ireland + Northern Ireland (IRE) ----
    ("Ballinrobe",         "IRE", 53.6270, -9.2240),
    ("Bellewstown",        "IRE", 53.6540, -6.3330),
    ("Clonmel",            "IRE", 52.3610, -7.7360),
    ("Cork",               "IRE", 52.1360, -8.4190),
    ("Curragh",            "IRE", 53.1640, -6.8360),
    ("Down Royal",         "IRE", 54.5080, -6.1140),  # Northern Ireland
    ("Downpatrick",        "IRE", 54.3340, -5.7190),  # Northern Ireland
    ("Dundalk",            "IRE", 54.0030, -6.3940),
    ("Fairyhouse",         "IRE", 53.4740, -6.4790),
    ("Galway",             "IRE", 53.2510, -8.9910),
    ("Gowran Park",        "IRE", 52.6300, -7.0640),
    ("Kilbeggan",          "IRE", 53.3570, -7.4990),
    ("Killarney",          "IRE", 52.0510, -9.5160),
    ("Laytown",            "IRE", 53.6760, -6.2410),
    ("Leopardstown",       "IRE", 53.2630, -6.1950),
    ("Limerick",           "IRE", 52.5680, -8.5490),
    ("Listowel",           "IRE", 52.4480, -9.4790),
    ("Naas",               "IRE", 53.2130, -6.6760),
    ("Navan",              "IRE", 53.6530, -6.6980),
    ("Punchestown",        "IRE", 53.1890, -6.6350),
    ("Roscommon",          "IRE", 53.6360, -8.1960),
    ("Sligo",              "IRE", 54.2660, -8.4610),
    ("Thurles",            "IRE", 52.6830, -7.8140),
    ("Tipperary",          "IRE", 52.4650, -8.1540),
    ("Tramore",            "IRE", 52.1620, -7.1430),
    ("Wexford",            "IRE", 52.3380, -6.4810),
]

COUNTRY_NAMES = {
    "ENG": "England",
    "SCO": "Scotland",
    "WAL": "Wales",
    "IRE": "Ireland",
}
