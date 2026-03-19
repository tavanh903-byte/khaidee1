"""
Khaidee — Auto Download 160 Part Images
รันโดย GitHub Actions อัตโนมัติ
"""
import os, time, requests

IMAGES = [
  {"id": "SS001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s20-5g-0.jpg", "filename": "SS001.jpg"},
  {"id": "SS002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s20-plus-5g-0.jpg", "filename": "SS002.jpg"},
  {"id": "SS003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s20-ultra-5g-0.jpg", "filename": "SS003.jpg"},
  {"id": "SS004", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-5g-1.jpg", "filename": "SS004.jpg"},
  {"id": "SS005", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-plus-5g-1.jpg", "filename": "SS005.jpg"},
  {"id": "SS006", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-ultra-5g-1.jpg", "filename": "SS006.jpg"},
  {"id": "SS007", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-5g-1.jpg", "filename": "SS007.jpg"},
  {"id": "SS008", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-plus-5g-1.jpg", "filename": "SS008.jpg"},
  {"id": "SS009", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-ultra-5g-1.jpg", "filename": "SS009.jpg"},
  {"id": "SS010", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-5g-1.jpg", "filename": "SS010.jpg"},
  {"id": "SS011", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-plus-5g-1.jpg", "filename": "SS011.jpg"},
  {"id": "SS012", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-ultra-5g-1.jpg", "filename": "SS012.jpg"},
  {"id": "SS013", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-5g-1.jpg", "filename": "SS013.jpg"},
  {"id": "SS014", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-plus-5g-1.jpg", "filename": "SS014.jpg"},
  {"id": "SS015", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg", "filename": "SS015.jpg"},
  {"id": "SA001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a51-1.jpg", "filename": "SA001.jpg"},
  {"id": "SA002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a52-1.jpg", "filename": "SA002.jpg"},
  {"id": "SA003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a52s-5g-1.jpg", "filename": "SA003.jpg"},
  {"id": "SA004", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a53-5g-1.jpg", "filename": "SA004.jpg"},
  {"id": "SA005", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a54-1.jpg", "filename": "SA005.jpg"},
  {"id": "SA006", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg", "filename": "SA006.jpg"},
  {"id": "SA007", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a32-1.jpg", "filename": "SA007.jpg"},
  {"id": "SA008", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a33-5g-1.jpg", "filename": "SA008.jpg"},
  {"id": "SA009", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a34-5g-1.jpg", "filename": "SA009.jpg"},
  {"id": "SA010", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a35-1.jpg", "filename": "SA010.jpg"},
  {"id": "SA011", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a71-1.jpg", "filename": "SA011.jpg"},
  {"id": "SA012", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a72-1.jpg", "filename": "SA012.jpg"},
  {"id": "SA013", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a73-5g-1.jpg", "filename": "SA013.jpg"},
  {"id": "SA014", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a14-1.jpg", "filename": "SA014.jpg"},
  {"id": "SA015", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a15-5g-2.jpg", "filename": "SA015.jpg"},
  {"id": "SA016", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a25-5g-2.jpg", "filename": "SA016.jpg"},
  {"id": "SA017", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a05s-1.jpg", "filename": "SA017.jpg"},
  {"id": "SN001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note20-0.jpg", "filename": "SN001.jpg"},
  {"id": "SN002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note20-ultra-5g-1.jpg", "filename": "SN002.jpg"},
  {"id": "SN003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note-10-1.jpg", "filename": "SN003.jpg"},
  {"id": "SN004", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note-10-plus-1.jpg", "filename": "SN004.jpg"},
  {"id": "SN005", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note-9-1.jpg", "filename": "SN005.jpg"},
  {"id": "IP001", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-6-1.jpg", "filename": "IP001.jpg"},
  {"id": "IP002", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-6-plus-1.jpg", "filename": "IP002.jpg"},
  {"id": "IP003", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-6s-1.jpg", "filename": "IP003.jpg"},
  {"id": "IP004", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-6s-plus-1.jpg", "filename": "IP004.jpg"},
  {"id": "IP005", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-7-1.jpg", "filename": "IP005.jpg"},
  {"id": "IP006", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-7-plus-1.jpg", "filename": "IP006.jpg"},
  {"id": "IP007", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-8-1.jpg", "filename": "IP007.jpg"},
  {"id": "IP008", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-8-plus-1.jpg", "filename": "IP008.jpg"},
  {"id": "IP009", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-x-1.jpg", "filename": "IP009.jpg"},
  {"id": "IP010", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-xr-1.jpg", "filename": "IP010.jpg"},
  {"id": "IP011", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-xs-1.jpg", "filename": "IP011.jpg"},
  {"id": "IP012", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-xs-max-1.jpg", "filename": "IP012.jpg"},
  {"id": "IP013", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-1.jpg", "filename": "IP013.jpg"},
  {"id": "IP014", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-pro-1.jpg", "filename": "IP014.jpg"},
  {"id": "IP015", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-pro-max-1.jpg", "filename": "IP015.jpg"},
  {"id": "IP016", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-1.jpg", "filename": "IP016.jpg"},
  {"id": "IP017", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-mini-1.jpg", "filename": "IP017.jpg"},
  {"id": "IP018", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-pro-1.jpg", "filename": "IP018.jpg"},
  {"id": "IP019", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-pro-max-1.jpg", "filename": "IP019.jpg"},
  {"id": "IP020", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-1.jpg", "filename": "IP020.jpg"},
  {"id": "IP021", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-mini-1.jpg", "filename": "IP021.jpg"},
  {"id": "IP022", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-1.jpg", "filename": "IP022.jpg"},
  {"id": "IP023", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-pro-max-1.jpg", "filename": "IP023.jpg"},
  {"id": "IP024", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-1.jpg", "filename": "IP024.jpg"},
  {"id": "IP025", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-plus-1.jpg", "filename": "IP025.jpg"},
  {"id": "IP026", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-1.jpg", "filename": "IP026.jpg"},
  {"id": "IP027", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-max-1.jpg", "filename": "IP027.jpg"},
  {"id": "RM001", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-7-1.jpg", "filename": "RM001.jpg"},
  {"id": "RM002", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-7-pro-1.jpg", "filename": "RM002.jpg"},
  {"id": "RM003", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-8-1.jpg", "filename": "RM003.jpg"},
  {"id": "RM004", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-8-pro-1.jpg", "filename": "RM004.jpg"},
  {"id": "RM005", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-9-4g-1.jpg", "filename": "RM005.jpg"},
  {"id": "RM006", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-9-pro-plus-1.jpg", "filename": "RM006.jpg"},
  {"id": "RM007", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-10-pro-plus-1.jpg", "filename": "RM007.jpg"},
  {"id": "RM008", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-11-pro-plus-5g-1.jpg", "filename": "RM008.jpg"},
  {"id": "RM009", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-12-pro-plus-5g-1.jpg", "filename": "RM009.jpg"},
  {"id": "XM001", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-9-1.jpg", "filename": "XM001.jpg"},
  {"id": "XM002", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-9-pro-1.jpg", "filename": "XM002.jpg"},
  {"id": "XM003", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-10-1.jpg", "filename": "XM003.jpg"},
  {"id": "XM004", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-10-pro-1.jpg", "filename": "XM004.jpg"},
  {"id": "XM005", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-11-1.jpg", "filename": "XM005.jpg"},
  {"id": "XM006", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-11-pro-plus-5g-1.jpg", "filename": "XM006.jpg"},
  {"id": "XM007", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-12-5g-1.jpg", "filename": "XM007.jpg"},
  {"id": "XM008", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-12-pro-plus-5g-1.jpg", "filename": "XM008.jpg"},
  {"id": "XM009", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-13-5g-1.jpg", "filename": "XM009.jpg"},
  {"id": "XM010", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-13-pro-1.jpg", "filename": "XM010.jpg"},
  {"id": "XM011", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-13-pro-plus-5g-1.jpg", "filename": "XM011.jpg"},
  {"id": "XM012", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-poco-x3-nfc-1.jpg", "filename": "XM012.jpg"},
  {"id": "XM013", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-poco-x5-pro-5g-1.jpg", "filename": "XM013.jpg"},
  {"id": "OP001", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-f3-1.jpg", "filename": "OP001.jpg"},
  {"id": "OP002", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-f5-1.jpg", "filename": "OP002.jpg"},
  {"id": "OP003", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-f7-1.jpg", "filename": "OP003.jpg"},
  {"id": "OP004", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-f9-1.jpg", "filename": "OP004.jpg"},
  {"id": "OP005", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-f11-1.jpg", "filename": "OP005.jpg"},
  {"id": "OP006", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-f11-pro-1.jpg", "filename": "OP006.jpg"},
  {"id": "OP007", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a54-1.jpg", "filename": "OP007.jpg"},
  {"id": "OP008", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a74-1.jpg", "filename": "OP008.jpg"},
  {"id": "OP009", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno5-1.jpg", "filename": "OP009.jpg"},
  {"id": "OP010", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno6-5g-1.jpg", "filename": "OP010.jpg"},
  {"id": "OP011", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno7-5g-1.jpg", "filename": "OP011.jpg"},
  {"id": "OP012", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno8-5g-1.jpg", "filename": "OP012.jpg"},
  {"id": "OP013", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno10-5g-1.jpg", "filename": "OP013.jpg"},
  {"id": "OP014", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno11-5g-1.jpg", "filename": "OP014.jpg"},
  {"id": "OP015", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno11-pro-5g-1.jpg", "filename": "OP015.jpg"},
  {"id": "OP016", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-a79-5g-1.jpg", "filename": "OP016.jpg"},
  {"id": "VI001", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v7-1.jpg", "filename": "VI001.jpg"},
  {"id": "VI002", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v9-1.jpg", "filename": "VI002.jpg"},
  {"id": "VI003", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v11-1.jpg", "filename": "VI003.jpg"},
  {"id": "VI004", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v15-pro-1.jpg", "filename": "VI004.jpg"},
  {"id": "VI005", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v20-1.jpg", "filename": "VI005.jpg"},
  {"id": "VI006", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v21-5g-1.jpg", "filename": "VI006.jpg"},
  {"id": "VI007", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v23-5g-1.jpg", "filename": "VI007.jpg"},
  {"id": "VI008", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v25-1.jpg", "filename": "VI008.jpg"},
  {"id": "VI009", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v27-5g-1.jpg", "filename": "VI009.jpg"},
  {"id": "VI010", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v29-5g-1.jpg", "filename": "VI010.jpg"},
  {"id": "VI011", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-5g-1.jpg", "filename": "VI011.jpg"},
  {"id": "VI012", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-pro-5g-1.jpg", "filename": "VI012.jpg"},
  {"id": "VI013", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-y200-5g-1.jpg", "filename": "VI013.jpg"},
  {"id": "BS001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s20-5g-0.jpg", "filename": "BS001.jpg"},
  {"id": "BS002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s20-ultra-5g-0.jpg", "filename": "BS002.jpg"},
  {"id": "BS003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-5g-1.jpg", "filename": "BS003.jpg"},
  {"id": "BS004", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s21-ultra-5g-1.jpg", "filename": "BS004.jpg"},
  {"id": "BS005", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s22-5g-1.jpg", "filename": "BS005.jpg"},
  {"id": "BS006", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-5g-1.jpg", "filename": "BS006.jpg"},
  {"id": "BS007", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-5g-1.jpg", "filename": "BS007.jpg"},
  {"id": "BA001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a51-1.jpg", "filename": "BA001.jpg"},
  {"id": "BA002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a54-1.jpg", "filename": "BA002.jpg"},
  {"id": "BA003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg", "filename": "BA003.jpg"},
  {"id": "BA004", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a35-1.jpg", "filename": "BA004.jpg"},
  {"id": "BN001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note-9-1.jpg", "filename": "BN001.jpg"},
  {"id": "BN002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note-10-1.jpg", "filename": "BN002.jpg"},
  {"id": "BN003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note20-0.jpg", "filename": "BN003.jpg"},
  {"id": "BI001", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-6-1.jpg", "filename": "BI001.jpg"},
  {"id": "BI002", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-6-plus-1.jpg", "filename": "BI002.jpg"},
  {"id": "BI003", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-7-1.jpg", "filename": "BI003.jpg"},
  {"id": "BI004", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-8-1.jpg", "filename": "BI004.jpg"},
  {"id": "BI005", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-x-1.jpg", "filename": "BI005.jpg"},
  {"id": "BI006", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-xr-1.jpg", "filename": "BI006.jpg"},
  {"id": "BI007", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-11-1.jpg", "filename": "BI007.jpg"},
  {"id": "BI008", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-1.jpg", "filename": "BI008.jpg"},
  {"id": "BI009", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-1.jpg", "filename": "BI009.jpg"},
  {"id": "BI010", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-1.jpg", "filename": "BI010.jpg"},
  {"id": "BG001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg", "filename": "BG001.jpg"},
  {"id": "BG002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-ultra-5g-1.jpg", "filename": "BG002.jpg"},
  {"id": "BG003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg", "filename": "BG003.jpg"},
  {"id": "BG004", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-max-1.jpg", "filename": "BG004.jpg"},
  {"id": "BG005", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-1.jpg", "filename": "BG005.jpg"},
  {"id": "BG006", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-13-1.jpg", "filename": "BG006.jpg"},
  {"id": "BG007", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-12-1.jpg", "filename": "BG007.jpg"},
  {"id": "TG001", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-5g-1.jpg", "filename": "TG001.jpg"},
  {"id": "TG002", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-5g-1.jpg", "filename": "TG002.jpg"},
  {"id": "TG003", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a55-1.jpg", "filename": "TG003.jpg"},
  {"id": "TG004", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-a35-1.jpg", "filename": "TG004.jpg"},
  {"id": "TG005", "url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-note20-ultra-5g-1.jpg", "filename": "TG005.jpg"},
  {"id": "TG006", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-max-1.jpg", "filename": "TG006.jpg"},
  {"id": "TG007", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-1.jpg", "filename": "TG007.jpg"},
  {"id": "TG008", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-x-1.jpg", "filename": "TG008.jpg"},
  {"id": "TG009", "url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-8-1.jpg", "filename": "TG009.jpg"},
  {"id": "TG010", "url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-redmi-note-13-pro-1.jpg", "filename": "TG010.jpg"},
  {"id": "TG011", "url": "https://fdn2.gsmarena.com/vv/pics/oppo/oppo-reno11-pro-5g-1.jpg", "filename": "TG011.jpg"},
  {"id": "TG012", "url": "https://fdn2.gsmarena.com/vv/pics/vivo/vivo-v30-pro-5g-1.jpg", "filename": "TG012.jpg"},
  {"id": "TG013", "url": "https://fdn2.gsmarena.com/vv/pics/realme/realme-12-pro-plus-5g-1.jpg", "filename": "TG013.jpg"},
  {"id": "TG014", "url": "https://m.media-amazon.com/images/I/61yTxPJT6OL._AC_SX679_.jpg", "filename": "TG014.jpg"},
]

SAVE_DIR = 'images/parts'
os.makedirs(SAVE_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://www.gsmarena.com/'
}

ok = fail = skip = 0

print(f'🚀 Downloading {len(IMAGES)} images...')

for i, item in enumerate(IMAGES, 1):
    save_path = os.path.join(SAVE_DIR, item['filename'])
    if os.path.exists(save_path) and os.path.getsize(save_path) > 5000:
        print(f'[{i:3d}/{len(IMAGES)}] SKIP {item["filename"]}')
        skip += 1
        continue
    try:
        r = requests.get(item['url'], headers=HEADERS, timeout=20)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(save_path, 'wb') as f:
                f.write(r.content)
            print(f'[{i:3d}/{len(IMAGES)}] OK   {item["filename"]} ({len(r.content)//1024}KB)')
            ok += 1
        else:
            print(f'[{i:3d}/{len(IMAGES)}] FAIL {item["filename"]} HTTP {r.status_code}')
            fail += 1
    except Exception as e:
        print(f'[{i:3d}/{len(IMAGES)}] ERR  {item["filename"]} {e}')
        fail += 1
    time.sleep(0.3)

print(f'
Done! OK={ok} SKIP={skip} FAIL={fail}')
if fail > 0:
    import sys; sys.exit(1)
