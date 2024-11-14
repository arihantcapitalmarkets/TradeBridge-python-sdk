from swagger_client.models.refresh_token_request import RefreshTokenRequest
from swagger_client.models.intraday_candle_data_request import IntradayCandleDataRequest, IntradayData
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
from swagger_client.api import ChartApi
from swagger_client.api import FundsApi
from swagger_client.api import LoginProfileApi
from swagger_client.models.login_request import LoginRequest
from swagger_client.models.get_profile_request import GetProfileRequest
from swagger_client.models.get_profile_request import GetProfileRequestData
from swagger_client.api import OrderControllerApi
from swagger_client.api import PositionControllerApi
from swagger_client.api import ProfitLossReportApi
from swagger_client.api import TradeBookApi
import attrs

# Login
loginAPI = LoginApi()
login_body = LoginRequest(userId="NEST8003",
                          password="Abcd@12341",
                          mobileNumber="9642229195")
api_key = "XNVFuVAF4ZTh39lVeH"
login_response_body = loginAPI.login_normal_login_post(login_body, api_key)[0]

# Access the accessToken and refreshToken
accessToken = attrs.asdict(login_response_body)["data"]["accessToken"]
refreshToken = attrs.asdict(login_response_body)["data"]["refreshToken"]

# # Refresh Token
# refreshTokenAPI = LoginApi()
# refresh_token_body = RefreshTokenRequest(refreshToken=refreshToken)
# refresh_token_response_body = refreshTokenAPI.refresh_token(refresh_token_body, accessToken, api_key)[0]
#
# # Get profile
# profileAPI = LoginProfileApi()
# profile_body = GetProfileRequest(data=GetProfileRequestData(),
#                                  appID="1")
# profile_response_body = profileAPI.get_profile(profile_body, accessToken, api_key)[0]
#
# # Get Funds
# fundsAPI = FundsApi()
# funds_response_body = fundsAPI.fund_view(accessToken, api_key)[0]
#
# Place Order
orderControllerAPI = OrderControllerApi()
place_order_body = body = PlaceOrderRequest(
    symbol="ACC-EQ",
    excToken="532540",
    ordAction=OrdActionEnum.BUY,
    ordValidity=OrdValidityEnum.DAY,
    ordType=OrdTypeEnum.MARKET,
    prdType=PrdTypeEnum.DELIVERY,
    qty=1,
    triggerPrice=0.0,
    limitPrice=0.0,
    disQty=0,
    instrument=InstrumentEnum.STK,
    exc=ExcEnum.NSE,
    lotSize=1,
    amo=False,
    build="MOB",
    boStpLoss=0,
    boTgtPrice=0,
    trailingSL=0.0
)

latitude = "5.66"
longitude = ""
place_order_response = \
    orderControllerAPI.place_order(place_order_body, accessToken, api_key, latitude, longitude)[0]
