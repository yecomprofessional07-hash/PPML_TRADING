import pandas as pd
from ..usuarios.recibiendo import recibir
empresas = {
    # 🔴 TECNOLOGÍA (25 empresas)
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta Platforms (Facebook)": "META",
    "Tesla": "TSLA",
    "Broadcom": "AVGO",
    "Adobe": "ADBE",
    "Salesforce": "CRM",
    "Oracle": "ORCL",
    "Cisco": "CSCO",
    "Intel": "INTC",
    "IBM": "IBM",
    "Qualcomm": "QCOM",
    "AMD": "AMD",
    "Netflix": "NFLX",
    "PayPal": "PYPL",
    "Intuit": "INTU",
    "ServiceNow": "NOW",
    "Applied Materials": "AMAT",
    "Texas Instruments": "TXN",
    "Micron Technology": "MU",
    "Snowflake": "SNOW",
    "Shopify": "SHOP",
    
    # 🏦 FINANZAS (20 empresas)
    "JPMorgan Chase": "JPM",
    "Bank of America": "BAC",
    "Wells Fargo": "WFC",
    "Citigroup": "C",
    "Goldman Sachs": "GS",
    "Morgan Stanley": "MS",
    "BlackRock": "BLK",
    "Visa": "V",
    "Mastercard": "MA",
    "American Express": "AXP",
    "S&P Global": "SPGI",
    "Moody's": "MCO",
    "Blackstone": "BX",
    "Charles Schwab": "SCHW",
    "PNC Financial": "PNC",
    "Truist Financial": "TFC",
    "US Bancorp": "USB",
    "Capital One": "COF",
    "Aon": "AON",
    "Marsh & McLennan": "MMC",
    
    # 🏥 SALUD (15 empresas)
    "Johnson & Johnson": "JNJ",
    "UnitedHealth": "UNH",
    "Pfizer": "PFE",
    "Merck": "MRK",
    "AbbVie": "ABBV",
    "Eli Lilly": "LLY",
    "Thermo Fisher Scientific": "TMO",
    "Abbott Laboratories": "ABT",
    "Danaher": "DHR",
    "Amgen": "AMGN",
    "Bristol-Myers Squibb": "BMY",
    "Gilead Sciences": "GILD",
    "Moderna": "MRNA",
    "Regeneron": "REGN",
    "Biogen": "BIIB",
    
    # 🛒 CONSUMO (20 empresas)
    "Procter & Gamble": "PG",
    "Walmart": "WMT",
    "Coca-Cola": "KO",
    "PepsiCo": "PEP",
    "McDonald's": "MCD",
    "Nike": "NKE",
    "Home Depot": "HD",
    "Lowe's": "LOW",
    "Starbucks": "SBUX",
    "Costco": "COST",
    "Target": "TGT",
    "Disney": "DIS",
    "Netflix": "NFLX",
    "Booking Holdings": "BKNG",
    "Estée Lauder": "EL",
    "Colgate-Palmolive": "CL",
    "Mondelez": "MDLZ",
    "Kraft Heinz": "KHC",
    "General Mills": "GIS",
    "Hershey": "HSY",
    
    # ⚡ ENERGÍA/INDUSTRIALES (10 empresas)
    "Exxon Mobil": "XOM",
    "Chevron": "CVX",
    "ConocoPhillips": "COP",
    "NextEra Energy": "NEE",
    "Southern Company": "SO",
    "Boeing": "BA",
    "Caterpillar": "CAT",
    "3M": "MMM",
    "Honeywell": "HON",
    "Union Pacific": "UNP",
    
    # 🏠 BIENES RAÍCES/UTILIDADES (10 empresas)
    "American Tower": "AMT",
    "Crown Castle": "CCI",
    "Prologis": "PLD",
    "Equinix": "EQIX",
    "Digital Realty": "DLR",
    "Verizon": "VZ",
    "AT&T": "T",
    "T-Mobile": "TMUS",
    "Comcast": "CMCSA",
    "Charter Communications": "CHTR"
}

def enviar(self):
    selector= self
    if selector in empresas.keys():
        ident = empresas[selector]
        return ident
    else:
        return None

