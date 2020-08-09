import sys
import os
import request
import requests
from FareEstimator import Fare_Details
from flask import Flask, render_template, request,redirect,session,url_for
app = Flask(__name__)
sys.path.append("/InCityProject")

@app.route("/")
def index():
    return render_template("HomePage.html")

@app.route("/Estimated_Fare", methods = ["POST"])
def Estimated_Fare():
    if request.method == "POST":
        global Input_Data
        global microdict
        global minidict
        global jumbodict
        Input_Data = dict()
        L1 = ["Source","Destinetion","Distance","Time","Helper_Amount","Insurance_Amount","Discount"]
        source = str(request.form["Source"])
        destinetion = str(request.form["Destinetion"])
        print(source)
        print(destinetion)
        distance = float(request.form['Distance'])
        print(distance)
        time = float(request.form["Time"])
        print(time)
        helper_amount = float(request.form["Helper_Amount"])
        print(helper_amount)
        insurance_amount = float(request.form["Insurance_Amount"])
        print(insurance_amount)
        Discount = float(request.form["Discount"])
        L2 = [source,destinetion,distance,time,helper_amount,insurance_amount,Discount]
        Input_Data = {L1 : L2 for L1, L2 in zip(L1,L2)}
        micro_data = Fare_Details(Input_Data)
        microdict = micro_data.Fare_Details_Micro()
        mini_data = Fare_Details(Input_Data)
        minidict = mini_data.Fare_Details_Mini()
        jumbo_data = Fare_Details(Input_Data)
        jumbodict = jumbo_data.Fare_Details_Jumbo()
        return render_template("Estimated_Fare.html", input_data_micro = microdict, input_data_mini = minidict, input_data_jumbo = jumbodict)


@app.route("/Micro_Page", methods = ["POST"])
def Micro_Page():
    if request.method == "POST":
        return render_template("Micro_Page.html",microdict = microdict, Input_Data = Input_Data)

@app.route("/Mini_Page", methods = ["POST"])
def Mini_Page():
    if request.method == "POST":
        return render_template("Mini_Page.html", minidict = minidict)


@app.route("/Jumbo_Page", methods = ["POST"])
def Jumbo_Page():
    if request.method == "POST":
        return render_template("Jumbo_Page.html", jumbodict = jumbodict)

@app.route("/Additional_Data_Micro",methods = ["POST"])
def Additional_Data_Micro():
    if request.method == "POST":
        global dictionary
        dictionary = dict()
        Trip_ID = str(request.form["Trip_ID"])
        print(Trip_ID)
        Customer_Details = str(request.form["C_Details"])
        print(Customer_Details)
        Driver_Name = str(request.form["D_Name"])
        print(Driver_Name)
        Driver_Number = request.form["D_Number"]
        print(Driver_Number)
        Payment_Mode = str(request.form["Payment_Mode"])
        print(Payment_Mode)
        L1 = ["Trip_ID","Customer_Details","Driver_Name","Driver_Number","Payment_Mode"]
        L2 = [Trip_ID,Customer_Details,Driver_Name,Driver_Number,Payment_Mode]
        dictionary = {L1 : L2 for L1,L2 in zip(L1,L2)}
        return render_template("Micro_Button.html", dictionary = dictionary,microdict = microdict)


@app.route("/Start_Trip_Micro",methods = ["POST"])
def Start_Trip_Micro():
    if request.method == "POST":
        return render_template("Start_Trip_Micro.html", dictionary = dictionary,Input_Data = Input_Data, microdict = microdict)



@app.route("/Ongoing_Trip_Micro",methods = ["POST"])
def Ongoing_Trip_Micro():
    if request.method == "POST":
        return render_template("Ongoing_Trip_Micro.html",dictionary = dictionary, Input_Data = Input_Data, microdict = microdict)


@app.route("/Trip_Completed_Micro",methods = ["POST"])
def Trip_Completed_Micro():
    if request.method == "POST":
        return render_template("Trip Completed_Micro.html",microdict = microdict, Input_Data = Input_Data, dictionary = dictionary)

@app.route("/Payment_Received_Micro",methods = ["POST"])
def Payment_Received_Micro():
    if request.method == "POST":
        return render_template("Payment_Received_Micro.html",dictionary = dictionary, microdict = microdict, Input_Data = Input_Data)



