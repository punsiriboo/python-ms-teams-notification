# MS Teams Notification with Python - แจ้งเตือนอัตโนมัติภายในองค์กร
![MS Teams Notification](images/title.png)

โปรเจกต์นี้ช่วยให้คุณสามารถส่งการแจ้งเตือนไปยัง Microsoft Teams โดยใช้ Python และ Cloud Run Function ได้อย่างง่ายดาย

## คุณสมบัติ
- ส่งข้อความแจ้งเตือนแบบง่ายไปยัง Microsoft Teams
- รองรับการตั้งค่าผ่านไฟล์ `.env`
- ใช้โครงสร้างโค้ดที่เข้าใจง่ายและปรับแต่งได้

## Step to Create MS Teams Workflow
[Please, follow step in documents](documents/create_ms_workflow.md)


### โครงสร้างโปรเจกต์
```
├── .env                  # ไฟล์ตั้งค่าตัวแปรลับ
├── snippet/
│   └── single_message.py # ตัวอย่างการส่งข้อความ
├── deployment/           # สคริปต์สำหรับการ deploy
└── README.md             # ไฟล์เอกสารโปรเจกต์
```


## การติดตั้ง
1. Clone โปรเจกต์นี้:
   ```bash
   git clone https://github.com/your-repo/ms-teams-notification.git
   cd ms-teams-notification

2. สร้าง Virtual Environment และติดตั้ง dependencies:
```
    python -m venv .venv
    source .venv/bin/activate  # สำหรับ Linux/Mac
    .venv\Scripts\activate     # สำหรับ Windows
    pip install -r requirements.txt
```

3. คัดลอกไฟล์ .env.example เป็น .env และตั้งค่า Webhook URL:
```
MS_TEAMS_WEBHOOK_URL="YOUR_WEBHOOK_URL"
```

# การใช้งาน
1. รันสคริปต์ตัวอย่างเพื่อส่งข้อความแจ้งเตือน:
```
python snippet/single_message.py
```
