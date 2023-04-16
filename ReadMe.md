# RazorPay Integration In Flask (Python)

Razorpay SDK based payment integration in Flask (Python) with Callback URL Redirection on payment signature verification.

## Installation
```
pip install razorpay
```

## Update Your Razorpay Credentials
##### [Main.py]("https://github.com/Subhamsaurav/razorpay-flask-integration/blob/master/main.py")  &nbsp;Line 5

```
client = razorpay.Client(auth=("rzp_id", "rzp_secret key"))
```
##### [Index.html]("https://github.com/Subhamsaurav/razorpay-flask-integration/blob/master/main.py")  &nbsp;Line 5

```
"key": "rzp_id"
```
## Change User Data
##### [Index.html]("https://github.com/Subhamsaurav/razorpay-flask-integration/blob/master/main.py")  &nbsp;Line 13-17
```
    "prefill": {
        "name": "Gaurav Kumar",
        "email": "gaurav.kumar@example.com",
        "contact": "9000090000"
    },
```

## Running Tests
```
python main.py
```

## Issues? Changes?
Just open an issue/pull requests