orderId = attrs.asdict(place_order_response)['data']['ordId']

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
#     symbol="ACC-EQ",
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
#     orderControllerAPI.modify_order(modify_order_body, accessToken, api_key, latitude, longitude)[0]
#
# # Cancel Order
# orderControllerAPI = OrderControllerApi()
# cancel_order_body = CancelOrderRequest(
#     symbol="ACC-EQ",
#     ordId=orderId,
#     exc=ExcEnum.NSE
# )
# latitude = ""
# longitude = "0.77"
# cancel_order_response = \
#     orderControllerAPI.cancel_order(cancel_order_body, accessToken, api_key, latitude, longitude)[0]
#
# # Exit Order
# orderControllerAPI = OrderControllerApi()
# exit_order_body = ExitOrderRequest(symbol="ACC-EQ",
#                                    boOrdStatus="complete",
#                                    ordId=orderId,
#                                    parOrdId=orderId,
#                                    exc=ExcEnum.NSE,
#                                    prdType=PrdTypeEnum.COVER_ORDER
#                                    )
# latitude = "3.22"
# longitude = "1.6666"
# exit_order_response = orderControllerAPI.exit_order(exit_order_body, accessToken, api_key, latitude, longitude)[
#     0]
#
# # BrokerageCharges
# orderControllerAPI = OrderControllerApi()
# brokerage_body = BrokerageChargeRequest(
#     symbol="STK_TCS_EQ_NSE",
#     exc=ExcEnum.NSE,
#     product=PrdTypeEnum.INTRADAY,
#     triggerPrice="",
#     price="3489.80",
#     qty="10000000",
#     instrument=InstrumentEnum.STK,
#     orderAction=OrdActionEnum.SELL,
#     excToken="11536",
#     orderType=OrdTypeEnum.MARKET
# )
# brokerage_response_body = \
#     orderControllerAPI.brokerage_charges(brokerage_body, accessToken, api_key)[0]
#
# # Trade Book
# tradeAPI = TradeBookApi()
# trade_book_response = tradeAPI.trade_book(accessToken, api_key)[0]
#
# # OrderBook
# tradeAPI = TradeBookApi()
# order_book_response = tradeAPI.get_order_book(accessToken, api_key)[0]
#
# # Order Trail
# tradeAPI = TradeBookApi()
# order_trail_body = OrderTrailRequest(
#     instrument=InstrumentEnum.STK,
#     ordId='241114000000020'
# )
# order_trail_response = tradeAPI.order_trail(order_trail_body, accessToken, api_key)[0]
#
# # Order Status
# tradeAPI = TradeBookApi()
# order_status_body = OrderTrailRequest(
#     instrument=InstrumentEnum.STK,
#     ordId="241114000000020"
# )
# order_status_response = tradeAPI.order_status(order_status_body, accessToken, api_key)[0]
#
# # Position Book
# positionControllerAPI = PositionControllerApi()
# position_book_response = positionControllerAPI.get_position_book("net", accessToken, api_key)[0]
#
# # Holdings
# positionControllerAPI = PositionControllerApi()
# holdings_response = positionControllerAPI.do_holdings(accessToken, api_key)[0]
#
# # ConvertPosition
# positionControllerAPI = PositionControllerApi()
# convert_position_body = ConvertPositionRequest(
#     exc=ExcEnum.BSE,
#     excToken="308",
#     instrument=InstrumentEnum.OPTSTK,
#     id="STK_BAJAJHIND_EQ_NSE",
#     qty=2589,
#     symbol="STK_BAJAJHIND_EQ_NSE",
#     lotSize=1,
#     ordAction=OrdActionEnum.SELL,
#     prdType=PrdTypeEnum.DELIVERY,
#     toPrdType=PrdTypeEnum.INTRADAY,
#     type="DAY1"
# )
# convert_position_response = positionControllerAPI.convert_position(convert_position_body, accessToken, api_key)[0]
#
# # Profit Loss Cash Report
# profitLossReport = ProfitLossReportApi()
# profit_loss_cash_report_body = ProfitLossCashReportRequest(filters=[
#     ReportFilters(key="date", value="02/10/2024-02/11/2024"),
#     ReportFilters(key="charges", value="incCharges")])
# profit_loss_cash_report_response = (
#     profitLossReport.profit_loss_cash_report(profit_loss_cash_report_body, accessToken, api_key))[0]
#
# # Profit Loss Fo report
# profitLossReport = ProfitLossReportApi()
# profit_loss_fo_report_body = ProfitLossFoReportRequest(filters=[
#     ReportFilters(key="date", value="21/02/2024-21/03/2024"),
#     ReportFilters(key="charges", value="incCharges"),
#     ReportFilters(key="exc", value="ALL"),
#     ReportFilters(key="finYear", value="2023-2024")
# ])
# profit_loss_fo_report_response = \
#     profitLossReport.profit_loss_fo_report(profit_loss_fo_report_body, accessToken, api_key)[0]
#
# # Historical Data
# chartAPI = ChartApi()
# historical_data_response = chartAPI.historical_data(accessToken, api_key, 'STK_INOXGREEN_BE_NSE',
#                                                     '1day',
#                                                     '2023-02-01T17:55:00.000',
#                                                     '2024-02-01T17:55:00.000',
#                                                     'STK',
#                                                     'NSE',
#                                                     '12193_NSE')[0]
#
# # Intraday Candle Data
# chartAPI = ChartApi()
# intraday_body = IntradayCandleDataRequest(data=IntradayData(
#     symbol="STK_JIOFIN_EQ_NSE",
#     resolution="1day",
#     exchange=ExcEnum.NSE,
#     instrument=InstrumentEnum.STK,
#     startTime="2024-09-02T00:00:00.000",
#     endTime="2024-09-02T15:00:00.000"
# ))
# intraday_response = chartAPI.intraday(intraday_body, accessToken, api_key)[0]

if __name__ == "__main__":
    print("\nLOGIN_RESPONSE: \n", login_response_body, "\n\n")
    # print("REFRESH_TOKEN_RESPONSE: \n", refresh_token_response_body, "\n\n")
    # print("PROFILE_RESPONSE: \n", profile_response_body, "\n\n")
    # print("FUNDS_RESPONSE: \n", funds_response_body, "\n\n")
    # print("PLACE_ORDER_RESPONSE: \n", place_order_response, "\n\n")
    # print("MODIFY_ORDER_RESPONSE: \n", modify_order_response, "\n\n")
    # print("CANCEL_ORDER_RESPONSE: \n", cancel_order_response, "\n\n")
    # print("EXIT_ORDER_RESPONSE: \n", exit_order_response, "\n\n")
    # print("BROKERAGE_RESPONSE: \n", brokerage_response_body, "\n\n")
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
