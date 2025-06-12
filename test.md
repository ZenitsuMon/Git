## Main page 

**Connection:**

- Choose connected ones 
- Add new one: 

    **Create a connection**
    - Connection name: 
    - Flow type: Authorization Code/ Implicit 
    - Authorize URI 
    - Token URI 
    - Scope: Add Item
    - Client ID 
    - Client Secret 
    - Show advanced settings 
        - Scope separator 
        - Authorize parameters: Add item (Additional authorize request parameters). 
        - Access token parameters: Add item (Additional access token request parameters). 
        - Refresh token parameters: Add item (Additional refresh token request parameters), 
        - Custom Headers: Add item 
        - Token placement: In the header/ In the query string/ In both the header and in the query string
        - Header token name: Bearer 
    
    **URL**: Enter text or type '/' to search 
    - Search items
    - Fill by AI: Describe the content of this field. (Remaining: 30 of 30 credits. Credits reset every 7 days. [Update for more](https://eu2.make.com/organization/4161390/subscription))
    - General functions 
        - Variables: executionID 
        - Functions: (), get, if, ifempty, switch, omit, pick 
        - Operators: =, !=, and, or 
        - Keywords: true, false, ignore, null, erase 
    - Math functions
        - Variables: pi, random 
        - Functions: average, ceil, floor, trunc, median, max, min, abs, round, sum, parseNumber, stdevS, stdevP, formatNumber
        - Operators: *, /, mod, +, -, <, >, <=, >=
    
    **Method**
    - Map: On/ Off
    - GET
    - HEAD
    - POST
    - PUT
    - PATCH
    - DELETE
    - OPTIONS

    **Headers**
    - Map: On/ Off 
    - Add a header 
    - Item 1 
        - Name 
        - Value 
    
    **Query String**
    - Map: On/ Off 
    - Add parameter 
    - Item 1 
        - Name 
        - Value 
    
    **Body type**
    - Empty
    - Raw
    - Application/ x-www-form-urlencoded
    - Multipart/ form-data

    **Parse Response** 
    
    - Automatically parses responses and converts JSON and XML responses so you don't need to use JSON or XML parser. Before you can use parsed JSON or XML content, run the module once manually so that the module can recognize the response content and allows you to map it in subsequent modules. 
    - Yes/ No 

    **Timeout**

    In seconds. Default: 300 seconds. This value controls two timeouts: Read timeout and Connection timeout. 
    
    Read timeout is a time to wait for a server to send response headers (and start the response body) before aborting the request.  

    Connection timeout sets the socket to timeout after timeout milliseconds of inactivity. 

    **Share cookies with other HTTP modules**

    Yes/ No (Why do we need to share cookies with other HTTP modules ? - keep the history ?)

    **Self-signed certificate**

    Upload your certificate if you want to use TLS using your self-signed certificate 

    Extract 
    - Extract: 
        - Certificate 
        - Private key 
    - P12, PFX or PEM file: 
        - Choose File: No file chosen 
    - Password: Provided file and password is only used to extract private key/certificate. We do not save anything on our servers. 

    **Reject connections that are using unverified (self-signed) certificates**
    - Yes/ No 

    **Follow redirect**
    - Yes/ No 

    **Follow all redirect**
    - Yes/ No
