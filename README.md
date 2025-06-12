# Fitness Booking API - Omnify 

The **Fitness Booking API** is a RESTful service that enables clients to view available fitness classes, book sessions, and track their booking history in real time. Built with **FastAPI**, this backend system is designed for a fictional fitness studio to manage its class schedules and user bookings.

> 🌐 **Live Demo:** [https://omnify-fastapi-1.onrender.com/docs](https://omnify-fastapi-1.onrender.com/docs)
> 
> 🎥 **Loom Video Walkthrough:** [Watch Here](https://www.loom.com/share/your-loom-video-id)

---

## 📚 Table of Contents

- [Getting Started](#-getting-started)
- [Local Installation](#-local-installation)
- [API Endpoints](#-api-endpoints)
- [Authentication](#-authentication)
- [Rate Limits](#-rate-limits)
- [Postman Collection](#-postman-collection)
- [Swagger & ReDoc](#-swagger--redoc)
- [Testing](#-testing)
- [Contributing](#-contributing)

---

## 🚀 Getting Started

To start using the API:

1. Make sure the API is running at [https://fitness-booking-lockandopen.vercel.app](https://fitness-booking-lockandopen.vercel.app).
2. Use **Swagger**, **ReDoc**, or **Postman** to explore and test the API.
3. No authentication is required for basic use.
4. All endpoints are publicly available and respond in JSON.

---

## 💻 Local Installation

To run the API locally, follow these steps:

```bash
# 1. Clone the repository
$ git clone https://github.com/your-username/fitness-booking-api.git
$ cd fitness-booking-api

# 2. (Optional) Create a virtual environment
$ python -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run the FastAPI app
$ uvicorn main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the Swagger documentation locally.

---

## 🔌 API Endpoints

### ✅ View All Upcoming Classes

- **GET** `/classes`
- **Description**: Returns a list of all upcoming fitness classes.
- **Response**:

```json
[
  {
    "name": "HIIT",
    "date_time": "2025-06-13T10:30:00",
    "id": 1,
    "instructor": "Aron Swartz",
    "available_slots": 50
  },
  ...
]
```

---

### 🗕️ Book a Class

- **POST** `/book`
- **Body**:

```json
{
  "id": 3,
  "client_name": "Arafat",
  "client_email": "stringsss@gmail.com"
}
```

- **Success Response**:

```text
Session is Booked  for Zumba at 2025-06-12 18:00:00 ,thanks Arafat
```

- **Validation**:
  - Checks for overbooking
  - Validates class ID and class time

---

### 📜 Get Booking History by Email

- **GET** `/booking/?email=strings@gmail.com`
- **Response**:

```json
[
  {
    "id": 1,
    "booked_at": "2025-06-12T15:27:20.766613",
    "fitness_class": {
      "name": "Yoga",
      "date_time": "2025-06-13T07:00:00",
      "instructor": "Tyrell Wellick",
      "available_slots": 49
    }
  },
  ...
]
```

---

### 📂 Add New Class (Admin)

- **POST** `/classes`
- **Body**:

```json
{
  "name": "Pilates",
  "date_time": "2025-06-15T10:00:00",
  "instructor": "Darlene",
  "available_slots": 30
}
```

- **Response**:

```json
{
  "message": "Classes is added Pilates and instrcutor Darlene"
}
```

---

### 📁 Get All Booking Logs (Admin)

- **GET** `/book_all`
- **Description**: Returns all archived booking data.
- **Response**:

```json
[
  {
    "id": 1,
    "class_id": 1,
    "client_id": 1,
    "booked_at": "2025-06-12T03:05:07.605677",
    "archived_at": "2025-06-12T13:42:47.356171"
  },
  ...
]
```

---

## 🔐 Authentication

Currently, **no authentication** is required. In the future, `JWT` or `OAuth` can be integrated for secured admin routes.

---

## 📉 Rate Limits

- 🔄 No strict rate limiting is applied.
- 🚧 For production, consider adding throttling middleware or FastAPI rate-limiting extensions.

---

## 📬 Postman Collection

You can test all endpoints using Postman.

📁 **Download**: [`Fitness_Booking_Omnify.postman_collection.json`](https://github.com/MohamedAsifS/Postman_doc_omnify_fastapi)

🛠️ **How to use**:

1. Open Postman.
2. Click **Import** → Choose the JSON file.
3. Use endpoints for booking, viewing classes, and history.

---

## 📊 Swagger & ReDoc

- 📘 **Swagger UI**: [https://fitness-booking-lockandopen.vercel.app/docs](https://fitness-booking-lockandopen.vercel.app/docs)
- 📕 **ReDoc UI**: [https://fitness-booking-lockandopen.vercel.app/redoc](https://fitness-booking-lockandopen.vercel.app/redoc)

---

## 🧪 Testing

- ✅ **Manual Testing** with Swagger and browser endpoints
- ✅ **Automated API Testing** using Postman Collection
- 🔍 Edge case validation tested (duplicate booking, overbooking, empty fields)
- 🧰 Optional: Add `pytest` or `unittest` if needed for future expansion

---

## 🤝 Contributing

Have an idea to improve this API?

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

Made with 💪 by [Mohamed Asif](https://www.linkedin.com/in/mohamed-asif-a5856817b/)


