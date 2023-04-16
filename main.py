import razorpay
from flask import Flask, render_template, redirect, request

app=Flask(__name__)
client = razorpay.Client(auth=("rzp_id", "rzp_secret key"))
@app.route('/')
def func_name():
    return render_template('form.html')

@app.route('/pay', methods=["GET", "POST"])
def pay():
    if request.form.get("amount") != "":
        amount=request.form.get("amt")
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        pdata=[amount, payment["id"]]
        return render_template("index.html", pdata=pdata)
    return redirect("/")

@app.route('/success', methods=["POST"])
def success():
    pid=request.form.get("razorpay_payment_id")
    ordid=request.form.get("razorpay_order_id")
    sign=request.form.get("razorpay_signature")
    print(f"The payment id : {pid}, order id : {ordid} and signature : {sign}")
    params={
    'razorpay_order_id': ordid,
    'razorpay_payment_id': pid,
    'razorpay_signature': sign
    }
    final=client.utility.verify_payment_signature(params)
    if final == True:
        return redirect("/", code=301)
    return "Something Went Wrong Please Try Again"


app.run(debug=True)