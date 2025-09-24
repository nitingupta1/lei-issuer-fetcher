# LEI Issuer Fetcher & Cache Service (Python)

Fetches LEI Issuers from the given GLEIF API endpoint, handling pagination. It parses the JSON and extracts, for each issuer, at least these fields:  
-LEI code  
-Issuer name  
It also has in-memory cache implementation of 60 seconds for request coming to same endpoint. It also supports concurrent fetching of multiple pages, so it makes multiple requests to different endpoints/parameters at the same time.

## 1. Install packages

Open the root folder in VS Code. Then open the terminal. Run the below command:  
pip install -r requirements.txt

## 2. Run the API

fastapi dev app/main.py

Access the Swagger endpoint on http://127.0.0.1:8000/docs

There are two web methods in the API:

1. /issuers
2. /issuers/multipage

Test both the web methods using Swagger endpoint shown above.

## 3. Run the Integration tests

1. test_fetch_lei_issuers_real_api  
   This test checks the actual business logic and makes a call to the real API endpoint.

2. test_fetch_lei_issuers_multiple_pages_real_api  
   This test makes the call to real API endpoint and tests for multiple pages logic.

3. test_concurrent_fetch_is_faster  
   This test is performance test and shows concurrent call takes less time than in-sequence multiple calls.

4. test_cache_set_and_get  
   This test checks the memory cache is accessible and data can be stored in it and accessed from it.

5. test_cache_expiry  
   This test checks for the cache expiry once time duration completes.

Run all the above tests using below command in terminal from the root folder of the project.
python -m pytest -v
