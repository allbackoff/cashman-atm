# cashman-atm
REST API for an ATM-style cash dispensing application

## How to build and run the application

Docker was used to set up the automatic build for this project.

You can run the application by pulling from Docker Hub:

`$docker run -d -p 8000:8000 allbackoff/cashman-atm`

This executes automated tests and then builds the application.

Now, you can access it by going to `127.0.0.1:8000/atm/`

There you will see the list of endpoints which you can visit to check the functions.

## Libraries used

Other than the core Django framework, I used the Django Rest Framework. 

I made this choice so that I can concentrate on pure back-end work with REST API principles.
