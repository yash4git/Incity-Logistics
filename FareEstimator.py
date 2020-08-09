class Fare_Details(object):
    Input_Details = dict()

    def __init__(self, Input_Details):
        self.Input_Details = Input_Details




    def Fare_Details_Micro(self):
        Base_Fare = 250
        Cost_Per_Km = 26
        Cost_Per_Min = 0
        Platform_Charge = 0
        Surcharge = 0
        Night_Charge = 0
        Tax_Factor = 0.05
        Commission_Factor = 0.85
        Actual_Km_Charges = 0
        Actual_Min_Charges = 0
        Actual_Min_Charges = Cost_Per_Min * self.Input_Details["Time"]
        Multiplier = 0
        Actual_Trip_Fare = 0
        Taxable_Amount = 0
        Tax = 0
        Payable_Fare = 0
        Partner_Share = 0

        if self.Input_Details["Distance"] <=3:
            Actual_Km_Charges = 0
        else:
            Actual_Km_Charges = (self.Input_Details["Distance"] - 3) *  Cost_Per_Km

        if self.Input_Details["Distance"] < 10:
            Multiplier = Actual_Km_Charges+ Actual_Min_Charges
        elif self.Input_Details["Distance"] >=10:
            Multiplier = (Actual_Km_Charges+ Actual_Min_Charges)*1.5

        Actual_Trip_Fare = Base_Fare + Platform_Charge + Surcharge + Night_Charge + Multiplier + self.Input_Details["Helper_Amount"]
        Total_Trip_Fare = Actual_Trip_Fare + self.Input_Details["Insurance_Amount"]
        Taxable_Amount = Total_Trip_Fare - self.Input_Details["Discount"]
        Tax = (Taxable_Amount * Tax_Factor)
        Tax = round(Tax,2)
        Payable_Fare = Taxable_Amount+Tax
        Partner_Share = round(Actual_Trip_Fare * Commission_Factor,2)

        Micro_Output = dict()
        Micro_Output["Vehicle Type"] = "Micro"
        Micro_Output["Source"] = self.Input_Details["Source"]
        Micro_Output["Destinetion"] = self.Input_Details["Destinetion"]
        Micro_Output["Distance"] = self.Input_Details["Distance"]
        Micro_Output["Actual Trip Fare"] = Actual_Trip_Fare
        Micro_Output["Total Trip Fare"] = Total_Trip_Fare
        Micro_Output["Discount"] = self.Input_Details["Discount"]
        Micro_Output["Taxable Amount"] = Taxable_Amount
        Micro_Output["Tax"] = Tax
        Micro_Output["Payable Fare"] = Payable_Fare
        Micro_Output["Partner Share"] = Partner_Share
        return Micro_Output



    def Fare_Details_Mini(self):
        Base_Fare = 300
        Cost_Per_Km = 28
        Cost_Per_Min = 0
        Platform_Charge = 0
        Surcharge = 0
        Night_Charge = 0
        Tax_Factor = 0.05
        Commission_Factor = 0.85
        Actual_Km_Charges = 0
        Actual_Min_Charges = 0
        Actual_Min_Charges = Cost_Per_Min * self.Input_Details["Time"]
        Multiplier = 0
        Actual_Trip_Fare = 0
        Taxable_Amount = 0
        Tax = 0
        Payable_Fare = 0
        Partner_Share = 0

        if self.Input_Details["Distance"] <=3:
            Actual_Km_Charges = 0
        else:
            Actual_Km_Charges = (self.Input_Details["Distance"] - 3) *  Cost_Per_Km

        if self.Input_Details["Distance"] < 10:
            Multiplier = Actual_Km_Charges+ Actual_Min_Charges
        elif self.Input_Details["Distance"] >=10:
            Multiplier = (Actual_Km_Charges+ Actual_Min_Charges)*1.5

        Actual_Trip_Fare = Base_Fare + Platform_Charge + Surcharge + Night_Charge + Multiplier + self.Input_Details["Helper_Amount"]
        Total_Trip_Fare = Actual_Trip_Fare + self.Input_Details["Insurance_Amount"]
        Taxable_Amount = Total_Trip_Fare - self.Input_Details["Discount"]
        Tax = (Taxable_Amount * Tax_Factor)
        Tax = round(Tax,2)
        Payable_Fare = Taxable_Amount+Tax
        Partner_Share = round(Actual_Trip_Fare * Commission_Factor,2)

        Mini_Output = dict()
        Mini_Output["Vehicle Type"] = "Mini"
        Mini_Output["Distance"] = self.Input_Details["Distance"]
        Mini_Output["Source"] = self.Input_Details["Source"]
        Mini_Output["Destinetion"] = self.Input_Details["Destinetion"]
        Mini_Output["Actual Trip Fare"] = Actual_Trip_Fare
        Mini_Output["Total Trip Fare"] = Total_Trip_Fare
        Mini_Output["Discount"] = self.Input_Details["Discount"]
        Mini_Output["Taxable Amount"] = Taxable_Amount
        Mini_Output["Tax"] = Tax
        Mini_Output["Payable Fare"] = Payable_Fare
        Mini_Output["Partner Share"] = Partner_Share
        return Mini_Output




    def Fare_Details_Jumbo(self):
        Base_Fare = 400
        Cost_Per_Km = 30
        Cost_Per_Min = 0
        Platform_Charge = 0
        Surcharge = 0
        Night_Charge = 0
        Tax_Factor = 0.05
        Commission_Factor = 0.85
        Actual_Km_Charges = 0
        Actual_Min_Charges = 0
        Actual_Min_Charges = Cost_Per_Min * self.Input_Details["Time"]
        Multiplier = 0
        Actual_Trip_Fare = 0
        Taxable_Amount = 0
        Tax = 0
        Payable_Fare = 0
        Partner_Share = 0

        if self.Input_Details["Distance"] <=3:
            Actual_Km_Charges = 0
        else:
            Actual_Km_Charges = (self.Input_Details["Distance"] - 3) *  Cost_Per_Km

        if self.Input_Details["Distance"] < 10:
            Multiplier = Actual_Km_Charges+ Actual_Min_Charges
        elif self.Input_Details["Distance"] >=10:
            Multiplier = (Actual_Km_Charges+ Actual_Min_Charges)*1.5

        Actual_Trip_Fare = Base_Fare + Platform_Charge + Surcharge + Night_Charge + Multiplier + self.Input_Details["Helper_Amount"]
        Total_Trip_Fare = Actual_Trip_Fare + self.Input_Details["Insurance_Amount"]
        Taxable_Amount = Total_Trip_Fare - self.Input_Details["Discount"]
        Tax = (Taxable_Amount * Tax_Factor)
        Tax = round(Tax,2)
        Payable_Fare = Taxable_Amount+Tax
        Partner_Share = round(Actual_Trip_Fare * Commission_Factor,2)

        Jumbo_Output = dict()
        Jumbo_Output["Vehicle Type"] = "Jumbo"
        Jumbo_Output["Source"] = self.Input_Details["Source"]
        Jumbo_Output["Distance"] = self.Input_Details["Distance"]
        Jumbo_Output["Destinetion"] = self.Input_Details["Destinetion"]
        Jumbo_Output["Actual Trip Fare"] = Actual_Trip_Fare
        Jumbo_Output["Total Trip Fare"] = Total_Trip_Fare
        Jumbo_Output["Discount"] = self.Input_Details["Discount"]
        Jumbo_Output["Taxable Amount"] = Taxable_Amount
        Jumbo_Output["Tax"] = Tax
        Jumbo_Output["Payable Fare"] = Payable_Fare
        Jumbo_Output["Partner Share"] = Partner_Share
        return Jumbo_Output









