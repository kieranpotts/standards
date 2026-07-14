<h2 id="controller-resource">Controller Resources</h2>

#### HTTP Status Codes For Controller Resources

Following sections provide some examples for modeling of controller resources to
carry out various kinds of complex operations.

<h4 id="complex-operation-sub-resource">Complex Operation - Sub-Resource</h4>

_NOTE: Use with caution_

_For associated risks, see [Controller Resource](#controller-resource) above_

There are often situations in which a canonical resource needs to impart certain
actions or state changes which are not appropriate in a `PUT` or `PATCH`. These
URIs look like other Sub-Resources, but imply action.

A good use for this pattern is when a particular state change requires a
"comment" (e.g. cancellation "reason"). Adding this comment, or other data such
as location, would make the `GET`/`PUT` unnecessarily include those extra fields
on every request/response. This action may change the status of the given
resource implicitly.

Additionally, when a resource identifier is required for an action, it's best to
keep it in the URL. Some actions are business processes which are not innately a
resource (and in some cases might not even change resource state).

The response is typically `200 OK` and the resource itself, if there are changes
expected in the resource the consumer needs to capture. However, if no resource
state change occurs, `204 No Content` and no response body could also be
considered appropriate.

##### URI Template

    POST /{version}/{namespace}/{resource}/{resource-id}/{complex-operation}

###### Example Request

```
POST /v1/payments/billing-agreements/I-0LN988D3JACS/suspend
{
    "note": "Suspending the agreement."
}
```

###### Example Response

```
204 No Content
```

However, when state changes are imparted in this manner, it does not mean that
all state changes for the given resource should use a complex operation. Simple
state transitions (i.e. changes to a `status` field) should still utilize
`PUT`/`PATCH`. It is completely appropriate to mix patterns using `PUT`/`PATCH`
on a [Collection Resource](#collection-resource) + Complex Operation, as to
minimize the number of operations.

###### Example Request (for mixed use of `PUT`)

```
PATCH /v1/payments/billing-agreements/I-0LN988D3JACS
[
    {
        "op": "replace",
        "path": "/",
        "value": {
            "description": "New Description",
            "shipping_address": {
                "line1": "2065 Hamilton Ave",
                "city": "San Jose",
                "state": "CA",
                "postal_code": "95125",
                "country_code": "US"
            }
        }
    }
]
```

Keep in mind that if there is any need to see the history of these actions, a
[Sub-resource Collection](#sub-resource-collection) is appropriate to show all
of the prior executions of this action. In that case, the verb should be
[_reified_](<http://en.wikipedia.org/wiki/Reification_(computer_science)'>), or
changed to a plural noun (e.g. 'execute' would become 'executions').

<h4 id="complex-operation-composite">Complex Operation - Composite</h4>

This type of complex operation creates/updates/deletes multiple resources in one
operation. This serves as both a performance and usability optimization, as well
as adding better atomicity when values in the request might affect multiple
resources at the same time.

Note in the sample below, the capture and the payment are both potentially
affected by refund. A `PUT` or `PATCH` operation on the capture resource would
have unintended side effects on the payment resource. To encapsulate both of
these changes, the 'refund' action is used.

##### URI Template

    POST /{version}/{namespace}/{action}

##### Example Request

```
POST /v1/payments/captures/{capture-id}/refund
```

##### Example Response

```
{
    "id": "0P209507D6694645N",
    "create_time": "2013-05-06T22:11:51Z",
    "update_time": "2013-05-06T22:11:51Z",
    "state": "completed",
    "amount": {
        "total": "110.54",
        "currency": "USD"
    },
    "capture_id": "8F148933LY9388354",
    "parent_payment": "PAY-8PT597110X687430LKGECATA",
    "links": [
        {
            "href": "https://api.foo.com/v1/payments/refund/0P209507D6694645N",
            "rel": "self",
            "method": "GET"
        },
        {
            "href": "https://api.foo.com/v1/payments/payment/PAY-8PT597110X687430LKGECATA",
            "rel": "parent_payment",
            "method": "GET"
        },
        {
            "href": "https://api.foo.com/v1/payments/capture/8F148933LY9388354",
            "rel": "capture",
            "method": "GET"
        }
    ]
}
```

<h4 id="complex-operation-transient">Complex Operation - Transient</h4>

This type of complex operation does not maintain state for the client, and
creates no resources. This is about as RPC as it gets; other alternatives should
be considered first.

This is not usually utilized in sub-resources, as a sub-resource action would
typically affect the parent resource.

HTTP status `200 OK` is always appropriate. Response body contains calculated
values, which could potentially change if run again.

As with all actions, [resource-oriented alternatives](##controller-alternative)
should be considered first.

##### URI Template

    POST /{version}/{namespace}/{action}

##### Example Request

    POST /v1/risk/evaluate-payment
    {
    	"code": "h43j5k6iop"
    }

###### Example Response

    200 OK
    {
    	"status": "VALID"
    }

<h4 id="complex-operation-search">Complex Operation - Search</h4>

When [Collection Resources](#collection-resource) are used, it is best to use
query parameters on the collection to filter the set. However, there are some
situations that demand a very complex search syntax, where query parameter
filtering on a collection might present usability problems, or run up against
theoretical query parameter length limitations.

In these situations, `POST` can be utilized with a request object to specify the
search parameters.

##### Pagination

Assuming pagination will be required with large response quantities, it is
important to remember that the consumer will need to use `POST` on each
subsequent page. As such, it's important to maintain paging in the query
parameters (one of the rare exceptions where `POST` body + query parameters are
utilized).

Paging query parameters should follow the same conventions as in
[Collection Resources](#pagination).

This allows for hypermedia links to provide `next`, `previous`, `first`, `last`
page relationships with paging specified in the URL.

##### URI Template

    POST /{version}/{namespace}/{search-resource}

##### Example Request

    POST /v1/factory/widgets-search
    {
    	"created_before":"1975-05-13",
    	"status": "ACTIVE",
    	"vendor": "Parts Inc."
    }

##### Example Response

    200 OK
    {
    	"items": [
    		<<lots of part objects here>>
    	]
    	"links": [
                {
                    "href": "https://api.sandbox.factory.io/v1/factory/widgets-search?page=2&page_size=10",
                    "rel": "next",
                    "method": "POST"
                },
    			{
                    "href": "https://api.sandbox.factory.io/v1/factory/widgets-search?page=124&page_size=10",
                    "rel": "last",
                    "method": "POST"
                },
    	]
    }

<h2 id="controller-alternative">Resource-Oriented Alternative</h2>

A better pattern is to create a [Collection Resource](#collection-resource) of
actions and provide a history of those actions taken in `GET /{actions}`. This
allows for future expansion of use cases around a resource model, instead of a
single action-oriented, RPC-style URL.

Additionally, for various use cases, filtering the resource collection of
historical actions is usually desirable. This also feeds well into
[event sourcing](http://martinfowler.com/eaaDev/EventSourcing.html) concepts,
where the history of a given event can drive further functionality.

<h2 id="file-uploads">File Upload</h2>

Certains types of API operations require uploading a file (e.g. jpeg, png, pdf)
as part of the API call. Services for such use cases, MUST not support or allow
encoding the file content within a JSON body using `Base64` encoding.

For uploading a file, one of the following options SHOULD be used.

<h4 id="fileuploads-two-step">Standalone Operation</h4>

Services supporting such an operation SHOULD provide a separate dedicated URI
for uploading and retrieving the files. Clients of such services upload the
files using the file upload URI and retrieve the file metadata as part of the
response to an upload operation.

Format of the file upload request SHOULD conform to `multipart/form-data`
content type ([RFC 2388](https://www.ietf.org/rfc/rfc2388.txt)).

**Example of a** `multipart/form-data` **request**:

_The client first uploads the file using a file-upload URI provided by the
service._

```

POST /v1/identity/limit-resolution-files

Content-Type: multipart/form-data; boundary=--foo_bar_baz
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
MIME-Version: 1.0

--foo_bar_baz
Content-Type: text/plain
Content-Disposition: form-data; name="title"

Identity Document
--foo_bar_baz
Content-Type: image/jpeg
Content-Disposition: form-data; filename="passport.jpg"; name="artifact"

...(binary bytes of the image)...
--foo_bar_baz--
```

**Sample file upload response:**

_If the file upload is successful, the server responds with the metadata of the
uploaded file._

```
{
    "id": "file_egflf465vbk7468mvnb",
    "created_at": 748557607545,
    "size" : 3457689458369,
    "url" : "https://api.foo.com/v1/files/file_egflf465vbk7468mvnb"
    "type" : "image/jpeg"
}
```

The client can use the uploaded file's URI (received in the above response) for
any subsequent operation that requires the uploaded file as shown below.

**Example Request**

```
POST /v1/identity/limits-resolutions
Host: api.foo.com
Content-Type: application/json
Authorization: Bearer oauth2_token

{
    ...
    "identity_document_reference" : "https://api.foo.com/v1/files/file_egflf465vbk7468mvnb"

}
```

<h4 id="fileuploads-one-step">As Attachment</h4>

This option SHOULD be used if you have to combine the uploading of a file with
an API request body or parameters in one API request (e.g. for the purpose of
optimization or to process both the file upload and request data in an atomic
manner).

For such use cases, the request SHOULD either use content-type `multipart/mixed`
or `multipart/related` ([RFC 2387](https://tools.ietf.org/html/rfc2387)).
Following is an example of such a request.

**Example of a** `multipart/related` **request**:

_The first part in the below multipart request is the request metadata, while
the second part contains the binary file content_

```
POST /v1/identity/limits-resolutions
Host: api.foo.com
Content-Type: multipart/related; boundary=--foo_bar_baz
Authorization: Bearer oauth2_token

--foo_bar_baz
Content-Type: application/json; charset=UTF-8

{
  ...
}

--foo_bar_baz
Content-Type: image/jpeg

[JPEG_DATA]
--foo_bar_baz--

```

<h1 id="hateoas-use-cases">HATEOAS Use Cases</h1>

This section describes various use cases where HATEOAS could be used.

As a guiding principle, every API SHOULD strive for a single entry point. Any
response from this entry point will have [HATEOAS](index.md#hateoas) links using
which the client can navigate to all other methods on the same resource or
releated resources and sub-resources. Following are different patterns for
defining such an API entry point.

<h4>Pattern 1: API with a top level entry point</h4>

For most APIs, there's a natural top level object or a collection which can be
the resources addressed by the entry point. For example, the API defined in the
previous section has a collection resource `/users` which can be the entry point
URI.

<h4>Pattern 2: Entry point for complex controller style operations</h4>

A complex multi step operation always has a logical entry point. For example,
you want to build an API for a credit application process that involves multiple
steps- a create application step, consumer consent step (to sign, agree to terms
and conditions), an approval step- the last step of a successful credit
application.

- `/apply-credit` is the API's entry point. All other steps would be guided by
  the application create step in the from of links based on the captured data.
  For example a successful create application step would return the link to the
  next state of the application process `apply.sign`.
- An unsuccessful (application with incorrect data) MAY return only a link to
  send only the incorrect/missing data (e.g `PATCH` link).

<h4>Pattern 3: API without a top level entry point</h4>

Consider an API that provides a set of independent controller style utility
methods. For example, you want to build an identity API that provides the
following utility methods.

- generate OTP (one time password)
- encrypt payload using a particular algorithm
- decrypt the payload, link tokens

For such cases, the API MAY provide a separate resource `/actions` to return
links to all resources that can be served by this API.

`GET /actions` in the above example would return links to other api methods
(`/generate-otp`,`/encrypt`,`/decrypt`,`/link-tokens`).

<h2 id="collection-links">Navigating A Collection</h2>

For collection resources, a service MAY automatically provide paginated
collection. Client can also specify its pagination preferences, if the query
resultset is quite large. In such cases, the resultset is returned as a
paginated collection with appropriate pagination related links. Client utilizes
these links to navigate through the resultset back-and-forth. For more details
on this linking pattern, please refer to
[Pagination and HATEOAS links](#page-navigation).

<h2 id="error-links">Error Resolution</h2>

There are often use cases where an API wants to provide additional context in
case of error along with other error details (HTTP status code and error
messages. See [Error Standards](errors.md#errors) for more). An API could return
additional resource links to provide more hints on the error in order to resolve
it.

Consider an example from the `/users` API where the user wants to update his
address details.

**Request**:

```

PATCH /v1/users/ALT-JFWXHGUV7VI

{
    "address": {
        ...
    }
}

```

The service, however, finds that the user account is currently not active. So it
responds with an error that update of this account is not possible given the
current state. It also returns an HATEOAS link in the response to activate the
user account.

**Response**:

```
HTTP/1.1 422 Unprocessable Entity
{
    "name":"INVALID_OPERATION",
    "debug_id":"123456789",
    "message":"update to an inactive account is not supported",
    "links": [
        {
            "href": "https://api.foo.com/v1/customer/partner-referrals/ALT-JFWXHGUV7VI/activate",
            "rel": "activate",
            "method": "POST"
        }
    ]
}

```

The client can now prompt the user to first activate his account and then change
his address details.

<h2 id="service-controlled-flow">Service-controlled Flow</h2>

In a complex business operation that has one or more sub business operations and
business rules govern the state transitions at run-time, using HATEOAS links to
describe or emit the allowed state transitions prevents clients from embedding
the service-specific business logic into their code. Loose coupling or no
coupling with server's business logic enables better evolvability for both
client and server.

For example, an order can be cancelled when it is in a PENDING state. The order
cannot be cancelled once it moves to a COMPLETED state. Following example shows
how a service can use HATEOAS links to guide clients about next possible step(s)
in business process.

<h3>Example: Pending Order</h3>

Order is in PENDING state so the services returns the `cancel` HATEOAS link.

###### Request

```
GET v1/checkout/orders/52181732T9513405D HTTP/1.1
Host: api.foo.com
Content-Type: application/json
Authorization: Bearer oauth2_token
```

###### Response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "payment_details":{
        ...
    },
    "status":"PENDING",
    "links":[
        {
            "rel": "self",
            "href": "https://api.foo.com/v1/checkout/orders/19S86694A9334040A",
            "method": "GET"
        },
        {
            "rel": "cancel",
            "href": "https://api.foo.com/v1/checkout/orders/19S86694A9334040A/cancel",
            "method": "POST"
        }
     ]
}
```

<h3>Example: Completed Order</h3>

Order is in COMPLETED state so the services does not return the `cancel` link
anymore.

###### Request

```
GET v1/checkout/orders/52181732T9513405D HTTP/1.1
Host: api.foo.com
Content-Type: application/json
Authorization: Bearer oauth2_token
```

###### Response

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "payment_details":{
        ...
    },
    "status":"COMPLETED",
    "links":[
        {
            "rel": "self",
            "href": "https://api.foo.com/v1/checkout/orders/19S86694A9334040A",
            "method": "GET"
        }
     ]
}
```

Note: The service MAY decide to support cancellation of orders (for orders with
COMPLETED status) in some countries in future but that does not require the
client to change anything in its code. All that a client knows or has coded when
it first integrated with the service is the request body that is required to
`cancel` an order.

<h2 id="hateoas-asynchronous-operations">Asynchronous Operations</h2>

When an operation is carried out asynchronously, it is important to provide
relevant links to client so that the client can find out more details about the
operation such as finding out status or perform get, update and delete
operations. Please refer to [Asynchronous Operations](#asynchronous-operations)
to find how the HATEOAS links could be used in response of an asynchronous
operation.

<h2 id="saving-bandwidth">Saving Bandwidth</h2>

Some services always return very large response because of the nature of the
domain they address. APIs of such services are sometimes referred as `Composite`
APIs (they accumulate data from various sources or an aggregate of more than one
services). For such APIs, sending the entire response drastically impacts
performance of the API consumer, API server and the underlying network. In such
cases, the client can ask the service to return partial representation using
[`Prefer: return=minimal`](index.md#http-standard-headers) HTTP header. A
service could send response with relevant HATEOAS links with minimal data to
improve the performance.

<h1 id="bulk-operations">Bulk Operations</h1>

This section describes guidelines for handling bulk calls in APIs. There are two
different methods that you could use for bulk processing.

- **Homogeneous:** operation involves request and response payload representing
  collection of resources of the same type. Same operation is applied on all
  items in the collection.

- **Heterogeneous:** ~~operation involves a request and response payloads that
  contain one or more requests and reponse payloads respectively. Each nested
  request and response represents an operation on a specific type of resource.
  However, the container request and response have one or more operations
  operating on one or more types of resources. It is recommended to use a public
  domain standard such as _[OData Batch Specification] [1]_ in such cases.~~ We
  do not recommend heterogeneous operations within Sysco API eco system. Please
  revert to SyscoLABS EAG for any assistance.

This section only addresses bulk processing of payloads using the homogenous
method.

<h2 id="bulk-request-format">Request Format</h2>

Each bulk request is a single HTTP request to one target API endpoint. This
example illustrates a bulk add operation.

**Example Request:**

```
POST /v1/devices/cards HTTP/1.1
Host: api.foo.com
Content-Length: total_content_length

{
	...

  	"items": [
	{
		"account_number": "2097094104180012037",
		"address_id": "466354",
		"phone_id": "0",
		"first_name": "M",
		"last_name": "Shriver",
		"primary_card_holder": false
	},
 	{
		"account_number": "2097094104180012047",
		"address_id": "466354",
		"phone_id": "0",
		"first_name": "M",
		"last_name": "Shriver",
		"primary_card_holder": false
	},
 	{
		"account_number": "2097094104180012023",
		"address_id": "466354",
		"phone_id": "0",
		"first_name": "M",
		"last_name": "Shriver",
		"primary_card_holder": false
	}
	]
}
```

<h2 id="bulk-response">Response Format</h2>

The response usually contains the status of each item. Failure of an individual
item is described using
_[Error Handling Guidelines](index.md#sampleresponse-bulk)_ for an individual
item. Given below is such an example.

**Example Response:**

```
HTTP/1.1 200 OK

{
  ...

  "batch_result":[
	{
		… <Success_body>
	},
	{
  		"name": "VALIDATION_ERROR",
   		"details": [
   		    {
   		        "field": "#/credit_card/expire_month",
   		        "issue": "Required field is missing",
   		        "location": "body"
   		    }
   		],
   		"debug_id": "123456789",
   		"message": "Invalid data provided",
   		"information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
	},

	{
   		"name": "VALIDATION_ERROR",
   		"details": [
   		    {
       	                "field":"#/credit_card/currency",
                        "value":"XYZ",
                        "issue":"Currency code is invalid",
                        "location":"body"
                    }
   		],
   		"debug_id": "123456789",
   		"message": "Invalid data provided",
   		"information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
	}
 ]
}
```

If the API supports atomic semantics to processing requests, there would be a
single response code for the entire request with one or more errors as
applicable.

**Example Response:**

**Note**:

```
HTTP/1.1 400 Bad Request

{
   "name": "VALIDATION_ERROR",
   "details": [
      {
         "field": "#/credit_card/currency",
         "value": "XYZ",
         "issue": "Currency code is invalid",
         "location": "body"
      }
   ],
   "debug_id": "123456789",
   "message": "Invalid data provided",
   "information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
}
]
```

<h2 id="bulk-other">Replace And Update</h2>

Similar to bulk add, a service can support bulk update operation (replace using
HTTP `PUT` or partial update using `PATCH`). This is possible provided the bulk
add request also creates a first-class resource (e.g. a batch resource) that is
uniquely identifiable using an id and returned to the client. The subsequent
update operations could then use this id and perform updates on constituent
elements of the batch as if an update is performed on a single resource.

For bulk replace and update operations, every effort should be made to make the
execution atomic (all or nothing semantics). When it is not possible to make it
so, the response should be similar to the partial response of bulk add operation
described in the previous section.

<h2 id="bulk-status-code">HTTP Status Codes And Error Handling</h2>

Tne following guidelines describe HTTP status code and error handling for bulk
operations.

- If atomicity is supported (all or nothing), use the regular REST API standards
  for error handling as there would be only one response code.
- To support partial failures, you MUST return `200 OK` as the overall bulk
  processing status with individual status of each bulk item. In case of an
  error while processing a bulk item, the error description MUST follow the
  Error Handling Guidelines.
- If asynchronous processing is supported, the API MUST return `202 Accepted`
  with a status URI for the client to monitor the request. The client may choose
  to ignore the status URI if it has registered itself with the API server for
  notification via webhooks.

<h2 id="bulk-correlation">Response-Request Correlation in Error Scenarios</h2>

For a failed item, you MAY use the
_[JSON Pointer Expressions](#json-pointer-expression)_ in the error response for
that item using the `field` attribute of [`error.json`][2]. The caller can then
map a response item's processing state to the exact request item in the original
bulk request. Given below is an error response sample using the JSON Pointer
Expressions.

**Error Response Sample:**

```

HTTP/1.1 200 OK

[
{
	… <Success_body>
},

{
   "name": "VALIDATION_ERROR",
   "details": [
      {
         "field": "/items/@account_number=='2097094104180012047'/address_id",
         "issue": "Invalid Address Id for the account",
         "location": "body"
      }
   ],
   "debug_id": "123456789",
   "message": "Invalid data provided",
   "information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
},

{
   "name": "VALIDATION_ERROR",
   "details": [
   {
       "field": "/items/@account_number=='2097094104180012023'/phone_id",
       "value": "XYZ",
       "issue": "Phone Id is invalid",
       "location": "body"
   }
   ],
   "debug_id": "123456789",
   "message": "Invalid data provided",
   "information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
}
]

```

The alternative is to create a response that contains the processing status of
each item **in the same order** as it was received in the original request. The
failed item would be represented using `error.json` with appropriate value in
the `field` attribute.

**Error Response Sample:**

```

HTTP/1.1 200 OK

[
{
	… <Success_body>
},

{
   "name": "VALIDATION_ERROR",
   "details": [
      {
         "field": "/items/0/address_id",
         "issue": "Invalid Address Id for the account",
         "location": "body"
      }
   ],
   "debug_id": "123456789",
   "message": "Invalid data provided",
   "information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
},

{
   "name": "VALIDATION_ERROR",
   "details": [
   {
       "field": "/items/2/phone_id",
       "value": "XYZ",
       "issue": "Phone Id is invalid",
       "location": "body"
   }
   ],
   "debug_id": "123456789",
   "message": "Invalid data provided",
   "information_link": "http://developer.foo.com/apidoc/blah#VALIDATION_ERROR"
}
]

```

<h3 id="other">Other Patterns</h3>

Designers of new services SHOULD refer to the [_RESTful Web Services
Cookbook_][4] at Safari Books Online for other useful patterns.

[1]:
  http://www.odata.org/documentation/odata-version-3-0/batch-processing/
  "OData Batch Specification"
[2]: v1/schema/json/draft-04/error.json "error.json"
[4]:
  http://techbus.safaribooksonline.com/book/web-development/web-services/9780596809140
  "RESTful Web Services Cookbook"
[5]: https://www.w3.org/TR/NOTE-datetime "ISO 8601 Date and Time Formats"
[6]: http://tools.ietf.org/html/rfc6902 "RFC 6902"
