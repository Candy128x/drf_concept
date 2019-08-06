# Django REST Framework

---
## Software Requirements
- Python version: 3.7.3
- Django version: 2.2.3
- Django REST Framework version: 3.10.1


---
### For DRF Appn
- user: ashish
- pwd: qwerty


---
## Home page
	- hit http://localhost:8000
<kbd><img src="/imgs-readme/home_v1-1.png"></img></kbd>


---
## Insert data via API form [gif img]
	- hit http://localhost:8000/languages/
<kbd><img src="/imgs-readme/insert-data-api-form_v1-1.gif"></img></kbd>


---
## Listing Records
	- hit http://localhost:8000
<kbd><img src="/imgs-readme/listing_v1-1.png"></img></kbd>


---
## Listing HyperLinkModelSerializer Records
	- hit http://localhost:8000/languages/
<kbd><img src="/imgs-readme/hyperlink-model-serializer_v1-1.png"></img></kbd>


---
## Listing\Show Single Records
	- hit http://localhost:8000/languages/4/
<kbd><img src="/imgs-readme/select-single-data-set_v1-1.png"></img></kbd>


---
## Postman fetch all data
	- hit http://localhost:8000/languages
<kbd><img src="/imgs-readme/postman-get-or-select-all_v1-1.jpg"></img></kbd>


---
## Postman insert single set of data
	- hit http://localhost:8000/languages
<kbd><img src="/imgs-readme/postman-set-insert-single-data_v1-1.jpg"></img></kbd>


---
## Postman, Update single set of data
	- hit http://localhost:8000/languages
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 12-06-25.png"></img></kbd>


---
## Postman, Delete single set of data
	- hit http://localhost:8000/languages
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 12-13-05.png"></img></kbd>


---
## Postman, Disable edit feature for non-logedIn user (gif img)
	- hit http://localhost:8000/languages
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 12-22-24_v2-1.gif"></img></kbd><br>
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 12-13-05_v2-1.gif"></img></kbd>


---
## Postman, Disable update/edit feature for non-logedIn user
	- hit http://localhost:8000/languages
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 12-42-28.png"></img></kbd>


---
## User must be Authenticated
	- After add in `settting.py` file. code: 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 13-09-38.png"></img></kbd>

---
## Token generation
	- Hit localhost:8000/api/token/
	- for Debug token: https://jwt.io/
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 16-49-05.png"></img></kbd><br>
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 17-24-19.png"></img></kbd>


---
## Postman, Fetch all data using Token
	- Hit localhost:8000/languages/
<kbd><img src="/imgs-readme/Screenshot from 2019-08-06 17-31-46_v2-1.gif"></img></kbd>

