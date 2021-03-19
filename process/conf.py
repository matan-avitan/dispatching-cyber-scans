class Conf(object):
    BASE_API_URL = r"http://127.0.0.1:8080/db-api/"
    GET_NEW_REQ_URL = r'scans/'
    UPDATE_SCAN_STATUS_URL = r'scan/'

    LOOP_INTERVAL = 10
    LOOP_PRIORITY = 1

    COMPLETE_STATUS = "Complete"
    ERROR_STATUS = "Error"
