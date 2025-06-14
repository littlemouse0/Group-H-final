中文
# Django Notebook App

這是一個使用 Django 製作的線上筆記本應用程式，專為大學生課堂使用與筆記協作設計。支援資料夾分類、筆記版本管理、關鍵字搜尋、使用者權限控制等功能。

## 🔧 主要功能

- ✅ 使用者註冊 / 登入 / 登出
- ✅ 建立、編輯、刪除筆記
- ✅ 建立資料夾並分類筆記
- ✅ 搜尋功能（支援多關鍵字）
- ✅ 筆記版本記錄（自動備份）
- ✅ 權限控制：
  - 筆記是否公開 (`is_public`)
  - 是否允許其他人編輯 (`editable`)
- ✅ 管理頁面（Django admin）

## 📁 專案結構

```
notebook_project/
├── notes/             # 筆記 app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       └── notes/
├── templates/
│   └── registration/
├── static/
├── manage.py
└── requirements.txt
```

## 🚀 安裝與執行

```bash
git clone https://github.com/your-username/notebook-app.git
cd notebook-app
python -m venv venv
source venv/bin/activate  # Windows 用者請執行 venv\Scripts\activate
pip install -r requirements.txt

```

打開瀏覽器進入：
```
http://127.0.0.1:8000/
```

## 🔐 管理後台

```
http://127.0.0.1:8000/admin/
```

## ✍️ 作者

- Group H 
          -112370144林謙宏
          -112370109吳詳郁
          -112370138施浩偉
- 使用 Django + Bootstrap 製作
-------------------------
Emglish

# Django Notebook App

This is an online notebook application built using Django, designed specifically for university students to take and share notes. It supports folder categorization, version tracking, keyword search, and user permission control.

## 🔧 Features

- ✅ User registration / login / logout
- ✅ Create, edit, delete notes
- ✅ Organize notes into folders
- ✅ Search functionality (supports multiple keywords)
- ✅ Note version history (automatic backup)
- ✅ Access control:
  - Whether the note is public (`is_public`)
  - Whether others can edit the note (`editable`)
- ✅ Admin dashboard (Django admin)

## 📁 Project Structure

```
notebook_project/
├── notes/             # Notes app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       └── notes/
├── templates/
│   └── registration/
├── static/
├── manage.py
└── requirements.txt
```

## 🚀 Installation and Usage

```bash
git clone https://github.com/your-username/notebook-app.git
cd notebook-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open your browser and visit:
```
http://127.0.0.1:8000/
```

## 🔐 Admin Dashboard

```
http://127.0.0.1:8000/admin/
```

## ✍️ Authors

- Group H  
  - 112370144 Lin Qian-Hong  
  - 112370109 Wu Xiang-Yu  
  - 112370138 Shih Hao-Wei  
- Built with Django + Bootstrap
