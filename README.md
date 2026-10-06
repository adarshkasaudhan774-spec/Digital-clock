# 🕐 Python Digital Clock with Date

A simple and attractive "Digital Clock with Date" built using "Python and Tkinter".  
It displays the current time, day, date, month, and year and updates automatically every second.

## ✨ Features

- 🕐 Real-time digital clock
- 📅 Displays current day and date
- 🔄 Automatically updates every second
- 🖥️ Simple Tkinter graphical interface
- 🎨 Clean black-and-white design
- 🐍 Beginner-friendly Python project
- 📦 No external libraries required

## 📸 Project Preview

![Python Digital Clock with Date](digital-clock-screenshot.png)

> The screenshot above shows the actual output of the Digital Clock project.

## 🛠️ Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| 🐍 Python        | Main programming language |
| 🖼️ Tkinter       | GUI development           |
| ⏱️ `time` module | Current time and date     |

## 📂 Project Structure

````text
Digital-Clock/
│
├── clock.py
├── clock-screenshot.png
└── README.md

## ⚙️ How to Run
### 1. Clone the repository
```bash
git clone https://github.com/your-username/digital-clock.git
````

### 2. Open the project

```bash
cd digital-clock
```

### 3. Run the program

```bash
python digital_clock.py
```

The Digital Clock window will open automatically.

## 💻 Important Code

The current time is obtained using:

```python
current_time = strftime("%I:%M:%S %p")
```

The current date is obtained using:

```python
current_date = strftime("%A, %d %B %Y")
```

The display updates every second using:

```python
root.after(1000, update_clock)
```

## 📅 Date Format

```text
%A, %d %B %Y
```

Example:

```text
Tuesday, 06 October 2026
```

## ⏰ Time Format

```text
%I:%M:%S %p
```

Example:

```text
03:53:26 PM
```

## 🎯 Learning Objectives

This project helps you practice:

- Python functions
- Tkinter GUI
- Labels and window configuration
- Date and time formatting
- Automatic GUI updates
- Basic project organization

## 🚀 Future Improvements

- 🌙 Dark/Light mode
- 🎨 Custom themes and fonts
- ⏰ Alarm clock
- ⏱️ Stopwatch
- ⏳ Countdown timer
- 🔊 Alarm sound
- 🌍 Multiple time zones
- 📅 Calendar
- 🖥️ Full-screen mode
- ⚙️ Settings panel

## 👨‍💻Created By

**Adarsh Aksaudhan**

## ⭐ Support

If you find this project useful, consider giving the GitHub repository a ⭐ Star!

### 🚀 Keep Coding. Keep Learning. Keep Building!
