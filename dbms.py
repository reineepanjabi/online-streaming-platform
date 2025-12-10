import streamlit as st

import pandas as pd


# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="Online Streaming Platform DBMS Project", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #dcedc8;  /* Light blue background color */
    }
    </style>
    """,
    unsafe_allow_html=True)
st.title("🎬 Online Streaming Platform — DBMS Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
tabs = [
    "📘 Project Overview",
    "🔖 Roadmap / Index",
    "📥 Entities & Attributes",
    "🔗 Relationships (ER Diagram)",
    "📑 Create Tables & Inserts",
    "📊 SQL Queries",
    "👤 User Dashboard"
]
if "selected_tab" not in st.session_state:
    st.session_state["selected_tab"] = tabs[0]
selected_tab = st.sidebar.radio(
    "Go to:",
    tabs,
    index=tabs.index(st.session_state["selected_tab"])
)

st.session_state["selected_tab"] = selected_tab
# ============================
# TAB 0 — PROJECT OVERVIEW
# ============================
if selected_tab == "📘 Project Overview":
    st.header("📘 Project Overview")
    st.markdown("""
    **Project Title:** *Online Streaming Platform — DBMS Project*  
    **Team Members:** Aahana & Reinee  """)
    tabs = st.tabs(["📘 Description", "🎯 Objectives", "🏁 Conclusion", "⚠️ Limitations", "🚀 Future Scope"])


    with tabs[0]:
        st.markdown("""
    This project focuses on designing and implementing a **Database Management System (DBMS)** 
    for an online streaming platform.  

    - Using **SQL (Oracle)**, we created multiple **tables and entities**, defined **relationships**, 
      and executed various **queries** to analyze user data, content, and revenue.  
    - The results and database structure were displayed through an interactive **Streamlit dashboard**, 
      enabling easy navigation and visualization.
    """)

# --------------------------- OBJECTIVES TAB ---------------------------
    with tabs[1]:
        st.markdown("""
    1. To design and implement a relational database system for an online streaming platform using SQL (Oracle).  
    2. To establish entity relationships among users, subscriptions, content, genres, and payments for efficient data management.  
    3. To execute analytical SQL queries that provide insights into user behavior, revenue, and content performance.  
    4. To create an interactive Streamlit dashboard that visualizes data outputs and enables easy navigation between entities and queries.  
    5. To demonstrate integration of database management and front-end visualization for practical understanding of DBMS concepts.
    """)

# --------------------------- CONCLUSION TAB ---------------------------
    with tabs[2]:
        st.markdown("""
    - This project successfully demonstrates the integration of SQL-based database management 
    with Python’s Streamlit interface.  

    - It simulates a real-world streaming platform where multiple entities 
    (Users, Content, Subscriptions, Payments, Reviews, etc.) are interlinked to perform analytical operations.  

    - The dashboard enables visualization of query results, supports user login simulation, 
    and helps understand relational models in a user-friendly manner.  

    - Overall, the project fulfills academic and practical objectives of database design, 
    data querying, and interactive visualization.
    """)

# --------------------------- LIMITATIONS TAB ---------------------------
    with tabs[3]:
        st.markdown("""
    1. The project uses dummy datasets, not real-time or API-driven streaming data.  
    2. The login system is simulated locally without actual authentication or encryption.  
    3. The images and posters are referenced via local or placeholder URLs instead of dynamic retrieval from a server.  
    4. Queries are predefined; users cannot dynamically input or modify SQL queries in real-time.  
    5. The dashboard does not currently support write-back or CRUD operations (create, update, delete) on the database.
    """)

# --------------------------- FUTURE SCOPE TAB ---------------------------
    with tabs[4]:
        st.markdown("""
    1. Integration with a live backend database (MySQL/PostgreSQL/Oracle Cloud) for real-time querying.  
    2. Adding a fully functional authentication system with hashed passwords and role-based access.  
    3. Implementing recommendation algorithms (content-based or collaborative filtering) to personalize user suggestions.  
    4. Enabling real-time analytics dashboards for admin-level monitoring of revenue, ratings, and engagement.  
    5. Deploying the Streamlit app on the web (via Streamlit Cloud or Heroku) for public access.  
    6. Expanding to support CRUD operations and API endpoints to make the system a working prototype of an OTT backend.
    """)
    
    
# ============================
# TAB 1 — ROADMAP
# ============================
if selected_tab == "🔖 Roadmap / Index":
    st.header("📝 Project Roadmap / Index")
    st.markdown("""
    Welcome to the **Online Streaming Platform DBMS Dashboard**.  
    Use this roadmap to navigate through different project components:
    """)

    roadmap = {
        "📥 Entities & Attributes": "Detailed description of all entities and attributes used in the database.",
        "🔗 Relationships (ER Diagram)": "ER relationships between entities with diagram upload option.",
        "📑 Create Tables & Inserts": "SQL table creation statements, insert values, and execution proofs.",
        "📊 SQL Queries": "Interactive visualization of analytical SQL queries."
    }

    for name, desc in roadmap.items():
        st.markdown(f"**{name}** — {desc}")
        if st.button(f"Go to {name}"):
            st.session_state["selected_tab"] = name

# ============================
# TAB 2 — ENTITIES & ATTRIBUTES
# ============================
elif selected_tab == "📥 Entities & Attributes":
    st.header("📥 Entities & Attributes")
    st.write("Below are the entities and their corresponding attributes:")

    entities = {
        "User1": ["user_id (PK)", 
                 "name", 
                 "email", 
                 "password", 
                 "age"],
        "Subscription": ["subscription_id (PK)", "user_id (FK → User.user_id)", "plan_id (FK → Plan.plan_id)", "start_date", "end_date"],
        "Plan": ["plan_id (PK)", "plan_name", "price", "duration"],
        "Content": ["content_id (PK)", "title", "genre_id (FK → Genre.genre_id)", "release_date", "type (movie/series)"],
        "Genre": ["genre_id (PK)", "genre_name"],
        "Review": ["review_id (PK)", "user_id (FK → User.user_id)", "content_id (FK → Content.content_id)", "rating", "comment"],
        "Watch_History": ["history_id (PK)", "user_id (FK → User.user_id)", "content_id (FK → Content.content_id)", "watch_date", "progress"],
        "Device": ["device_id (PK)", "user_id (FK → User.user_id)", "device_type", "device_name"],
        "Payment": ["payment_id (PK)", "subscription_id (FK → Subscription.subscription_id)", "amount", "payment_date", "method"],
        "Actor": ["actor_id (PK)", "actor_name", "dob"],
        "Content_Actor": ["content_id (FK → Content.content_id, PK)", "actor_id (FK → Actor.actor_id, PK)"]
    }

    for entity, attributes in entities.items():
        with st.expander(f"📍 {entity}"):
            st.markdown("**Attributes:**")
            st.write(", ".join(attributes))

# ============================
# TAB 3 — RELATIONSHIPS
# ============================
elif selected_tab == "🔗 Relationships (ER Diagram)":
    st.header("🔗 Entity Relationships")
    st.markdown("""
    **Key Relationships:**
    - User1 → Subscription : 1-to-many  
    - Subscription → Plan : many-to-1  
    - Subscription → Payment : 1-to-many  
    - User1 → Review → Content : many-to-many  
    - User1 → Watch_History → Content : many-to-many  
    - User1 → Device : 1-to-many  
    - Content → Genre : many-to-1  
    - Content → Actor : many-to-many via Content_Actor
    """)


    st.image("images/erdiag1.jpeg", caption="Uploaded ER Diagram")
    st.image("images/erdiag2.jpeg", caption="Uploaded ER Diagram")
    st.image("images/extendeder1.jpeg", caption="Extended ER Diagram")
    st.image("images/extendeder2.jpeg", caption="Extended ER Diagram")

# ============================
# TAB 4 — CREATE TABLES
# ============================
elif selected_tab == "📑 Create Tables & Inserts":
    st.header("📑 Table Creation & Inserts")

    
    table_tabs = [
        "User", "Plan", "Subscription", "Genre", "Content",
        "Review", "Watch_History", "Device", "Payment", "Actor", "Content_Actor"
    ]
    sub_tab = st.selectbox("Select Table:", table_tabs)

    st.subheader(f"📄 SQL for {sub_tab} Table")

    sql_scripts = {
        "User": """CREATE TABLE User1(
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    age INT
)

