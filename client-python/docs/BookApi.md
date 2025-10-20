# swagger_client.BookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_book**](BookApi.md#create_book) | **POST** /v1/book | 
[**delete_book**](BookApi.md#delete_book) | **DELETE** /v1/book/{bookID} | 
[**get_book**](BookApi.md#get_book) | **GET** /v1/book/{bookID} | 
[**list_books**](BookApi.md#list_books) | **GET** /v1/book | 
[**update_book**](BookApi.md#update_book) | **PUT** /v1/book/{bookID} | 


# **create_book**
> CreateBookResponse create_book(book)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
book = swagger_client.CreateBookRequest() # CreateBookRequest | 

try:
    api_response = api_instance.create_book(book)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->create_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book** | [**CreateBookRequest**](CreateBookRequest.md)|  | 

### Return type

[**CreateBookResponse**](CreateBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_book**
> DeleteBookResponse delete_book(book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
book_id = 'book_id_example' # str | 

try:
    api_response = api_instance.delete_book(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->delete_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | 

### Return type

[**DeleteBookResponse**](DeleteBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_book**
> Book get_book(book_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
book_id = 'book_id_example' # str | 

try:
    api_response = api_instance.get_book(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->get_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_books**
> ListBooksResponse list_books()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()

try:
    api_response = api_instance.list_books()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->list_books: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListBooksResponse**](ListBooksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_book**
> Book update_book(book_id, book)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookApi()
book_id = 'book_id_example' # str | 
book = swagger_client.CreateBookRequest() # CreateBookRequest | 

try:
    api_response = api_instance.update_book(book_id, book)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookApi->update_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **str**|  | 
 **book** | [**CreateBookRequest**](CreateBookRequest.md)|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

