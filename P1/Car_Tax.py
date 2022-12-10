Central_tax= 20/100
def thar_jeep():
    UT=18/100
    thar_price=1800000
    Total_tax_chd=(Central_tax+UT) * thar_price
    print (f"Tax on Thar in Chandigarh =" ,{Total_tax_chd})
    total_tax_haryana=Central_tax*thar_price
    print(f"Tax on Thar in Haryana =", {total_tax_haryana} )
    jeep_price=2400000
    tax_jeep_chd=(Central_tax+UT) * jeep_price
    print(f"Tax on Jeep in Chandigarh =",{tax_jeep_chd})
    tax_jeep_haryana= jeep_price*Central_tax
    print(f"Tax on Jeep in Haryana =",{tax_jeep_haryana})

thar_jeep()