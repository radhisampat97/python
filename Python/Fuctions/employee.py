# save this code as employee. py

## to calcultae dearness allowance
def da(basic):
    '''da is 80% of the basic salary'''
    da = basic*(80/100)
    print(__name__)
    return da

# to calculate house rent allowance
def hra(basic):
    '''hra is 15% of basic salary'''
    hra = basic*(15/100)
    return hra

#to calculate provident fund amount
def pf(basic):
    '''pf is 12% of basic salary'''
    pf = basic*(12/100)
    return pf

# to calculate incometax payable by employee
def itax(gross):
    '''tax is calculate at 10% on gross'''
    tax = gross*0.1
    return tax