Insert all
INTO User1 VALUES(1, 'John Doe', 'john@example.com', 'password123', 28)
INTO User1 VALUES(2, 'Jane Smith', 'jane.smith@example.com', 'password456', 34)
INTO User1 VALUES(3, 'Emily Brown', 'emily@example.com', 'password789', 22)
INTO User1 VALUES(4, 'Michael Johnson', 'michael.johnson@example.com', 'password000', 30)
INTO User1 VALUES(5, 'Sarah Williams', 'sarah@example.com', 'password111', 25)
INTO User1 VALUES(6, 'David Miller', 'david.miller@example.com', 'password222', 40)
INTO User1 VALUES(7, 'Olivia Davis', 'olivia.davis@example.com', 'password333', 33)
INTO User1 VALUES(8, 'Lucas Martinez', 'lucas.martinez@example.com', 'password444', 27)
INTO User1 VALUES(9, 'Sophia Garcia', 'sophia@example.com', 'password555', 38)
INTO User1 VALUES(10, 'Ethan Lee', 'ethan.lee@example.com', 'password666', 29)
select * from dual
select * from User1
""",
        "Plan": """CREATE TABLE Plan (
    plan_id INT PRIMARY KEY,
    plan_name VARCHAR(100),
    price DECIMAL(10, 2),
    duration INT)
Insert all
INTO Plan Values (101, 'Basic', 9.99, 12)
INTO Plan Values(102, 'Standard', 14.99, 12)
INTO Plan Values(103, 'Premium', 19.99, 12)
select * from dual
select * from Plan
""",
        "Subscription": """CREATE TABLE Subscription (
    subscription_id INT PRIMARY KEY,
    user_id INT,
    plan_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES User1(user_id),
    FOREIGN KEY (plan_id) REFERENCES Plan(plan_id)
)

Insert all 
INTO Subscription Values(1001, 1, 101, '01-JAN-2023', '31-DEC-2024')
INTO Subscription Values(1002, 2, 102, '01-JAN-2023', '31-DEC-2024')
INTO Subscription Values(1003, 3, 101, '01-FEB-2023', '31-JAN-2024')
INTO Subscription Values(1004, 4, 103, '01-MAR-2023', '28-FEB-2024')
INTO Subscription Values(1005, 5, 101, '01-APR-2023', '31-MAR-2024')
INTO Subscription Values(1006, 6, 102, '01-FEB-2023', '31-JAN-2024')
INTO Subscription Values(1007, 7, 103, '01-MAY-2023', '30-APR-2024')
INTO Subscription Values(1008, 8, 101, '01-JUL-2023', '30-JUN-2024')
INTO Subscription Values(1009, 9, 102, '01-JAN-2023', '31-DEC-2024')
INTO Subscription Values(1010,10, 103, '01-JUN-2023', '31-MAY-2024')
select * from dual
select * from Subscription

""",
        "Genre": """CREATE TABLE Genre (
    genre_id INT PRIMARY KEY,
    genre_name VARCHAR(100)
)


INSERT all
INTO Genre values(11, 'Action')
INTO Genre values(22, 'Drama')
INTO Genre values(33, 'Comedy')
INTO Genre values(44, 'Horror')
INTO Genre values(55, 'Romance')
select * from dual
select * from genre

""",
        "Content": """CREATE TABLE Content (
    content_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre_id INT,
    release_date DATE,
    type VARCHAR(20), 
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
)

