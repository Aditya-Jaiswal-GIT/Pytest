from TestData.test_data import valid_credential,invalid_credential
import requests
from Logs.log_file import get_logs

class LoginPage():
    def valid_credential(self):
        log = get_logs()
        flag = True
        try :
           
                    url = "https://restful-booker.herokuapp.com/auth"
                    r = requests.post(url,json=valid_credential)
                    if r.status_code!=200:
                        log.info(f"Status Code is : {r.status_code}")
                        flag = False
                    log.info("Status code is 200")
                    R = r.json()
                    if not R['token']:
                        log.info("Token is not present")
                        flag = False
                    log.info(f"Token : {R['token']}")
        except Exception as e:
              flag= False
              log.error(f"Error occured : {str(e)}")

        return flag


    