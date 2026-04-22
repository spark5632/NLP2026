#pip install requests beautifulsoup4 



# import requests
# from bs4 import BeautifulSoup


# def crawl_tree_data():
#     url = "https://en.wikipedia.org/wiki/Honey"
#     try:
#         tesponse = requests.get(url)
#         response.encodeing = "utf-8"
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text,"html.parser")
#             paragraph = soup.find_all("p")
#             content = ""
#             for p in paragraph:
#                 content += p.get_text()+"\n"

#                 with open("tree_info.txt","w",encoding="utf-8")as f:
#                     f.write(content)
#                 print("เย้ ๆ ๆ ๆ")
#             else:
#                 print(f"แย่ ๆ ๆ ๆ ๆ ๆ {response.status_code}")
#     except Exception as  e:
#         print(f"แย่มาก : {e}")

# if __name__ == "__main__":
#     crawl_tree_data()



import requests
from bs4 import BeautifulSoup

def crawl_tree_data():
    url = "https://www.foodnetworksolution.com/wiki/word/1155/honey-%19%E0%B9%89%E0%B8%B3%1C%E0%B8%B6%E0%B9%89%07#google_vignette"
    
    # 1. เพิ่ม Headers เพื่อบอก Wikipedia ว่าเราคือ Browser ทั่วไป
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # 2. ส่ง headers เข้าไปพร้อมกับ request
        response = requests.get(url, headers=headers)
        response.encoding = "utf-8" 
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            content = ""
            
            for p in paragraphs:
                content += p.get_text() + "\n"

            with open("tree_info.txt", "w", encoding="utf-8") as f:
                f.write(content)
            
            print("เย้ ๆ ๆ ๆ ดึงข้อมูลสำเร็จแล้ว!")
        else:
            # ตอนนี้ถ้าได้ 403 มันจะมาตกที่นี่
            print(f"แย่ ๆ ๆ ๆ ๆ ๆ ติด Error code: {response.status_code}")
            print("ลองเช็คเรื่อง User-Agent หรือการเชื่อมต่ออินเทอร์เน็ตดูนะ")
            
    except Exception as e:
        print(f"แย่มาก เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    crawl_tree_data()