INSERT all
INTO Content VALUES (201, 'Shadow Protocol', 11, '10-JAN-2025', 'movie')
INTO Content VALUES (202, 'Echoes of Silence', 22, '14-FEB-2025', 'series')
INTO Content VALUES (203, 'Laugh Lines', 33, '20-MAR-2025', 'movie')
INTO Content VALUES (204, 'Whispers in the Dark', 44, '18-APR-2025', 'series')
INTO Content VALUES (205, 'Forever and Always', 55, '09-MAY-2025', 'movie')
INTO Content VALUES (206, 'Crimson Vengeance', 11, '13-JUN-2025', 'movie')
INTO Content VALUES (207, 'The Weight of Truth', 22, '25-JUL-2025', 'series')
INTO Content VALUES (208, 'Accidentally Perfect', 33, '22-AUG-2025', 'movie')
INTO Content VALUES (209, 'The Hollow Manor', 44, '19-SEP-2025', 'movie')
INTO Content VALUES (210, 'Hearts Entwined', 55, '14-NOV-2025', 'series')
SELECT * FROM dual
SELECT * FROM Content
""",
        "Review": """CREATE TABLE Review(
    review_id INT PRIMARY KEY,
    user_id INT,
    content_id INT,
    rating INT,
    commentt VARCHAR2(500),
    FOREIGN KEY (user_id) REFERENCES User1(user_id),
    FOREIGN KEY (content_id) REFERENCES content(content_id)
)

Insert all
INTO Review VALUES(901, 1, 201, 4, 'Great action movie!')
INTO Review VALUES(902, 2, 202, 5, 'Amazing drama series, must watch!')
INTO Review VALUES(903, 3, 203, 3, 'It was a decent comedy movie.')
INTO Review VALUES(904, 4, 204, 2, 'Not scary at all, disappointing.')
INTO Review VALUES(905, 5, 205, 5, 'Loved the romance, very touching!')
INTO Review VALUES(906, 6, 206, 4, 'Action-packed and fun.')
INTO Review VALUES(907, 7, 207, 4, 'Really emotional and well acted.')
INTO Review VALUES(908, 8, 208, 3, 'Funny but predictable.')
INTO Review VALUES(909, 9, 209, 4, 'Great horror movie, very intense!')
INTO Review VALUES(910, 10, 210, 4, 'Nice romantic series, great chemistry!')
SELECT * FROM dual
SELECT * FROM Review

""",
        "Watch_History": """CREATE TABLE Watch_History (
    history_id INT PRIMARY KEY,
    user_id INT,
    content_id INT,
    watch_date DATE,
    progress INT, -- Percentage of completion
    FOREIGN KEY (user_id) REFERENCES User1(user_id),
    FOREIGN KEY (content_id) REFERENCES Content(content_id)
);

INSERT ALL
INTO Watch_History VALUES(701, 1, 201, '10-JAN-2023', 100)
INTO Watch_History VALUES(702, 2, 202, '14-FEB-2023', 80)
INTO Watch_History VALUES(703, 3, 203, '25-MAR-2023', 50)
INTO Watch_History VALUES(704, 4, 204, '10-APR-2023', 20)
INTO Watch_History VALUES(705, 5, 205, '12-MAY-2023', 100)
INTO Watch_History VALUES(706, 6, 206, '18-JUN-2023', 30)
INTO Watch_History VALUES(707, 7, 207, '02-JUL-2023', 100)
INTO Watch_History VALUES(708, 8, 208, '15-AUG-2023', 60)
INTO Watch_History VALUES(709, 9, 209, '01-SEP-2023', 90)
INTO Watch_History VALUES(710, 10, 210, '05-OCT-2023', 40)
SELECT * FROM dual
Select * from Watch_History
""",
        "Device": """CREATE TABLE Device (
    device_id INT PRIMARY KEY,
    user_id INT,
    device_type VARCHAR(50),
    device_name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES User1(user_id)
);

Insert all
INTO Device VALUES(801, 1, 'Mobile', 'iPhone 13')
INTO Device VALUES(802, 2, 'Laptop', 'Dell XPS 13')
INTO Device VALUES(803, 3, 'Tablet', 'Samsung Galaxy Tab S7')
INTO Device VALUES(804, 4, 'Smart TV', 'Sony Bravia')
INTO Device VALUES(805, 5, 'Mobile', 'Samsung Galaxy S21')
INTO Device VALUES(806, 6, 'Laptop', 'MacBook Pro')
INTO Device VALUES(807, 7, 'Smart TV', 'LG OLED')
INTO Device VALUES(808, 8, 'Laptop', 'HP Spectre x360')
INTO Device VALUES(809, 9, 'Mobile', 'Google')
Select * from dual
Select * from Device

""",
        "Payment": """CREATE TABLE Payment (
    payment_id INT PRIMARY KEY,
    subscription_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    method VARCHAR(50), -- Payment method (e.g., Credit Card, PayPal)
    FOREIGN KEY (subscription_id) REFERENCES Subscription(subscription_id)
);

