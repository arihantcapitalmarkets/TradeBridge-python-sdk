from swagger_client.models.margin_calculator_request import MarginCalculatorRequest
from swagger_client.models.margin_calculator_request import Symbol
from swagger_client.models.verify_otp_request import VerifyOtpRequest
from swagger_client.models.resend_otp_request import ResendOtpRequest
from swagger_client.models.refresh_token_request import RefreshTokenRequest
from swagger_client.models.refresh_token_response import RefreshTokenResponse
from swagger_client.models.success_response import SuccessResponse
from swagger_client.models.refresh_token_request import RefreshTokenRequest
from swagger_client.models.intraday_candle_data_request import IntradayCandleDataRequest
from swagger_client.models.profit_loss_fo_report_request import ProfitLossFoReportRequest
from swagger_client.models.profit_loss_cash_report_request import ProfitLossCashReportRequest, ReportFilters
from swagger_client.models.convert_position_request import ConvertPositionRequest
from swagger_client.models.brokerage_charges_request import BrokerageChargeRequest
from swagger_client.models.exit_order_request import ExitOrderRequest
from swagger_client.models.cancel_order_request import CancelOrderRequest
from swagger_client.models.modify_order_request import ModifyOrderRequest
from swagger_client.models.order_trail_request import OrderTrailRequest
from swagger_client.models.place_order_request import PlaceOrderRequest, OrdActionEnum, OrdValidityEnum, OrdTypeEnum, \
    PrdTypeEnum, InstrumentEnum, ExcEnum
from swagger_client.api import LoginApi
from swagger_client.api import ContractMasterApi
from swagger_client.api import ChartApi
from swagger_client.api import FundsApi
from swagger_client.api import LoginProfileApi
from swagger_client.models.login_request import LoginRequest
from swagger_client.api import OrderControllerApi
from swagger_client.api import PositionControllerApi
from swagger_client.api import ProfitLossReportApi
from swagger_client.api import TradeBookApi
from swagger_client.api import MarginCalculatorApi
import attrs

api_key = "r4AGcBE9by1ZmDGLL4"
source = "SDK"
accessToken = "eyJhbGciOiJIUzUxMiJ9.eyJhcHAtaWQiOiJlOGM1ZDEwYy1mODNmLTRkNjMtYjIxMi0zZGEyMTkxMjM0MjIiLCJsaW1pdCI6IkJBU0lDIiwic3ViIjoiTkVTVDgwMDMiLCJpYXQiOjE3Mzg3Mzk2NTUsImV4cCI6MTczODc2ODQ1NX0.K3NRZjle_QYvvaXi9cpsgS4iontWuvqQOtf7SEFhhBaf5XcxOEMbDkpLJ5z7uJAIyP_TmtO66ILbK6Gvzi9cLA"
#
# Login
loginAPI = LoginApi()
login_body = LoginRequest(userId="NEST8003",
                          password="Abcd@12342")
login_response_body = loginAPI.login_normal_login_post(login_body, api_key, source)[0]
#
# # Verify-Otp
# verifyOtpAPI = LoginApi()
# verify_otp_body = VerifyOtpRequest(userId="nest8003",
#                                    txnId="be5ace22-21b4-4ea7-9d14-ab9e7ec8cfe5",
#                                    otp="0267")
# verify_otp_response_body = verifyOtpAPI.verify_otp(verify_otp_body, api_key, source)[0]
#
# # # Access the accessToken and refreshToken
# # accessToken = attrs.asdict(verify_otp_response_body)["data"]["accessToken"]
# refreshToken = attrs.asdict(verify_otp_response_body)["data"]["refreshToken"]

# # Resend-Otp
# resendOtpAPI = LoginApi()
# resend_otp_body = ResendOtpRequest(userId="nest8003",
#                                    txnId="be5ace22-21b4-4ea7-9d14-ab9e7ec8cfe5")
# resend_otp_response_body = resendOtpAPI.resend_otp(resend_otp_body, api_key, source)[0]
# #
# # Refresh Token
# refreshTokenAPI = LoginApi()
# refresh_token_body = RefreshTokenRequest(userId="nest8003",
#                                          refreshToken="3cbb8e2008754ac39ff451960af915b9e10754edc50c4e2bb4ea150f70f0646c")
# refresh_token_response_body = refreshTokenAPI.refresh_token(refresh_token_body, api_key, source)[0]
#
# # Contract Master
# contractMasterAPI = ContractMasterApi()
# exch = 'NSE'
# contract_master_response_body = contractMasterAPI.contract_master(accessToken, api_key, source, exch)[0]
#
# # Logout
# logoutAPI = LoginApi()
# Logout_response_body = logoutAPI.logout(accessToken, api_key, source)[0]

