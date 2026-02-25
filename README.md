# 🌱 Plant Nursery E-Commerce Website

A full-stack Django-based Plant Nursery web application that allows users to browse plants, add them to cart, place orders, and make payments.

---

## 🚀 Features

- 🏡 Home page with plant listings
- 🌿 Category-wise plant filtering
- 🔍 Plant detail page
- 🛒 Add to Cart functionality
- 📦 Order placement system
- 💳 Payment method selection (COD / Online)
- 📊 Order status tracking (Pending, Processing, Shipped, Delivered, Cancelled)
- 🖼 Plant image upload support
- 🛠 Django Admin Panel for management

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📂 Project Structure


plant_nursery/
│
├── shop/ # Plant listing & cart logic
├── orders/ # Order & payment management
├── media/ # Uploaded plant images
├── templates/ # HTML templates
├── db.sqlite3
└── manage.py


---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MUGASIN/plant_nursery.git
cd plant_nursery
2️⃣ Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate
3️⃣ Install Dependencies
pip install django
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver

Now open:

http://127.0.0.1:8000/

👨‍💻 Author

Developed by MUGASIN

📌 Future Improvements

Razorpay Payment Integration

User Authentication System

Order History Dashboard

Deployment on Cloud (Render / Railway)

Email Confirmation on Order

⭐ If you like this project, give it a star!

---

