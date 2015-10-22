# Mortgage amortization
"""
    mortgage.amortization_table(66000,3,180,61,450)

    $66K principle, 3% APR, 15 year term, additional principal each month of $450 starting in year 6
"""
from decimal import *


def amortization_table(principal, rate, term, additional_month=0, addiitonal_principal=0):
    ''' Prints the amortization table for a loan.

    Prints the amortization table for a loan given
    the principal, the interest rate (as an APR), and
    the term (in months).'''

    payment = pmt(principal, rate, term)
    begBal = principal

    # Print headers
    print 'Pmt no'.rjust(6), ' ', 'Beg. bal.'.ljust(13), ' ',
    print 'Payment'.ljust(9), ' ', 'Principal'.ljust(9), ' ',
    print 'Interest'.ljust(9), ' ', 'End. bal.'.ljust(13)
    print ''.rjust(6, '-'), ' ', ''.ljust(13, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(9, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(13, '-'), ' '
    # Print data
    for num in range(1, term + 1):

        interest = round(begBal * (rate / (12 * 100.0)), 2)
        if num >= additional_month:
            applied = round(payment + addiitonal_principal - interest, 2)
        else:
            applied = round(payment - interest, 2)
        endBal = round(begBal - applied, 2)

        print str(num).center(6), ' ',
        print '{0:,.2f}'.format(begBal).rjust(13), ' ',
        print '{0:,.2f}'.format(payment).rjust(9), ' ',
        print '{0:,.2f}'.format(applied).rjust(9), ' ',
        print '{0:,.2f}'.format(interest).rjust(9), ' ',
        print '{0:,.2f}'.format(endBal).rjust(13)

        begBal = endBal
        if begBal < 0:
            break


def pmt(principal, rate, term):
    '''Calculates the payment on a loan.

    Returns the payment amount on a loan given
    the principal, the interest rate (as an APR),
    and the term (in months).'''

    ratePerTwelve = rate / (12 * 100.0)

    result = principal * (ratePerTwelve / (1 - (1 + ratePerTwelve) ** (-term)))

    # Convert to decimal and round off to two decimal
    # places.
    result = Decimal(result)
    result = round(result, 2)
    return result