INSERT ALL
INTO Payment VALUES(901, 1001, 9.99, '01-JAN-2023', 'Credit Card')
INTO Payment VALUES(902, 1002, 14.99, '01-FEB-2023', 'PayPal')
INTO Payment VALUES(903, 1003, 9.99, '01-MAR-2023', 'Credit Card')
INTO Payment VALUES(904, 1004, 19.99, '01-APR-2023', 'PayPal')
INTO Payment VALUES(905, 1005, 9.99, '01-MAY-2023', 'Credit Card')
INTO Payment VALUES(906, 1006, 14.99, '01-JUN-2023', 'PayPal')
INTO Payment VALUES(907, 1007, 19.99, '01-JUL-2023', 'Credit Card')
INTO Payment VALUES(908, 1008, 9.99, '01-AUG-2023', 'PayPal')
INTO Payment VALUES(909, 1009, 14.99, '01-SEP-2023', 'Credit Card')
INTO Payment VALUES(910, 1010, 19.99, '01-OCT-2023', 'PayPal')
SELECT * FROM dual
Select * from Payment
""",
        "Actor": """CREATE TABLE Actor (
    actor_id INT PRIMARY KEY,
    actor_name VARCHAR(100),
    dob DATE -- Date of birth
);
INSERT ALL
  INTO Actor VALUES(301, 'Will Smith', '25-SEP-1968')
  INTO Actor VALUES(302, 'Meryl Streep', '22-JUN-1949')
  INTO Actor VALUES(303, 'Tom Hanks', '09-JUL-1956')
  INTO Actor VALUES(304, 'Emma Stone', '06-NOV-1988')
  INTO Actor VALUES(305, 'Leonardo DiCaprio', '11-NOV-1974')
  INTO Actor VALUES(306, 'Scarlett Johansson', '22-NOV-1984')
  INTO Actor VALUES(307, 'Brad Pitt', '18-DEC-1963')
  INTO Actor VALUES(308, 'Natalie Portman', '09-JUN-1981')
  INTO Actor VALUES(309, 'Johnny Depp', '09-JUN-1963')
  INTO Actor VALUES(310, 'Jennifer Lawrence', '15-AUG-1990')
SELECT * FROM dual;
Select * from Actor

""",
        "Content_Actor": """CREATE TABLE Content_Actor (
    content_id INT,
    actor_id INT,
    PRIMARY KEY (content_id, actor_id),
    FOREIGN KEY (content_id) REFERENCES Content(content_id),
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
)

INSERT all 
INTO Content_Actor values(201, 301)
INTO Content_Actor values(202, 302)
INTO Content_Actor values(203, 303)
INTO Content_Actor values(204, 304)
INTO Content_Actor values(205, 305)
INTO Content_Actor values(206, 306)
INTO Content_Actor values(207, 307)
INTO Content_Actor values (208, 308)
INTO Content_Actor values (209, 309)
INTO Content_Actor values (210, 310)
Select * from dual
Select * from Content_Actor
"""
    }

    st.code(sql_scripts[sub_tab], language="sql")

    # Add this dictionary to map each table to its image
    table_images = {
    "User": "images/table1.jpeg",
    "Plan": "images/table2.jpeg",
    "Subscription": "images/table3.jpeg",
    "Genre": "images/table4.jpeg",
    "Content": "images/table5.jpeg",
    "Review": "images/table6.jpeg",
    "Watch_History": "images/table7.jpeg",
    "Device": "images/table8.jpeg",
    "Payment": "images/table9.jpeg",
    "Actor": "images/table10.jpeg",
    "Content_Actor": "images/table11.jpeg"
}

    # Display image for each table automatically
    if sub_tab in table_images:
          st.image(
            table_images[sub_tab],
            caption=f"{sub_tab} Table Schema / ER Diagram",
            use_column_width=True
            )


# ============================
# TAB 5 — SQL QUERIES DASHBOARD
# ============================
elif selected_tab == "📊 SQL Queries":
    st.header("📊 SQL Query Execution & Analysis")

    queries = {
        "QUERY 1 — Top 3 Most Popular Genres Based on Watch Count": """
SELECT g.genre_name, COUNT(wh.content_id) AS total_views
FROM Watch_History wh
JOIN Content c ON wh.content_id = c.content_id
JOIN Genre g ON c.genre_id = g.genre_id
GROUP BY g.genre_name
ORDER BY total_views DESC;
""",

        "QUERY 2 — Total Revenue Generated by Each Subscription Plan": """
SELECT p.plan_name, SUM(pay.amount) AS total_revenue
FROM Payment pay
JOIN Subscription s ON pay.subscription_id = s.subscription_id
JOIN Plan p ON s.plan_id = p.plan_id
GROUP BY p.plan_name
ORDER BY total_revenue DESC;
""",

        "QUERY 3 — Highest Rated Content Titles": """
SELECT c.title, AVG(r.rating) AS avg_rating
FROM Review r
JOIN Content c ON r.content_id = c.content_id
GROUP BY c.title
ORDER BY avg_rating DESC;
""",

        "QUERY 4 — Actor-Wise Average Content Rating": """
SELECT a.actor_name, AVG(r.rating) AS avg_actor_rating
FROM Actor a
JOIN Content_Actor ca ON a.actor_id = ca.actor_id
JOIN Review r ON ca.content_id = r.content_id
GROUP BY a.actor_name
ORDER BY avg_actor_rating DESC;
""",

        "QUERY 5 — Average Revenue Per User (ARPU)": """
SELECT SUM(pay.amount) / COUNT(DISTINCT u.user_id) AS avg_revenue_per_user
FROM User1 u
JOIN Subscription s ON u.user_id = s.user_id
JOIN Payment pay ON s.subscription_id = pay.subscription_id;
""",

        "QUERY 6 — Users Whose Subscription Expires Within 60 Days": """
SELECT u.user_id, u.name, s.end_date
FROM User1 u
JOIN Subscription s ON u.user_id = s.user_id
WHERE s.end_date BETWEEN SYSDATE AND ADD_MONTHS(SYSDATE, 2)
ORDER BY s.end_date;
""",

        "QUERY 7 — Average Watch Completion (%) per Genre": """
SELECT g.genre_name, AVG(wh.progress) AS avg_completion
FROM Watch_History wh
JOIN Content c ON wh.content_id = c.content_id
JOIN Genre g ON c.genre_id = g.genre_id
GROUP BY g.genre_name
ORDER BY avg_completion DESC;
""",

        "QUERY 8 — Find Users Who Posted More Than or equal to One Review": """
SELECT u.name, COUNT(r.review_id) AS review_count
FROM User1 u
JOIN Review r ON u.user_id = r.user_id
GROUP BY u.name
HAVING COUNT(r.review_id) > 1;
""",

        "QUERY 9 — Most Popular Actor (Based on Number of Watched Contents)": """