# #
# # Get profile
# profileAPI = LoginProfileApi()
# profile_response_body = profileAPI.get_profile(accessToken, api_key, source)[0]
#
# # Get Funds
# fundsAPI = FundsApi()
# funds_response_body = fundsAPI.fund_view(accessToken, api_key, source)[0]
# #
# # Place Order
# orderControllerAPI = OrderControllerApi()
# place_order_body = body = PlaceOrderRequest(
#     symbol="TCS-EQ",
#     excToken="532540",
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
#     boStpLoss=0,
#     boTgtPrice=0,
#     trailingSL=0.0
# )
#
# latitude = "5.66"
# longitude = ""
# place_order_response = \
#     orderControllerAPI.place_order(place_order_body, accessToken, api_key, latitude, longitude, source)[0]
# orderId = attrs.asdict(place_order_response)['data']['ordId']

# # Modify Order
# orderControllerAPI = OrderControllerApi()
# modify_order_body = ModifyOrderRequest(
#     trigger_price=0.0,
#     ord_type=OrdTypeEnum.MARKET,
#     prd_type=PrdTypeEnum.CASH,
#     instrument=InstrumentEnum.STK,
#     exc=ExcEnum.NSE,
#     qty=5,
#     lot_size=0,
#     symbol="TCS-EQ",
#     ord_id=orderId,
#     ord_action=OrdActionEnum.BUY,
#     limit_price=192.55,
#     dis_qty=0,
#     ord_validity=OrdValidityEnum.DAY,
#     traded_qty=0,
#     ord_validity_days=0,
#     exchange_token="13528",
#     amo=False
# )
# latitude = "4"
# longitude = "9.888"
# modify_order_response = \
#     orderControllerAPI.modify_order(modify_order_body, accessToken, api_key, latitude, longitude, source)[0]
#
# # Cancel Order
# orderControllerAPI = OrderControllerApi()
# cancel_order_body = CancelOrderRequest(
#     symbol="TCS-EQ",
#     ordId=orderId,
#     exc=ExcEnum.NSE
# )
# latitude = ""
# longitude = "0.77"
# cancel_order_response = \
#     orderControllerAPI.cancel_order(cancel_order_body, accessToken, api_key, latitude, longitude, source)[0]

# # Exit Order
# orderControllerAPI = OrderControllerApi()
# exit_order_body = ExitOrderRequest(symbol="TCS-EQ",
#                                    boOrdStatus="complete",
#                                    ordId=orderId,
#                                    parOrdId=orderId,
#                                    exc=ExcEnum.NSE,
#                                    prdType=PrdTypeEnum.COVER_ORDER
#                                    )
# latitude = "3.22"
# longitude = "1.6666"
# exit_order_response = orderControllerAPI.exit_order(exit_order_body, accessToken, api_key, latitude, longitude, source)[
#     0]
# #
# # BrokerageCharges
# orderControllerAPI = OrderControllerApi()
# brokerage_body = BrokerageChargeRequest(
#     symbol="TCS-EQ",
#     exc=ExcEnum.NSE,
#     prdType=PrdTypeEnum.INTRADAY,
#     triggerPrice="",
#     price="3489.80",
#     qty="10000000",
#     instrument=InstrumentEnum.STK,
#     ordAction=OrdActionEnum.SELL,
#     excToken="11536",
#     ordType=OrdTypeEnum.MARKET
# )
# brokerage_response_body = \
#     orderControllerAPI.brokerage_charges(brokerage_body, accessToken, api_key, source)[0]
# #
# # MarginCalculator
# marginCalculatorAPI = MarginCalculatorApi()
# margin_calculator_body = MarginCalculatorRequest(symbols=[
#     Symbol(
#         symbol="BANKNIFTY25MARFUT",
#         netQty="1",
#         lotSize="1",
#         instrument=InstrumentEnum.FUTIDX,
#         streamSym="58958_NFO",
#         excToken="58958",
#         exc=ExcEnum.NFO,
#         prdType=PrdTypeEnum.DELIVERY,
#         brand=[]
#     )
# ])
# margin_calculator_response_body = (
#     marginCalculatorAPI.margin_calculator(margin_calculator_body, accessToken, api_key, source))[0]
#
# # Trade Book
# tradeAPI = TradeBookApi()
# trade_book_response = tradeAPI.trade_book(accessToken, api_key, source)[0]
#
# # OrderBook
# tradeAPI = TradeBookApi()
# order_book_response = tradeAPI.get_order_book(accessToken, api_key, source)[0]
#
# # Order Trail
# tradeAPI = TradeBookApi()
# order_trail_body = OrderTrailRequest(
#     instrument=InstrumentEnum.STK,
#     ordId='250205000000026'
# )
# order_trail_response = tradeAPI.order_trail(order_trail_body, accessToken, api_key, source)[0]
#
# # Order Status
# tradeAPI = TradeBookApi()
# order_status_body = OrderTrailRequest(
#     instrument=InstrumentEnum.STK,
#     ordId="250205000000026"
# )
# order_status_response = tradeAPI.order_status(order_status_body, accessToken, api_key, source)[0]
# #
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
# convert_position_body = ConvertPositionRequest(
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
# # #
# # Profit Loss Cash Report
# profitLossReport = ProfitLossReportApi()
# profit_loss_cash_report_body = ProfitLossCashReportRequest(filters=[
#     ReportFilters(key="date", value="29/01/2025-29/01/2025"),
#     ReportFilters(key="charges", value="incCharges")])
# profit_loss_cash_report_response = (
#     profitLossReport.profit_loss_cash_report(profit_loss_cash_report_body, accessToken, api_key, source))[0]
#
# # Profit Loss Fo report
# profitLossReport = ProfitLossReportApi()
# profit_loss_fo_report_body = ProfitLossFoReportRequest(filters=[
#     ReportFilters(key="date", value="29/01/2025-29/01/2025"),
#     ReportFilters(key="charges", value="incCharges"),
#     ReportFilters(key="exc", value="ALL"),
#     ReportFilters(key="finYear", value="2024-2025")
# ])
# profit_loss_fo_report_response = \
#     profitLossReport.profit_loss_fo_report(profit_loss_fo_report_body, accessToken, api_key, source)[0]
#
# # Historical Data
# chartAPI = ChartApi()
# api_key = "yXAtQFJQSL4tKLdHSo"
# historical_data_response = chartAPI.historical_data(accessToken, api_key, source,
#                                                     'TCS-EQ',
#                                                     '1day',
#                                                     '2023-02-01T17:55:00.000',
#                                                     '2024-02-01T17:55:00.000',
#                                                     'STK',
#                                                     'NSE',
#                                                     '12193_NSE')[0]
#
# # Intraday Candle Data
# chartAPI = ChartApi()
# api_key = "yXAtQFJQSL4tKLdHSo"
# intraday_body = IntradayCandleDataRequest(
#     symbol="JIOFIN-EQ",
#     resolution="1day",
#     exc=ExcEnum.NSE,
#     instrument=InstrumentEnum.STK,
#     startTime="2025-01-30T00:00:00.000",
#     endTime="2025-01-30T15:00:00.000"
# )
# intraday_response = chartAPI.intraday(intraday_body, accessToken, api_key, source)[0]

if __name__ == "__main__":
    print("\nLOGIN_RESPONSE: \n", login_response_body, "\n\n")
    # print("VERIFY_OTP_RESPONSE: \n", verify_otp_response_body, "\n\n")
    # print("RESEND_OTP_RESPONSE: \n", resend_otp_response_body, "\n\n")
    # print("REFRESH_TOKEN_RESPONSE: \n", refresh_token_response_body, "\n\n")
    # print("CONTRACT_MASTER_RESPONSE: \n", contract_master_response_body, "\n\n")
    # print("LOGOUT_RESPONSE: \n", Logout_response_body, "\n\n")
    # print("PROFILE_RESPONSE: \n", profile_response_body, "\n\n")
    # print("FUNDS_RESPONSE: \n", funds_response_body, "\n\n")
    # print("PLACE_ORDER_RESPONSE: \n", place_order_response, "\n\n")
    # print("MODIFY_ORDER_RESPONSE: \n", modify_order_response, "\n\n")
    # print("CANCEL_ORDER_RESPONSE: \n", cancel_order_response, "\n\n")
    # print("EXIT_ORDER_RESPONSE: \n", exit_order_response, "\n\n")
    # print("BROKERAGE_RESPONSE: \n", brokerage_response_body, "\n\n")
    # print("MARGIN_CACULATOR_RESPONSE: \n", margin_calculator_response_body, "\n\n")
    # print("TRADE_BOOK_RESPONSE: \n", trade_book_response, "\n\n")
    # print("ORDER_BOOK_RESPONSE: \n", order_book_response, "\n\n")
    # print("ORDER_TRAIL_RESPONSE: \n", order_trail_response, "\n\n")
    # print("ORDER_STATUS_RESPONSE: \n", order_status_response, "\n\n")
    # print("POSITION_BOOK_RESPONSE: \n", position_book_response, "\n\n")
    # print("HOLDINGS_RESPONSE: \n", holdings_response, "\n\n")
    # print("CONVERT_POSITION_RESPONSE: \n", convert_position_response, "\n\n")
    # print("PROFIT_LOSS_CASH_REPORT_RESPONSE: \n", profit_loss_cash_report_response, "\n\n")
    # print("PROFIT_LOSS_FO_REPORT_RESPONSE: \n", profit_loss_fo_report_response, "\n\n")
    # print("HISTORICAL_DATA_RESPONSE: \n", historical_data_response, "\n\n")
    # print("INTRADAY_DATA_RESPONSE: \n", intraday_response, "\n\n")
