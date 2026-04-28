FutureHub | Next-Gen Footwear Showcase
FutureHub is a high-performance, "Official Company" style footwear website built with a focus on experimental UI/UX and dynamic content management. It features a bold, minimalist light theme, heavy geometric typography, and immersive animations powered by GSAP.

🚀 Features
1. "Sick" Experimental UI
Dynamic Hero Section: A high-impact entrance with "Precision In Every Stride" typography and a choreographed GSAP entrance.

Spinning Button Drop: A custom-animated "Learn More" button that drops from the top and spins into place with a physical bounce effect upon page load.

Monochrome Geometric Transition: A high-energy transition overlay featuring spinning black and white squares that "blast" the user into the Engineering Lab when clicking "Learn More".

Product Reveal Scroll: An immersive scroll experience where the main product image expands to fill the screen as the user dives deeper into the site.

2. Powerful Django Backend
Dynamic Product Management: Swap the hero sneaker image and name directly from the Django Admin panel without touching the frontend code.

Manageable Category Grid: The "Collections," "Innovation," and "Studio" cards are fully dynamic. You can update images, titles, and subtitles in the backend to keep up with global trends.

Clean Template Architecture: Uses Django template inheritance with a global base.html for a unified "Enlarged Black Top Bar" across all pages.

3. Modern Tech Stack
Backend: Django (Python).

Frontend: Tailwind CSS for rapid, modern styling.

Animations: GSAP (GreenSock) & ScrollTrigger for high-end, buttery-smooth motion.

Database: SQLite (Development).

🛠️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/your-username/FutureHub_Website.git
cd FutureHub_Website
2. Set Up Virtual Environment
Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install Dependencies
Bash
pip install django Pillow
4. Database Migrations
Apply the models to your local database:

Bash
python manage.py makemigrations
python manage.py migrate
5. Create Admin Account
Create a superuser to access the "FutureHub" backend:

Bash
python manage.py createsuperuser
6. Run the Server
Bash
python manage.py runserver
Visit http://127.0.0.1:8000/ to see the site.

📂 Project Structure
config/: Project settings and root URL configurations.

core/: The main application folder containing models for Hero Products and Category Cards.

templates/:

base.html: The global skeleton with the enlarged black navigation bar.

core/index.html: The main landing page with GSAP scroll-trigger animations.

core/learn_more.html: The light-themed brand story page.

media/: Stores dynamically uploaded sneaker and category images.

📸 Admin Preview
You can manage the entire "trendy" aesthetic via the Django Admin:

Navigate to /admin.

Add a Hero Product to change the main sneaker.

Add Category Cards to update the top-level grid (Collections, Innovation, Studio).
