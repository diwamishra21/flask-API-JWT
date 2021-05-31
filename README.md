# flask-API-JWT
This project is a simple flask API to authorize users using JWT(JSON Web Tokens). User can access public API directly but after login they needed token to use private APIs. This is a standard way to secure your API from unauthorize access.

## prerequisites-
- python
- Flask

## Details-
- Flask api with JWT Token
- protected URLs can only be accessible using token

## Running this Project
- Download and Install python
- Install Flask using command - pip install flask
- extract this repository or clone it.
- go inside project directory and run command- python api.py
- in cmd you will get URL of project i.e. http://localhost:5000
- try both APIs in your favourite browser using URLs-
- Access URLs on brpwser-
  http://localhost:5000/unprotected
  http://localhost:5000/login (Username- admin, Password- secret)
  in response you will get a token, Use this token using GET method to access protected Data
  http://localhost:5000/protected?token=<your token>

# Pictorial View

## Running App View -
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-app-run.png)

## Public/unprotected API -
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-unprotected.png)

## Accessing protected API without token -
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-protected-token-missing.png)

## Login API -
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-login.png)

## Login API Response-
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-token-response.png)

## Protected API Response using Token-
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-protected-response.png)

## Lets use Postman for same

## Postman Login API -
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-login-postman.png)

## Postman Protected API Response using Token-
![alt text](https://github.com/diwamishra21/flask-API-JWT/blob/main/images-for-git-readme/API-protected-response-postman.png)

Thanks for Visiting :pray:
