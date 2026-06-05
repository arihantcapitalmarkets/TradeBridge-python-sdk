from swagger_client.models import TaxPnlEquityRequest, TaxPnlEquityFilter, TaxPnlFoRequest, TaxPnlFoFilter, DpHoldingsRequest, TradeHistoryRequest, MultiFilter
from swagger_client.models.ledger_report_request import LedgerRequest, LedgerFilter
from swagger_client.models.margin_calculator_request import MarginCalculatorRequest
from swagger_client.models.check_margin_request import CheckMarginRequest
from swagger_client.models.margin_calculator_request import Symbol
from swagger_client.models.verify_otp_request import VerifyOtpRequest
from swagger_client.models.resend_otp_request import ResendOtpRequest
from swagger_client.models.refresh_token_request import RefreshTokenRequest
from swagger_client.models.intraday_candle_data_request import IntradayCandleDataRequest
from swagger_client.models.profit_loss_fo_report_request import ProfitLossFoReportRequest
from swagger_client.models.profit_loss_cash_report_request import ProfitLossCashReportRequest, ReportFilters
from swagger_client.models.position_conversion_request import PositionConversionRequest
from swagger_client.models.brokerage_charges_request import BrokerageChargeRequest
from swagger_client.models.exit_order_request import ExitOrderRequest
from swagger_client.models.cancel_order_request import CancelOrderRequest
from swagger_client.models.modify_order_request import ModifyOrderRequest
from swagger_client.models.order_trail_request import OrderTrailRequest
from swagger_client.models.place_order_request import PlaceOrderRequest
from swagger_client.api import LoginApi
from swagger_client.api import ContractMasterApi
from swagger_client.api import ChartApi
from swagger_client.api import FundsApi
from swagger_client.api import LoginProfileApi
from swagger_client.models.login_request import LoginRequest
from swagger_client.api import OrderControllerApi
from swagger_client.api import PositionControllerApi
from swagger_client.api import ProfitLossReportApi
from swagger_client.api import PortfolioApi
from swagger_client.api import MarginCalculatorApi
from swagger_client.enums.exc_enum import ExcEnum
from swagger_client.enums.instrument_enum import InstrumentEnum
from swagger_client.enums.ord_action_enum import OrdActionEnum
from swagger_client.enums.ord_type_enum import OrdTypeEnum
from swagger_client.enums.ord_validity_enum import OrdValidityEnum
from swagger_client.enums.prd_type_enum import PrdTypeEnum
import attrs

api_key = "1QSa*******z8JbOe"
source = "SDK"
accessToken = "eyJhbGciOiJIUzUxMiJ9**************oyVInpmMk3psEmhP1xRRH6k-oPJg2Bw"


# Login
loginAPI = LoginApi()
login_body = LoginRequest(userId="nest**3",
                          password="aa***11")
login_response_body = loginAPI.login_normal_login_post(login_body, api_key, source)[0]
#
# # Verify-Otp
# verifyOtpAPI = LoginApi()
# verify_otp_body = VerifyOtpRequest(userId="nest**3",
#                                    txnId="587c4fcd-6d27-480d-9578-020428d712f9",
#                                    otp="795538")
# verify_otp_response_body = verifyOtpAPI.verify_otp(verify_otp_body, api_key, source)[0]
#
# # Access the accessToken and refreshToken
# accessToken = attrs.asdict(verify_otp_response_body)["data"]["accessToken"]
# refreshToken = attrs.asdict(verify_otp_response_body)["data"]["refreshToken"]
#
# # Resend-Otp
# resendOtpAPI = LoginApi()
# resend_otp_body = ResendOtpRequest(userId="nest**3",
#                                    txnId="e9ebb6e6-ca1b-472f-9430-6afafc5e0d5d")
# resend_otp_response_body = resendOtpAPI.resend_otp(resend_otp_body, api_key, source)[0]
#
# # Refresh Token
# refreshTokenAPI = LoginApi()
# refresh_token_body = RefreshTokenRequest(userId="nest**3",
#                                          refreshToken="75dbfd0338ec49108e9ddfbd89775e03881615a175fa4289ac1636bf1db1a509")
# refresh_token_response_body = refreshTokenAPI.refresh_token(refresh_token_body, api_key, source)[0]
#
# # Logout
# logoutAPI = LoginApi()
# Logout_response_body = logoutAPI.logout(accessToken, api_key, source)[0]
#
# # Contract Master
# contractMasterAPI = ContractMasterApi()
# exch = 'NSE'
# contract_master_response_body = contractMasterAPI.contract_master(api_key, source, exch)[0]
#
# # Surveillance Symbols Api
# contractMasterAPI = ContractMasterApi()
# surv_symbol_response_body = contractMasterAPI.surv_symbol(api_key, source)[0]
#
# # Get profile
# profileAPI = LoginProfileApi()
# profile_response_body = profileAPI.get_profile(accessToken, api_key, source)[0]
#
# # Get Funds
# fundsAPI = FundsApi()
# funds_response_body = fundsAPI.fund_view(accessToken, api_key, source)[0]
#
# # Check Margin
# fundsAPI = FundsApi()
# check_margin_body = CheckMarginRequest(
#     symbol="TCS-EQ",
#     excToken="11536",
#     ordAction=OrdActionEnum.BUY,
#     ordValidity=OrdValidityEnum.DAY,
#     ordType=OrdTypeEnum.LIMIT,
#     prdType=PrdTypeEnum.DELIVERY,
#     qty=5,
#     triggerPrice=0.0,
#     limitPrice=3200,
#     instrument=InstrumentEnum.STK,
#     exc=ExcEnum.NSE,
#     lotSize=1,
#     amo=False,
#     boStpLoss=0.0,
#     boTgtPrice=0.0
# )
# check_margin_response = fundsAPI.check_margin(check_margin_body, accessToken, api_key, source)[0]
#
# # Place Order
# orderControllerAPI = OrderControllerApi()
# place_order_body = PlaceOrderRequest(
#     symbol="TCS-EQ",
#     excToken="11536",
#     ordAction=OrdActionEnum.BUY,
#     ordValidity=OrdValidityEnum.DAY,
#     ordType=OrdTypeEnum.MARKET,
#     prdType=PrdTypeEnum.DELIVERY,
#     qty=1,
#     triggerPrice=0.0,
#     limitPrice=0.0,
#     disQty=0,
#     instrument=InstrumentEnum.STK,
#     exc=ExcEnum.NSE,
#     lotSize=1,
#     amo=False,
#     build="MOB",
#     boStpLoss=0.0,
#     boTgtPrice=0.0,
#     trailingSL=0.0,
#     remarks="place-order",
#     excAlgoId=""
# )
#
# latitude = "5.66"
# longitude = ""
# place_order_response = orderControllerAPI.place_order(place_order_body, accessToken, api_key, latitude, longitude, source)[0]
# orderId = attrs.asdict(place_order_response)['data']['ordId']
#
# # Modify Order
# orderControllerAPI = OrderControllerApi()
# modify_order_body = ModifyOrderRequest(
#     triggerPrice=0.0,
#     ordType=OrdTypeEnum.MARKET,
#     prdType=PrdTypeEnum.CASH,
#     instrument=InstrumentEnum.STK,
#     exc=ExcEnum.NSE,
#     qty=5,
#     lotSize=0,
#     symbol="TCS-EQ",
#     ordId="260514000000154",
#     ordAction=OrdActionEnum.BUY,
#     limitPrice=192.55,
#     disQty=0,
#     ordValidity=OrdValidityEnum.DAY,
#     tradedQty=0,
#     ordValidityDays=0,
#     exchangeToken="11536",
#     amo=False
# )
# latitude = "4"
# longitude = "9.888"
# modify_order_response = orderControllerAPI.modify_order(modify_order_body, accessToken, api_key, latitude, longitude, source)[0]
#
# # Cancel Order
# orderControllerAPI = OrderControllerApi()
# cancel_order_body = CancelOrderRequest(
#     symbol="TCS-EQ",
#     ordId="260514000000154",
#     exc=ExcEnum.NSE
# )
# latitude = ""
# longitude = "0.77"
# cancel_order_response = orderControllerAPI.cancel_order(cancel_order_body, accessToken, api_key, latitude, longitude, source)[0]
#
# # Exit Order
# orderControllerAPI = OrderControllerApi()
# exit_order_body = ExitOrderRequest(symbol="TCS-EQ",
#                                    boOrdStatus="complete",
#                                    ordId="260514000000154",
#                                    parOrdId="260514000000154",
#                                    exc=ExcEnum.NSE,
#                                    prdType=PrdTypeEnum.COVER_ORDER
#                                    )
# latitude = "3.22"
# longitude = "1.6666"
# exit_order_response = orderControllerAPI.exit_order(exit_order_body, accessToken, api_key, latitude, longitude, source)[0]
#
# # BrokerageCharges
# orderControllerAPI = OrderControllerApi()
# brokerage_body = BrokerageChargeRequest(
#     symbol="TCS-EQ",
#     exc=ExcEnum.NSE,
#     prdType=PrdTypeEnum.INTRADAY,
#     triggerPrice="",
#     price="3489.80",
#     qty="10",
#     instrument=InstrumentEnum.STK,
#     ordAction=OrdActionEnum.SELL,
#     excToken="11536",
#     ordType=OrdTypeEnum.MARKET
# )
# brokerage_response_body = orderControllerAPI.brokerage_charges(brokerage_body, accessToken, api_key, source)[0]
#
# # MarginCalculator
# marginCalculatorAPI = MarginCalculatorApi()
# margin_calculator_body = MarginCalculatorRequest(symbols=[
#     Symbol(
#         symbol="BANKNIFTY26JUL70100CE",
#         netQty=1,
#         lotSize=1,
#         instrument=InstrumentEnum.OPTIDX,
#         streamSym="62278_NFO",
#         excToken="62278",
#         exc=ExcEnum.NFO,
#         prdType=PrdTypeEnum.DELIVERY,
#         brand=[]
#     )
# ])
# margin_calculator_response = marginCalculatorAPI.margin_calculator(margin_calculator_body, accessToken, api_key, source)[0]
#
# # OrderBook
# portfolioApi = PortfolioApi()
# order_book_response = portfolioApi.get_order_book(accessToken, api_key, source)[0]
#
# # Order Trail
# portfolioApi = PortfolioApi()
# order_trail_body = OrderTrailRequest(
#     instrument=InstrumentEnum.STK,
#     ordId='260515000000004'
# )
# order_trail_response = portfolioApi.order_trail(order_trail_body, accessToken, api_key, source)[0]
#
# # Order Status
# portfolioApi = PortfolioApi()
# order_status_body = OrderTrailRequest(
#     instrument=InstrumentEnum.STK,
#     ordId='260515000000004'
# )
# order_status_response = portfolioApi.order_status(order_status_body, accessToken, api_key, source)[0]
#
# # Position Book
# positionControllerAPI = PositionControllerApi()
# position_book_response = positionControllerAPI.get_position_book("net", accessToken, api_key, source)[0]
#
# # Holdings
# positionControllerAPI = PositionControllerApi()
# holdings_response = positionControllerAPI.do_holdings(accessToken, api_key, source)[0]
#
# # ConvertPosition
# positionControllerAPI = PositionControllerApi()
# convert_position_body = PositionConversionRequest(
#     exc=ExcEnum.NSE,
#     excToken="11536",
#     instrument=InstrumentEnum.STK,
#     qty=1,
#     symbol="TCS-EQ",
#     lotSize=1,
#     ordAction=OrdActionEnum.BUY,
#     prdType=PrdTypeEnum.INTRADAY,
#     toPrdType=PrdTypeEnum.DELIVERY,
#     type="DAY1"
# )
# convert_position_response = positionControllerAPI.convert_position(convert_position_body, accessToken, api_key, source)[0]
#
# # Profit Loss Cash Report
# profitLossReport = ProfitLossReportApi()
# profit_loss_cash_report_body = ProfitLossCashReportRequest(filters=[
#     ReportFilters(key="date", value="13/04/2026-15/04/2026"),
#     ReportFilters(key="charges", value="incCharges"),
#     ReportFilters(key="finYear", value="2025-2026")])
# profit_loss_cash_report_response = profitLossReport.profit_loss_cash_report(profit_loss_cash_report_body, accessToken, api_key, source)[0]
#
# # Profit Loss Fo report
# profitLossReport = ProfitLossReportApi()
# profit_loss_fo_report_body = ProfitLossFoReportRequest(filters=[
#     ReportFilters(key="date", value="01/01/2026-15/04/2026"),
#     ReportFilters(key="charges", value="incCharges"),
#     ReportFilters(key="exc", value="ALL"),
#     ReportFilters(key="finYear", value="2025-2026")
# ])
# profit_loss_fo_report_response = profitLossReport.profit_loss_fo_report(profit_loss_fo_report_body, accessToken, api_key, source)[0]
#
# # Ledger Report
# profitLossReport = ProfitLossReportApi()
# ledger_report_body = LedgerRequest(filters=[
#     LedgerFilter(key="date", value="01/04/2026-31/03/2027"),
#     LedgerFilter(key="prdtCd", value="10"),
#     LedgerFilter(key="finYear", value="2026-2027")])
# ledger_report_response = profitLossReport.ledger_report(ledger_report_body, accessToken, api_key, source)[0]
#
# # Tax PnL Equity Report
# profitLossReport = ProfitLossReportApi()
# tax_pnl_equity_report_body = TaxPnlEquityRequest(filters=[
#     TaxPnlEquityFilter(key="date", value="01/04/2025-31/03/2026"),
#     TaxPnlEquityFilter(key="charges", value="incCharges"),
#     TaxPnlEquityFilter(key="finYear", value="2026-2027")])
# tax_pnl_equity_report_response = profitLossReport.tax_pnl_equity_report(tax_pnl_equity_report_body, accessToken, api_key, source)[0]
#
# # Tax PnL Fo Report
# profitLossReport = ProfitLossReportApi()
# tax_pnl_fo_report_body = TaxPnlFoRequest(filters=[
#     TaxPnlFoFilter(key="date", value="01/04/2025-31/03/2026"),
#     TaxPnlFoFilter(key="charges", value="incCharges"),
#     TaxPnlFoFilter(key="finYear", value="2026-2027"),
#     TaxPnlFoFilter(key="exc", value="ALL")])
# tax_pnl_fo_report_response = profitLossReport.tax_pnl_fo_report(tax_pnl_fo_report_body, accessToken, api_key, source)[0]
#
# # DP Holdings
# profitLossReport = ProfitLossReportApi()
# dp_holdings_body = DpHoldingsRequest(date="22/04/2026",
#                                      dpName="NSDL")
# dp_holdings_response = profitLossReport.dp_holdings(dp_holdings_body, accessToken, api_key, source)[0]
#
# # Trade History
# profitLossReport = ProfitLossReportApi()
# trade_history_body = TradeHistoryRequest(frmDte="01/01/2026",
#                                          toDte="22/04/2026",
#                                          multiFilters=[
#                                              MultiFilter(
#                                                  key="actualExc",
#                                                  value=["NSE", "CDS", "BFO"]
#                                              ),
#                                              MultiFilter(
#                                                  key= "ordAction",
#                                                  value= ["BUY", "SELL"]
#                                              )
#                                          ])
# trade_history_response = profitLossReport.trade_history(trade_history_body, accessToken, api_key, source)[0]
#
# # Historical Data
# chartAPI = ChartApi()
# api_key = "EkX*******yUKfCC"
# historical_data_response = chartAPI.historical_data(accessToken, api_key, source,
#                                                     'TCS-EQ',
#                                                     '1day',
#                                                     '2025-04-04T17:55:00.000',
#                                                     '2025-04-04T17:55:00.000',
#                                                     'STK',
#                                                     'NSE',
#                                                     '12193_NSE')[0]
#
# # Intraday Candle Data
# chartAPI = ChartApi()
# api_key = "EkX********yUKfCC"
# intraday_body = IntradayCandleDataRequest(
#     symbol="JIOFIN-EQ",
#     resolution="1day",
#     exc=ExcEnum.NSE,
#     instrument=InstrumentEnum.STK,
#     startTime="2025-04-04T00:00:00.000",
#     endTime="2025-04-04T15:00:00.000"
# )
# intraday_response = chartAPI.intraday(intraday_body, accessToken, api_key, source)[0]


if __name__ == "__main__":
    print("\nLOGIN_RESPONSE: \n", login_response_body, "\n\n")
    # print("VERIFY_OTP_RESPONSE: \n", verify_otp_response_body, "\n\n")
    # print("RESEND_OTP_RESPONSE: \n", resend_otp_response_body, "\n\n")
    # print("REFRESH_TOKEN_RESPONSE: \n", refresh_token_response_body, "\n\n")
    # print("LOGOUT_RESPONSE: \n", Logout_response_body, "\n\n")
    # print("CONTRACT_MASTER_RESPONSE: \n", contract_master_response_body, "\n\n")
    # print("SURVEILLANCE_SYMBOLS_RESPONSE: \n", surv_symbol_response_body, "\n\n")
    # print("PROFILE_RESPONSE: \n", profile_response_body, "\n\n")
    # print("FUNDS_RESPONSE: \n", funds_response_body, "\n\n")
    # print("CHECK_MARGIN_RESPONSE: \n", check_margin_response, "\n\n")
    # print("PLACE_ORDER_RESPONSE: \n", place_order_response, "\n\n")
    # print("MODIFY_ORDER_RESPONSE: \n", modify_order_response, "\n\n")
    # print("CANCEL_ORDER_RESPONSE: \n", cancel_order_response, "\n\n")
    # print("EXIT_ORDER_RESPONSE: \n", exit_order_response, "\n\n")
    # print("BROKERAGE_RESPONSE: \n", brokerage_response_body, "\n\n")
    # print("MARGIN_CACULATOR_RESPONSE: \n", margin_calculator_response, "\n\n")
    # print("ORDER_BOOK_RESPONSE: \n", order_book_response, "\n\n")
    # print("ORDER_TRAIL_RESPONSE: \n", order_trail_response, "\n\n")
    # print("ORDER_STATUS_RESPONSE: \n", order_status_response, "\n\n")
    # print("POSITION_BOOK_RESPONSE: \n", position_book_response, "\n\n")
    # print("HOLDINGS_RESPONSE: \n", holdings_response, "\n\n")
    # print("CONVERT_POSITION_RESPONSE: \n", convert_position_response, "\n\n")
    # print("PROFIT_LOSS_CASH_REPORT_RESPONSE: \n", profit_loss_cash_report_response, "\n\n")
    # print("PROFIT_LOSS_FO_REPORT_RESPONSE: \n", profit_loss_fo_report_response, "\n\n")
    # print("LEDGER_REPORT_RESPONSE: \n", ledger_report_response, "\n\n")
    # print("TAX_PNL_EQUITY_REPORT_RESPONSE: \n", tax_pnl_equity_report_response, "\n\n")
    # print("TAX_PNL_FO_REPORT_RESPONSE: \n", tax_pnl_fo_report_response, "\n\n")
    # print("DP_HOLDINGS_RESPONSE: \n", dp_holdings_response, "\n\n")
    # print("TRADE_HISTORY_RESPONSE: \n", trade_history_response, "\n\n")
    # print("HISTORICAL_DATA_RESPONSE: \n", historical_data_response, "\n\n")
    # print("INTRADAY_DATA_RESPONSE: \n", intraday_response, "\n\n")
