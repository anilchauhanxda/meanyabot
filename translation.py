class Translation(object):
    START_TEXT = """Hi! there bish
bsdk yeah private use key ley hia nikla ab pahli furshat main.
Agar tunney mera use kiya toh terey telegram ki gand maar lungi bsdk.
Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """I see!
bsdk ab OTP send kr.


/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@meanii"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"