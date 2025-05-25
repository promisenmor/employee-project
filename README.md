# 👥 Employee Management System

A web-based application designed to streamline the management of employee records within an organization. Built with Django, this system allows administrators to perform CRUD operations on employee data, ensuring efficient and organized record-keeping.

## 🌐 Live Demo

Experience the application live at: [employee-project-eta.vercel.app](https://employee-project-eta.vercel.app)

## 🚀 Features

- **Employee Registration**: Add new employees with essential details.
- **Employee Directory**: View a list of all registered employees.
- **Update Records**: Modify existing employee information.
- **Delete Records**: Remove employee entries as needed.
- **Responsive Design**: Accessible on various devices for ease of use.

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Deployment**: Vercel

## 📁 Project Structure
employee-project/
├── Employee/ 
├── employeeRegister/ 
├── db.sqlite3 
├── manage.py
├── requirement.txt 
├── vercel.json 
└── README.md 


## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/promisenmor/employee-project.git
   cd employee-project
   
python -m venv venv
source venv/bin/activate  

pip install -r requirement.txt

python manage.py migrate

python manage.py runserver

Access the application:
Navigate to http://127.0.0.1:8000/ in your web browser.

## 📌 Future Enhancements
Implement user authentication for secure access.

Add search and filter functionalities for employee records.

Integrate pagination for improved data navigation.

Enhance the UI/UX for better user experience.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License
This project is licensed under the MIT License.

## 👤 Author
Promise Nmor

GitHub: @promisenmor

LinkedIn: linkedin.com/in/promisenmor
