# 🏨 Dormitory Management System

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</div>

<div align="center">
  <h3>A comprehensive Django-based web application for managing student dormitories, admissions, chatrooms, and hostel administration.</h3>
  <p>Designed to streamline hostel workflows, provide real-time communication, and improve user experience for students and staff.</p>
</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Technologies Used](#️-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/🧾-Student_Admission-blue?style=for-the-badge" alt="Admission"/>
        <br><strong>Student Admission Module</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/🏢-Hostel_Management-green?style=for-the-badge" alt="Hostel"/>
        <br><strong>Hostel & Room Management</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/👤-User_Profiles-orange?style=for-the-badge" alt="Profile"/>
        <br><strong>User Profile Handling</strong>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/💬-Real_Time_Chat-purple?style=for-the-badge" alt="Chat"/>
        <br><strong>Real-Time Chatrooms</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/🤖-Chatbot_Support-red?style=for-the-badge" alt="Chatbot"/>
        <br><strong>Integrated Chatbot Support</strong>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/📅-Timetable_View-yellow?style=for-the-badge" alt="Timetable"/>
        <br><strong>Timetable Management</strong>
      </td>
    </tr>
  </table>
</div>

### Additional Features:
- 🗂️ **Media Handling** - Secure file uploads and management
- 🛡️ **Authentication & Authorization** - Secure user access control
- 📱 **Responsive Design** - Mobile-friendly interface
- ⚡ **Real-time Updates** - Live notifications and updates

---

## 📁 Project Structure

```
Dormitory_Management_System/
│
├── 📂 admission/              # Student admission logic and forms
├── 📂 chatbot/                # AI chatbot integration
├── 📂 chatroom/               # Real-time chat functionality
├── 📂 hostel/                 # Hostel room & administration
├── 📂 hostel_management/      # Django project settings
├── 📂 media/                  # User uploaded files
├── 📂 static/                 # Static assets (CSS, JS, images)
├── 📂 templates/              # HTML templates
├── 📂 timetable/              # Class schedules management
├── 📂 userprofile/            # User registration & profiles
│
├── 🗄️ db.sqlite3             # Development database
├── ⚙️ manage.py               # Django management script
├── 📋 requirements.txt        # Python dependencies
└── 📖 README.md               # Project documentation
```

---

## ⚙️ Technologies Used

<div align="center">
  <h3>Backend</h3>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  
  <h3>Frontend</h3>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
</div>

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/Kowshik-bh18/Dormitory_Management_System.git
cd Dormitory_Management_System
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### Step 5: Run the Development Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:8000
```

---

## 🎯 Usage

### Sample Credentials (for testing)
```
Username: admin
Password: admin123
```

### Key Endpoints
- **Home**: `/` - Main dashboard
- **Admin Panel**: `/admin/` - Administrative interface
- **User Registration**: `/register/` - New user signup
- **Chatroom**: `/chat/` - Real-time messaging
- **Admissions**: `/admission/` - Student admission portal

---

## 📸 Screenshots

<div align="center">
  <img src="https://via.placeholder.com/800x400/0d1117/58a6ff?text=Dashboard+Screenshot" alt="Dashboard" width="48%"/>
  <img src="https://via.placeholder.com/800x400/0d1117/58a6ff?text=Chatroom+Screenshot" alt="Chatroom" width="48%"/>
  
  <img src="https://via.placeholder.com/800x400/0d1117/58a6ff?text=Admission+Portal" alt="Admission" width="48%"/>
  <img src="https://via.placeholder.com/800x400/0d1117/58a6ff?text=Hostel+Management" alt="Hostel Management" width="48%"/>
</div>

*Replace these placeholder images with actual screenshots of your application*

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contributors

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/Kowshik-bh18.png" width="100px;" alt="Kowshik BH"/>
        <br />
        <sub><b>Kowshik BH</b></sub>
        <br />
        <a href="https://github.com/Kowshik-bh18">🚀 Lead Developer</a>
      </td>
      <td align="center">
        <img src="https://github.com/MDGanesha.png" width="100px;" alt="MDGanesha"/>
        <br />
        <sub><b>MDGanesha</b></sub>
        <br />
        <a href="https://github.com/MDGanesha">💻 Developer</a>
      </td>
    </tr>
  </table>
</div>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Dormitory Management System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🌐 Live Demo

🔗 **[View Live Demo](https://your-app-name.herokuapp.com)** *(Replace with your actual deployment URL)*

---

## 📞 Contact

<div align="center">
  <h3>Get in Touch</h3>
  
  **Kowshik BH**
  
  [![Email](https://img.shields.io/badge/Email-kobh22cs@cmrit.ac.in-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kobh22cs@cmrit.ac.in)
  [![Phone](https://img.shields.io/badge/Phone-+91_7483226281-green?style=for-the-badge&logo=whatsapp&logoColor=white)](tel:+917483226281)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
  [![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Kowshik-bh18)
</div>

---

<div align="center">
  <h3>⭐ Star this repository if you found it helpful!</h3>
  <p>Made with ❤️ for the student community</p>
  
  <img src="https://img.shields.io/github/stars/Kowshik-bh18/Dormitory_Management_System?style=social" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/Kowshik-bh18/Dormitory_Management_System?style=social" alt="GitHub forks"/>
  <img src="https://img.shields.io/github/watchers/Kowshik-bh18/Dormitory_Management_System?style=social" alt="GitHub watchers"/>
</div>
