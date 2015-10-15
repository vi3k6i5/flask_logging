# flask_logging
logging across files in flask project

### to run the app locally use this command 

    PYTHONPATH=. python app.py runserver


### to make a call to the service use this command

  curl -X GET "localhost:5000/v1/status"

  {
    "data": "SUCCESSFUL"
  }
  
### Log message in the file.log

it will look somewhat like this:

 2015-10-15 17:49:05,795 INFO: hi [in /tmp/app/helper.py:5]
 