@app.route("/Additional_Data_Mini",methods = ["POST"])
def Additional_Data_Mini():
    if request.method == "POST":
        global dictionary_mini
        dictionary_mini = dict()
        print("Bony")
        Trip_ID = str(request.form["Trip_ID"])
        print(Trip_ID)
        print("8532")
        Customer_Details = str(request.form["C_Details"])
        print(Customer_Details)
        Driver_Name = str(request.form["D_Name"])
        print(Driver_Name)
        Driver_Number = request.form["D_Number"]
        print(Driver_Number)
        Payment_Mode = str(request.form["Payment_Mode"])
        print(Payment_Mode)
        L1 = ["Trip_ID","Customer_Details","Driver_Name","Driver_Number","Payment_Mode"]
        L2 = [Trip_ID,Customer_Details,Driver_Name,Driver_Number,Payment_Mode]
        dictionary_mini = {L1 : L2 for L1,L2 in zip(L1,L2)}
        print("85321")
        return render_template("Mini_Button.html", dictionary_mini = dictionary_mini,Input_Data = Input_Data, minidict = minidict )


@app.route("/Start_Trip_Mini",methods = ["POST"])
def Start_Trip_Mini():
    if request.method == "POST":
        return render_template("Start_Trip_Mini.html", dictionary_mini = dictionary_mini,Input_Data = Input_Data, minidict = minidict)


@app.route("/Ongoing_Trip_Mini", methods=["POST"])
def Ongoing_Trip_Mini():
    if request.method == "POST":
        return render_template("Ongoing_Trip_Mini.html", dictionary_mini=dictionary_mini, Input_Data=Input_Data,
                               minidict=minidict)


@app.route("/Trip_Completed_Mini", methods=["POST"])
def Trip_Completed_Mini():
    if request.method == "POST":
        return render_template("Trip_Completed_Mini.html", minidict=minidict, Input_Data=Input_Data,
                               dictionary_mini=dictionary_mini)


@app.route("/Payment_Received_Mini", methods=["POST"])
def Payment_Received_Mini():
    if request.method == "POST":
        return render_template("Payment_Received_Mini.html", dictionary_mini=dictionary_mini, minidict=minidict,
                               Input_Data=Input_Data)

@app.route("/Additional_Data_Jumbo",methods = ["POST"])
def Additional_Data_Jumbo():
    if request.method == "POST":
        global dictionary_jumbo
        dictionary_jumbo = dict()
        Trip_ID = str(request.form["Trip_ID"])
        print(Trip_ID)
        Customer_Details = str(request.form["C_Details"])
        print(Customer_Details)
        Driver_Name = str(request.form["D_Name"])
        print(Driver_Name)
        Driver_Number = request.form["D_Number"]
        print(Driver_Number)
        Payment_Mode = str(request.form["Payment_Mode"])
        print(Payment_Mode)
        L1 = ["Trip_ID","Customer_Details","Driver_Name","Driver_Number","Payment_Mode"]
        L2 = [Trip_ID,Customer_Details,Driver_Name,Driver_Number,Payment_Mode]
        dictionary_jumbo = {L1 : L2 for L1,L2 in zip(L1,L2)}
        return render_template("Jumbo_Button.html", dictionary_jumbo = dictionary_jumbo, Input_Data = Input_Data, jumbodict = jumbodict )


@app.route("/Start_Trip_Jumbo",methods = ["POST"])
def Start_Trip_Jumbo():
    if request.method == "POST":
        return render_template("Start_Trip_Jumbo.html", dictionary_jumbo = dictionary_jumbo,Input_Data = Input_Data, jumbodict = jumbodict)


@app.route("/Ongoing_Trip_Jumbo", methods=["POST"])
def Ongoing_Trip_Jumbo():
    if request.method == "POST":
        return render_template("Ongoing_Trip_Jumbo.html", dictionary_jumbo=dictionary_jumbo, Input_Data=Input_Data,
                               jumbodict=jumbodict)


@app.route("/Trip_Completed_Jumbo", methods=["POST"])
def Trip_Completed_Jumbo():
    if request.method == "POST":
        return render_template("Trip_Completed_Jumbo.html", jumbodict=jumbodict, Input_Data=Input_Data,
                               dictionary_jumbo=dictionary_jumbo)


@app.route("/Payment_Received_Jumbo", methods=["POST"])
def Payment_Received_Jumbo():
    if request.method == "POST":
        return render_template("Payment_Received_Jumbo.html", dictionary_jumbo=dictionary_jumbo, jumbodict=jumbodict,
                               Input_Data=Input_Data)


if __name__ == "__main__":
    app.run(debug= False)