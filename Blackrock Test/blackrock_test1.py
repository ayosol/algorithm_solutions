from datetime import *

def get_portfolios_with_open_positions(date_str: str, portfolio_strings: list[str]) -> list[str]:
    # Access your code here. Feel free to create other methods as required
    pwithp = []
        for i in portfolio_strings:
            portfolio = i.split('|')
            #print(portfolio[0])
            portfolio_name = portfolio[0]
            positions = portfolio[1].split(',')
            #print("positions", positions)
            for j in positions:
                name = j.split(':')[0]
                start_date = j.split(':')[1]
                end_date = j.split(':')[2]
                #print("name", name, "start", start_date, "end", end_date)
                if start_date <= date_str and (end_date > date_str or end_date == '' or date_str == None):
                    if portfolio_name not in pwithp:
                        pwithp.append(portfolio_name)


        return pwithp if len(pwithp) != 0 else None


        if (datetime.datetime.strptime(start_date, DATE_FORMAT) <= datetime.datetime.strptime(date_str, DATE_FORMAT) and (datetime.datetime.strptime(end_date, DATE_FORMAT) > datetime.datetime.strptime(date_str, DATE_FORMAT) or end_date == "" or end_date is None)):




# date_str = '2020-01-01'
# portfolios = ['Portfolio1|CUSIP1:2019-01-01:2022-02-01','Portfolio2|CUSIP2:2019-01-01:2022-02-01']
# ans = get_portfolios_with_open_positions(date_str, portfolios)
# print("ans->", ans)
# # Portfolio1
# # Portfolio2


# date_str = '2020-01-01'
# portfolios = ['Portfolio1|CUSIP1:2019-01-01:2022-02-01', 'Portfolio2|CUSIP2:2019-01-01:2022-02-01', 'Portfolio3|CUSIP3:2020-01-01:2022-02-01', 'Portfolio4|CUSIP3:2020-01-01:2019-01-01']
# ans = get_portfolios_with_open_positions(date_str, portfolios)
# print("ans->", ans)
# # Portfolio1
# # Portfolio2
# # Portfolio3

date_str = '2020-01-01'
portfolios = ['Portfolio1|CUSIP1:2019-01-01:2020-01-01', 'Portfolio2|CUSIP1:2019-01-01:2021-12-31', 'Portfolio1|CUSIP2:2019-01-01:2021-12-31']
ans = get_portfolios_with_open_positions(date_str, portfolios)
print("ans->", ans)
# Portfolio1
# Portfolio2

# date_str = '2020-01-01'
# portfolios = ['Portfolio1|CUSIP1:2021-01-01:2022-02-01', 'Portfolio2|CUSIP2:2021-01-01:2022-02-01', 'Portfolio3|CUSIP3:2021-01-01:2022-02-01', 'Portfolio4|CUSIP3:2021-01-01:2022-01-01']
# ans = get_portfolios_with_open_positions(date_str, portfolios)
# print("ans->", ans)
# # NONE


# date_str = '2020-01-01'
# portfolios = ['XXKCN|BRTHFKS01:2019-01-04:2019-05-03,CHDKWYNK:2020-01-04:2022-12-24','XXKSN|BRTHFKS04:2019-11-04:,PSNKWYNK:2020-06-01:2022-12-24 ','XXPSN|BRTHFKS02:2023-01-04:2019-05-03,SHDNWYNK:2024-01-01:2022-12-24,SHDNWPSH:2027-01-01:2030-12-24']
# ans = get_portfolios_with_open_positions(date_str, portfolios)
# print("ans->", ans)




# Programming challenge description:
# The goal of this question is to print out which portfolios have open positions.

# A portfolio is represented by a name, and a collection of positions. Each position has a name, a start date, and an end date.

# A position is considered to be open on a given date if its starting date is before or on the given date and its end date is either not specified or on a later date than the given date.

# Input:
# Your program should read lines of text from standard input (this is already part of the initial template). The first line will specify a date (in YYYY-MM-DD format). The rest of the lines will specify portfolios in the following format:

# PortfolioName|PositionName:startDate:endDate,PositionName:startDate:endDate

# If any dates are missing or in the wrong format, they can be considered null.

# For example, this will be a valid input:

# 2020-01-01
# XXKCN|BRTHFKS01:2019-01-04:2019-05-03,CHDKWYNK:2020-01-04:2022-12-24
# XXKSN|BRTHFKS04:2019-11-04:,PSNKWYNK:2020-06-01:2022-12-24 
# XXPSN|BRTHFKS02:2023-01-04:2019-05-03,SHDNWYNK:2024-01-01:2022-12-24,SHDNWPSH:2027-01-01:2030-12-24
# Output:
# If a portfolio contains at least an open position, print the portfolio name on a single line to standard output.

# The portfolio names should be printed on separate lines in the order in which they first appear in the input

# For example, this will be a valid output (there should be no extra new lines or spaces either before or after the portfolio list):

# XXKCE
# XXKSP
# XXKSQ
# If there are no open positions output "NONE", for example

# NONE