SELECT a.actor_name, COUNT(wh.content_id) AS total_views
FROM Actor a
JOIN Content_Actor ca ON a.actor_id = ca.actor_id
JOIN Watch_History wh ON ca.content_id = wh.content_id
GROUP BY a.actor_name
ORDER BY total_views DESC;
""",

        "QUERY 10 — Genre-Wise Revenue (Advanced Multi-Join)": """
SELECT g.genre_name, SUM(p.amount) AS total_genre_revenue
FROM Payment p
JOIN Subscription s ON p.subscription_id = s.subscription_id
JOIN User1 u ON s.user_id = u.user_id
JOIN Watch_History wh ON u.user_id = wh.user_id
JOIN Content c ON wh.content_id = c.content_id
JOIN Genre g ON c.genre_id = g.genre_id
GROUP BY g.genre_name
ORDER BY total_genre_revenue DESC;
""",

        "QUERY 11 — Most Popular Content Type (Movie or Series) by Average User Rating": """
SELECT 
    c.type AS content_type,
    AVG(r.rating) AS avg_rating,
    COUNT(DISTINCT c.content_id) AS total_titles,
    COUNT(r.review_id) AS total_reviews
FROM Content c
JOIN Review r ON c.content_id = r.content_id
GROUP BY c.type
ORDER BY avg_rating DESC;
""",

        "QUERY 12 — Users Who Have Rated Content Above the Average Rating (Subquery)": """
SELECT 
    u.user_id, 
    u.name, 
    r.content_id, 
    r.rating
