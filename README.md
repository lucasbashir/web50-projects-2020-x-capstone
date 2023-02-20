Distinctiveness and Complexity

This code is a Django web application for submitting and viewing alerts about criminal activities in different states and local government areas (LGA) in Nigeria. 

With reported criminal activities saved in the database, the databse can be queried to keep track
of what category of crime is rampant in a given location thus giving law enforcements officers better insight into understanding how to tackle crime.


The application has features for registering new users, logging in, and creating alerts. It also includes a notification system that broadcasts new alerts to all active users of the application.(To be updated)

The code includes several views, each with its own unique functionality. The index() function renders the main page of the application, while all_alerts() lists all the alerts submitted to the application. The new_alert() function is responsible for creating new alerts, and the login_view() and logout_view() functions handle the user authentication process.

The register() function handles new user registration, which includes validating input fields, such as the email and password fields, and checking if the email is unique in the database. The register() function also creates a new user account if the email is unique.

The Alert model defines the structure of the alerts created in the application. It includes fields for the user submitting the alert, the content of the alert, the date and time the alert was created, and the state and LGA where the incident occurred. The category field is used to specify the type of crime that occurred, such as theft or assault.

The code uses Django's built-in authentication system, which provides user authentication, login, and logout functionalities. It also uses Django's paginator module to display the alerts in the all_alerts() view. The paginator module ensures that only a fixed number of alerts are displayed on a single page, making it easier to navigate through the alerts.

The code also includes a WebSocket-based notification system that broadcasts new alerts to all active users of the application. The notification system uses Django Channels to manage the WebSocket connections and handle communication between the clients and the server.

The notification system works by creating a WebSocket connection between the client and the server. When a new alert is submitted to the application, the server broadcasts the alert to all active WebSocket connections, and the clients receive the notification. The notification system ensures that all clients receive the notification in real-time, making it easier for users to stay up-to-date with the latest alerts.

In terms of distinctiveness, this application provides a unique platform for people to report criminal activities in their community. The code is easy to navigate, with well-structured views and a clean user interface. The notification system is a unique feature that sets the application apart from other similar applications.

In terms of complexity, the code is relatively simple and easy to understand, with only a few views and a single model. The code uses Django's built-in authentication system, making it easier to manage user accounts and handle user authentication. The notification system is the most complex part of the code, but it uses well-documented Django Channels and is relatively straightforward to implement.

Overall, this code is a unique and straightforward web application that provides a platform for people to report criminal activities in their community. The code is well-structured, easy to understand, and includes several useful features such as user authentication, alerts creation, and a real-time notification system.

Contribute

If you would like to contribute to this project, you can fork the repository and make necessary changes. After making changes, submit a pull request with a brief description of the changes made. Your contributions are always welcome!

Credits
This project was developed by me, Samson Lukman. Thanks to David Malan, Brian You and Doug Lloyd at Harvard's CS50.