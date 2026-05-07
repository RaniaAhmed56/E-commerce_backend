🛒 BLANKO E-Commerce Backend API

A scalable and production-ready Django REST Framework backend for a full-featured e-commerce platform with advanced Admin Dashboard, User Management, Orders System, Coupons, Wishlist, and Analytics Engine.

🚀 Project Overview

BLANKO Backend is a complete e-commerce REST API designed to support:

Multi-role system (Admin / Customer)
Full e-commerce workflow (products → cart → orders → payment-ready flow)
Advanced Admin Dashboard (sales, revenue, users, orders analytics)
Dynamic product filtering and search
Coupon and discount system
Wishlist & user personalization features
Ready for frontend integration (React / Mobile apps)
⚙️ Tech Stack
Backend: Django, Django REST Framework
Authentication: JWT (SimpleJWT)
Database: SQLite (can be switched to PostgreSQL in production)
Architecture: RESTful API
Security: Role-based access control (RBAC)
📦 Installation & Setup
1. Clone the project
cd blanko-backend
2. Install dependencies
pip install -r requirements.txt
3. Run automated setup
bash setup.sh

This script will automatically:

Install dependencies
Create database
Run migrations
Seed initial data (admin, products, settings)
Start development server
🔐 Default Credentials
Admin Account
Email: admin@blanko.com
Password: admin123
Admin Panel
http://localhost:8000/django-admin/
📡 API Documentation
🔐 Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register new user
POST	/api/auth/login/	Login & receive JWT token
POST	/api/auth/logout/	Logout user
GET	/api/auth/me/	Get current user profile
PUT	/api/auth/me/update/	Update user profile
POST	/api/auth/refresh/	Refresh access token
🛍️ Products
Method	Endpoint	Description
GET	/api/products/	List all products (filters supported)
GET	/api/products/{id}/	Product details
POST	/api/products/	Create product (Admin only)
PATCH	/api/products/{id}/	Update product
DELETE	/api/products/{id}/	Delete product

Filtering Support:

?category=Women&sort=newest&featured=true&trending=true
&min_price=50&max_price=200&search=shirt
📦 Orders System
Method	Endpoint	Description
POST	/api/orders/	Create new order
GET	/api/orders/	User orders / All orders (Admin)
PATCH	/api/orders/{id}/update_status/	Update order status
GET	/api/orders/dashboard_stats/	Admin analytics dashboard
🎟️ Coupons System
Method	Endpoint	Description
POST	/api/coupons/validate/	Validate coupon
GET	/api/coupons/	List coupons (Admin)
POST	/api/coupons/	Create coupon
PATCH	/api/coupons/{id}/	Update coupon
DELETE	/api/coupons/{id}/	Delete coupon
❤️ Wishlist
Method	Endpoint	Description
GET	/api/wishlist/	Get wishlist
POST	/api/wishlist/add/	Add product
DELETE	/api/wishlist/remove/{product_id}/	Remove product
🧑‍💼 Admin Dashboard APIs
Method	Endpoint	Description
GET	/api/admin/users/	Manage users
GET	/api/admin/settings/	Get store settings
POST	/api/admin/settings/update/	Update settings
📊 Admin Dashboard Features

The system includes a powerful admin layer that provides:

📈 Sales & Revenue analytics
📦 Order tracking & management
👥 User management system
🛍️ Product inventory control
🎟️ Coupon management
📢 Ads & promotions control
⚙️ Global store settings
📊 Real-time dashboard statistics
🧱 Project Structure
blanko-backend/
│
├── blanko/              # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── api/                 # Main application
│   ├── models.py        # Database models
│   ├── views.py         # API logic
│   ├── serializers.py   # Data serialization
│   ├── urls.py          # Routes
│   └── admin.py         # Admin configuration
│
├── seed_data.py         # Initial data seeding
├── setup.sh             # One-command setup script
├── requirements.txt
└── manage.py