FROM Review r
JOIN User1 u ON r.user_id = u.user_id
WHERE r.rating > (
    SELECT AVG(rating) 
    FROM Review
)
ORDER BY r.rating DESC;
"""
    }


    query_images = {
        "QUERY 1 — Top 3 Most Popular Genres Based on Watch Count": [
            "images/table12.jpeg",
            "images/query1explain.jpeg"
        ],
        "QUERY 2 — Total Revenue Generated by Each Subscription Plan": [
            "images/query2ans.jpeg",
            "images/query2explain.jpeg"
        ],

        "QUERY 3 — Highest Rated Content Titles": [
            "images/query3ans.jpeg",
            "images/query3explain.jpeg"
            ],

        "QUERY 4 — Actor-Wise Average Content Rating": [
            "images/query4ans.jpeg",
            "images/query4explain.jpeg"
            ] ,

        "QUERY 5 — Average Revenue Per User (ARPU)": [
            "images/query5ans.jpeg",
            "images/query5explain.jpeg"
            ],

        "QUERY 6 — Users Whose Subscription Expires Within 60 Days": [
            "images/query6ans.jpeg",
            "images/query6explain.jpeg"
            ],

        "QUERY 7 — Average Watch Completion (%) per Genre": [
            "images/query7ans.jpeg",
            "images/query7explain.jpeg"
            ],

        "QUERY 8 — Find Users Who Posted More Than or equal to One Review":[
            "images/query8ans.jpeg",
            "images/query8explain.jpeg"
            ],

        "QUERY 9 — Most Popular Actor (Based on Number of Watched Contents)": [
            "images/query9ans.jpeg",
            "images/query9explain.jpeg"
            ],

        "QUERY 10 — Genre-Wise Revenue (Advanced Multi-Join)": [
            "images/query10ans.jpeg",
            "images/query10explain.jpeg"
            ],

        "QUERY 11 — Most Popular Content Type (Movie or Series) by Average User Rating": [
            "images/query11ans.jpeg",
            "images/query11explain.jpeg"
            ],

        "QUERY 12 — Users Who Have Rated Content Above the Average Rating (Subquery)":[
            "images/query12ans.jpeg",
            "images/query12explain.jpeg"
            ]
       }

    selected_query = st.selectbox(
    "Select Query:", 
    list(queries.keys()),
    key="sql_queries_dashboard_selectbox"
   )

    st.code(queries[selected_query], language="sql")
    
    

    queries_data = {
    "QUERY 1 — Top 3 Most Popular Genres Based on Watch Count": pd.DataFrame({
        "genre_name": ["Drama", "Comedy", "Action","Horror","Romance"],
        "total_views": [2,2,2,2,2]
    }),

    "QUERY 2 — Total Revenue Generated by Each Subscription Plan": pd.DataFrame({
        "plan_name": ["Basic", "Premium", "Standard"],
        "total_revenue": [39.96,59.97,44.97]
    }),

    "QUERY 3 — Highest Rated Content Titles": pd.DataFrame({
        "title": ["Echoes of Silence","Forever and Always","Crimson Vengeance","The Weight of Truth","The Hollow Manor","Hearts Entwined","Shadow Protocol","Laugh Lines","Accidentally Perfect","Whispers in the Dark"],
        "avg_rating": [5,5,4,4,4,4,4,3,3,2]
    }),

    "QUERY 4 — Actor-Wise Average Content Rating": pd.DataFrame({
        "actor_name": ["Will Smith",
                       "Meryl Streep",
                       "Tom Hanks",
                       "Emma Stone",
                       "Leonardo DiCaprio",
                       "Scarlett Johansson",
                       "Brad Pitt",
                       "Natalie Portman",
                       "Johnny Depp",
                       "Jennifer Lawrence"],
        "avg_actor_rating": [4,5,3,2,5,4,4,3,4,4]
    }),

    "QUERY 5 — Average Revenue Per User (ARPU)": pd.DataFrame({
        "avg_revenue_per_user": [14.49]
    }),

    "QUERY 6 — Users Whose Subscription Expires Within 60 Days": pd.DataFrame({
        "user_id": [8,6,3,1,7,4,5],
        "name": ["Lucas Martinez","David Miller","Emily Brown","John Doe","Olivia Davis","Michael Johnson","Sarah Williams",],
        "end_date": ["19/10/25","20/10/25","28/10/25","10/11/25","25/11/25","05/12/25","18/12/25"]
    }),

    "QUERY 7 — Average Watch Completion (%) per Genre": pd.DataFrame({
        "genre_name": ["Drama", "Comedy", "Action","Horror","Romance"],
        "avg_completion": [35,65,90,80,65]
    }),

    "QUERY 8 — Find Users Who Posted More Than or equal to One Review": pd.DataFrame({
        "name": ["John Doe","Jane Smith","Emily Brown","Michael Johnson","Sarah Williams","David Miller","Olivia Davis","Lucas Martinez","Sophia Garcia","Ethan Lee"],
        "review_count": [1,1,1,1,1,1,1,1,1,1]
    }),

    "QUERY 9 — Most Popular Actor (Based on Number of Watched Contents)": pd.DataFrame({
        "actor_name": ["Will Smith","Meryl Streep","Tom Hanks","Emma Stone","Leonardo DiCaprio","Scarlett Johansson","Brad Pitt","Natalie Portman","Johnny Depp","Jennifer Lawrence"],
        "total_views": [1,1,1,1,1,1,1,1,1,1]
    }),

    "QUERY 10 — Genre-Wise Revenue (Advanced Multi-Join)": pd.DataFrame({
        "genre_name": ["Drama", "Comedy", "Action","Horror","Romance"],
        "total_genre_revenue": [14.99,12.49,12.49,14.99,17.49]
    }),

    "QUERY 11 — Most Popular Content Type (Movie or Series) by Average User Rating": pd.DataFrame({
        "content_type": ["Movie", "Series"],
        "avg_rating": [3.833333333,3.75],
        "total_titles": [6,4],
        "total_reviews": [6,4]
    }),

    "QUERY 12 — Users Who Have Rated Content Above the Average Rating (Subquery)": pd.DataFrame({
        "user_id": [1,2,3,4,5,6,7,8,9,10],
        "name": ["John Doe","Jane Smith","Emily Brown","Michael Johnson","Sarah Williams","David Miller","Olivia Davis","Lucas Martinez","Sophia Garcia","Ethan Lee"],
        "content_id": [201,202,203,204,205,206,207,208,209,210],
        "rating": [4,5,3,2,5,4,4,3,4,4]
    })
  }

    
    df = queries_data[selected_query]
    st.dataframe(df)

    try:
            if selected_query in query_images:
                for i, img_path in enumerate(query_images[selected_query], start=1):
                    st.image(img_path, caption=f"{selected_query} - Image {i}", use_column_width=True)
            
                if df is not None and not df.empty:
                    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                    if numeric_cols:
                        col_to_plot = numeric_cols[0]  # Choose first numeric column for visualization
            
            # Bar chart of the numeric column by first column (usually the category)
                        st.bar_chart(data=df.set_index(df.columns[0])[col_to_plot])

            # Highest and Lowest values
                        max_val = df[col_to_plot].max()
                        max_idx = df[df[col_to_plot] == max_val][df.columns[0]].values[0]

                        min_val = df[col_to_plot].min()
                        min_idx = df[df[col_to_plot] == min_val][df.columns[0]].values[0]
                    

                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric(label="Highest Value", value=f"{max_val}", delta=f"{max_idx}")
                        with col2:
                            st.metric(label="Lowest Value", value=f"{min_val}", delta=f"{min_idx}")
    except:
            ("-")

# ============================
# TAB 6 — USER LOGIN & DASHBOARD
# ============================
elif selected_tab == "👤 User Dashboard":
    st.header("👤 User Login / Signup Portal")

    # Create dummy data
    users_df = pd.DataFrame({
        "user_id": [1,2,3,4,5,6,7,8,9,10],
        "name": ["John Doe","Jane Smith","Emily Brown","Michael Johnson","Sarah Williams","David Miller","Olivia Davis","Lucas Martinez","Sophia Garcia","Ethan Lee"],
        "email": ["john@example.com","jane.smith@example.com","emily@example.com","michael.johnson@example.com","sarah@example.com","david.miller@example.com","olivia.davis@example.com","lucas.martinez@example.com","sophia@example.com","ethan.lee@example.com"],
        "password": ["password123","password456","password789","password000","password111","password222","password333","password444","password555","password666"],
        "age": [28,34,22,30,25,40,33,27,38,29]
    })

    review_df = pd.DataFrame({
        "user_id": [1,2,3,4,5,6,7,8,9,10],
        "rating": [4,5,3,2,5,4,4,3,4,4]
    })


    watch_df = pd.DataFrame({
        "user_id": [1,2,3,4,5,6,7,8,9,10],
        "progress": [100,80,50,20,100,30,100,60,90,40]
    })

    genre_df = pd.DataFrame({
        "user_id": [1,2,3,4,5,6,7,8,9,10],
        "fav_genre": ["Action","Drama","Comedy","Horror","Romance","Action","Drama","Comedy","Horror","Romance"]
    })

    plan_df = pd.DataFrame({
        "user_id": [1,2,3,4,5,6,7,8,9,10],
        "plan": ["Basic","Standard","Basic","Premium","Basic","Standard","Premium","Basic","Standard","Premium"]
    })

    # SESSION STATE for login
    if "logged_in_user" not in st.session_state:
        st.session_state.logged_in_user = None

    if st.session_state.logged_in_user is None:
        choice = st.radio("Choose an option:", ["🔑 Login", "📝 Sign Up"])

        if choice == "🔑 Login":
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                user = users_df[(users_df["email"] == email) & (users_df["password"] == password)]
                if not user.empty:
                    st.session_state.logged_in_user = int(user.iloc[0]["user_id"])
                    st.success(f"Welcome back, {user.iloc[0]['name']}! 🎉")
                    st.experimental_rerun()
                else:
                    st.error("Invalid email or password 😕")

        elif choice == "📝 Sign Up":
            new_name = st.text_input("Name")
            new_email = st.text_input("Email")
            new_password = st.text_input("Password", type="password")
            new_age = st.number_input("Age", 10, 100, 25)
            if st.button("Create Account"):
                if new_email in users_df["email"].values:
                    st.error("Email already exists.")
                else:
                    new_id = users_df["user_id"].max() + 1
                    users_df.loc[len(users_df)] = [new_id, new_name, new_email, new_password, new_age]
                    st.success("Account created successfully! You can now log in.")
    else:
        # Fetch logged-in user data
        user_id = st.session_state.logged_in_user
        user_info = users_df[users_df["user_id"] == user_id].iloc[0]

        st.subheader(f"Welcome, {user_info['name']} 👋")
        st.markdown(f"**Age:** {user_info['age']} | **Email:** {user_info['email']}")

        user_plan = plan_df[plan_df["user_id"] == user_id]["plan"].values[0]
        user_genre = genre_df[genre_df["user_id"] == user_id]["fav_genre"].values[0]
        user_rating = review_df[review_df["user_id"] == user_id]["rating"].mean()
        user_progress = watch_df[watch_df["user_id"] == user_id]["progress"].mean()
            
        user_content_data = {
            1: {"movie": "Shadow Protocol",
 "actor": "Will Smith",
        "movie_poster": "images/shadowprotocol.jpeg",
        "actor_img": "images/willsmith.jpeg",
        "actor_movies": ["Men in Black","I Am Legend","Gemini Man"],
        "similar_movies": ["Crimson Vengeance","The Hollow Manor","Hearts Entwined"]},
       
 2: {"movie": "Echoes of Silence", "actor": "Meryl Streep",
        "movie_poster": "images/echoesofsilencw.jpeg",
        "actor_img": "images/merylstreep.jpeg",
        "actor_movies": ["The Iron Lady","Kramer vs Kramer","The Devil Wears Prada"],
        "similar_movies": ["Forever and Always","Whispers in the Dark","Accidentally Perfect"]},
       
 3: {"movie": "Laugh Lines", "actor": "Jim Carrey",
        "movie_poster": "images/laughlines.jpeg",
        "actor_img": "images/jimcarrey.jpeg",
        "actor_movies": ["The Mask","Ace Ventura","Dumb and Dumber"],
        "similar_movies": ["Accidentally Perfect","Whispers in the Dark","Forever and Always"]},
      
  4: {"movie": "The Haunted Hour", "actor": "Jamie Lee Curtis",
        "movie_poster": "images/thehauntedhour.jpeg",
        "actor_img": "images/jamieleecurtis.jpeg",
        "actor_movies": ["Halloween","Freaky Friday","True Lies"],
        "similar_movies": ["Crimson Vengeance","Whispers in the Dark","The Hollow Manor"]},
    
    5: {"movie": "Hearts Entwined", "actor": "Julia Roberts",
        "movie_poster": "images/heartsentwined.jpeg",
        "actor_img": "images/juliaroberts.jpeg",
        "actor_movies": ["Pretty Woman","Erin Brockovich","My Best Friend's Wedding"],
        "similar_movies": ["Forever and Always","The Hollow Manor","Accidentally Perfect"]},
        6: {"movie": "Gemini Force", "actor": "Tom Hanks",
        "movie_poster": "images/geminiman.jpeg",
        "actor_img": "images/tomhanks.jpeg",
        "actor_movies": ["Forrest Gump","Cast Away","Saving Private Ryan"],
        "similar_movies": ["Shadow Protocol","Laugh Lines","Crimson Vengeance"]},
        7: {"movie": "Forever and Always", "actor": "Emma Stone",
        "movie_poster": "images/foreverandalways.jpeg",
        "actor_img": "images/emmastoen.jpeg",
        "actor_movies": ["La La Land","Easy A","The Favourite"],
        "similar_movies": ["Hearts Entwined","Accidentally Perfect","The Hollow Manor"]},
        8: {"movie": "Accidentally Perfect", "actor": "Leonardo DiCaprio",
        "movie_poster": "images/accidentlyperfect.jpeg",
        "actor_img": "images/leodicap.jpeg",
        "actor_movies": ["Inception","Titanic","The Revenant"],
        "similar_movies": ["Shadow Protocol","Laugh Lines","Forever and Always"]},
        9: {"movie": "Whispers in the Dark", "actor": "Scarlett Johansson",
        "movie_poster": "images/whispersinthedark.jpeg",
        "actor_img": "images/scarlettjohanson.jpeg",
        "actor_movies": ["Lucy","Marriage Story","Lost in Translation"],
        "similar_movies": ["Echoes of Silence","Hearts Entwined","Accidentally Perfect"]},
        10: {"movie": "Crimson Vengeance", "actor": "Brad Pitt",
         "movie_poster": "images/crimsonvengeance.jpeg",
         "actor_img": "images/bradpitt.jpeg",
         "actor_movies": ["Fight Club","World War Z","Once Upon a Time in Hollywood"],
         "similar_movies": ["Shadow Protocol","Gemini Force","Laugh Lines"]}
}

        st.markdown(f"**Subscription Plan:** {user_plan}")
        st.markdown(f"**Favourite Genre:** 🎞️ {user_genre}")
        st.markdown("---")

        # Compare user stats with global averages
        global_avg_rating = review_df["rating"].mean()
        global_avg_progress = watch_df["progress"].mean()
        


        st.subheader("🎥 Currently Watching")

        current = user_content_data[user_id]  # Fetch the logged-in user's current content

        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(current["movie_poster"], caption=current["movie"], use_column_width=True)
        with col2:
            st.markdown(f"### {current['movie']}")
            st.markdown(f"**Lead Actor:** {current['actor']}")
            st.image(current["actor_img"], width=150, caption=f"{current['actor']}")
            
            col1, col2 = st.columns(2)
            col1.metric("⭐ Your Avg Rating", f"{user_rating:.1f}", delta=f"{user_rating - global_avg_rating:+.1f} vs global")
            col2.metric("📺 Your Watch Completion (%)", f"{user_progress:.1f}%", delta=f"{user_progress - global_avg_progress:+.1f}% vs global")

# ============================
# RECOMMENDED CONTENT SECTION
# ============================
        st.markdown("---")
        st.subheader("✨ Recommended For You")

        recommended_titles = current["similar_movies"]
        
        poster_paths = {
    "Crimson Vengeance": "images/crimsonvengeance.jpeg",
    "The Hollow Manor": "images/thehallowmanor.jpeg",
    "Hearts Entwined": "images/heartsentwined.jpeg",
    "Forever and Always": "images/foreverandalways.jpeg",
    "Whispers in the Dark": "images/whispersinthedark.jpeg",
    "Accidentally Perfect": "images/accidentlyperfect.jpeg",
    "Men in Black":"images/meninblack.jpeg",
    "I Am Legend":"images/iamlegend.jpeg",
    "Gemini Man":"images/geminiman.jpeg"
}

        st.write("Because you liked:", current["movie"])

        cols = st.columns(len(recommended_titles))
        for i, title in enumerate(recommended_titles):
            with cols[i]:
                if title in poster_paths:
                    st.image(poster_paths[title], caption=title, use_column_width=True)
                else:
                    st.image("https://via.placeholder.com/150x220.png?text=No+Poster", caption=title, use_column_width=True)

# ============================
# ACTOR'S OTHER MOVIES SECTION
# ============================
        st.markdown("---")
        st.subheader(f"🎬 More from {current['actor']}")
        
        actor_movies = current["actor_movies"]
        
        poster={"Men in Black":"images/meninblack.jpeg",
        "I Am Legend":"images/iamlegend.jpeg",
        "Gemini Man":"images/geminiman.jpeg",
        "The Iron Lady":"images/theironlady.jpeg",
        "Kramer vs Kramer":"images/.jpeg",
        "The Devil Wears Prada":"images/thedevilwearsprada.jpeg",
"Fight Club":"images/thefightclub.jpeg",
"World War Z":"images/worldwarz.jpeg",
"Once Upon a Time in Hollywood":"images/onceuponatimeinhollywood.jpeg",
" Lucy":"images/lucy.jpeg",
"Marriage Story":"images/marriagestory.jpeg",
"Lost in Translation":"images/lostintranslation.jpeg",
"Inception":"images/inception.jpeg",
"Titanic":"images/titanic.jpeg",
"The Revenant":"images/therevenant.jpeg",
"La La Land":"images/.lalalandjpeg",
"Easy A":"images/.easyajpeg",
"The Favourite":"images/.thefavouritejpeg",
"Forrest Gump":"images/forrestgump.jpeg",
"Cast Away":"images/castaway.jpeg",
"Saving Private Ryan":"images/savingprivateryan.jpeg",
"Pretty Woman":"images/prettywoman.jpeg"
,"Erin Brockovich":"images/erinbrockovich.jpeg",
"My Best Friend's Wedding":"images/mybsfsbody.jpeg",
"Halloween":"images/halloweem.jpeg",
"Freaky Friday":"images/freakyfriday.jpeg",
"True Lies":"images/truelies.jpeg",
"The Mask":"images/themask.jpeg",
"Ace Ventura":"images/aceventura.jpeg",
"Dumb and Dumber":"images/dumbanddumber.jpeg"

        }
        
        cols = st.columns(len(actor_movies))
        for i, title in enumerate(actor_movies):
            with cols[i]:
                if title in poster:
                    st.image(poster[title], caption=title, use_column_width=True)
                else:
                    st.image("https://via.placeholder.com/150x220.png?text=No+Poster", caption=title, use_column_width=True)
                

      
        plan_df = pd.DataFrame({
    "user_id": [1,2,3,4,5,6,7,8,9,10],
    "plan": ["Basic","Standard","Basic","Premium","Basic","Standard","Premium","Basic","Standard","Premium"],
    "amount_paid": [39.96,44.97,39.96,59.97,39.96,44.97,59.97,39.96,44.97,59.97],
    "perks": ["Ads","HD","Ads","Ultra HD + Offline","Ads","HD","Ultra HD + Offline","Ads","HD","Ultra HD + Offline"],
    "next_payment_date": ["01/11/25"]*10,
    "device_type": ["Mobile","Laptop","Tablet","Smart TV","Laptop","Mobile","Smart TV","Tablet","Laptop","Smart TV"]
})
    
        
        
        import plotly.express as px

        st.markdown("### 🍩 Your Stats vs Global Average")

# Combine into a long-form dataframe for pie charts
        comparison_long = pd.DataFrame({
    "Metric": ["Average Rating", "Average Rating", "Watch Progress", "Watch Progress"],
    "Type": ["You", "Global Avg", "You", "Global Avg"],
    "Value": [user_rating, global_avg_rating, user_progress, global_avg_progress]
})

# Create two donut charts side by side
        col1, col2 = st.columns(2)

        with col1:
            fig1 = px.pie(
        comparison_long[comparison_long["Metric"] == "Average Rating"],
        names="Type",
        values="Value",
        title="⭐ Average Rating",
        color="Type",
        color_discrete_map={"You": "#4CAF50", "Global Avg": "#FFC107"},
        hole=0.5
    )
            fig1.update_traces(textinfo="label+percent", pull=[0.05, 0])
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            fig2 = px.pie(
        comparison_long[comparison_long["Metric"] == "Watch Progress"],
        names="Type",
        values="Value",
        title="📺 Watch Completion",
        color="Type",
        color_discrete_map={"You": "#4CAF50", "Global Avg": "#FFC107"},
        hole=0.5
    )
            fig2.update_traces(textinfo="label+percent", pull=[0.05, 0])
            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### 🎭 Other Users with Same Genre Preference")
        same_genre_users = genre_df[genre_df["fav_genre"] == user_genre].merge(users_df, on="user_id")[["name", "age"]]
        st.dataframe(same_genre_users)

        if st.button("🔓 Logout"):
            st.session_state.logged_in_user = None
            st.experimental_rerun()











