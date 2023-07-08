from Base import InitiateDriver
from Library import ConfigReader
from Library import ExcelReader
from Pages import Registration
from Library import ExcelWrite
from Base import Screenshot

driver = InitiateDriver.startbrowser()
def test_TC001_Validate_Registration():
    try:
        x = ExcelReader.readdatafromexcel(ConfigReader.readConfigdata("Excel_Data_Read_Path","signup_data_path"))
        Registration.registration(driver, x[0], x[1], x[2],"TC001_Validate_Registration")
        ExcelWrite.capture_tc_pass()
    except:
        ExcelWrite.capture_tc_failed()
    finally:
        print("Execution completed")




def test_TC002_Validate_Registration_Invaliddata():
    try:
        x = ExcelReader.readdatafromexcel(ConfigReader.readConfigdata("Excel_Data_Read_Path","signup_data_path"))
        Registration.registration(driver, x[0], x[1], x[2],"TC001_Validate_Registration")
        ExcelWrite.capture_tc_pass()
    except:
        ExcelWrite.capture_tc_failed()
    finally:
        print("Execution completed")
        InitiateDriver.closebrowser()

        # ***********Conguration file*******

        ###from configparser import ConfigParser
        ###config_obj = ConfigParser()
        ###config_obj.read("Configuration/config.cfg")
        ###config_obj.get("AccessWebsite","website_url")

        # ************Error Handling********

        ###try:
        ###    x = readdatafromexcel(config_obj.get("Excel_Data_Read_Path","signup_data_path"))
        ###    registernation(config_obj, x[0],x[1],x[2])
        ###except:
        ###    print("There is some error/exception in the code")
        ###finally:
        ###    print("Execution completed")

        # Capture Screenshot
        # Separate Page Class (POM)
        # Test Directory

        # Class & Inheritance, Polymorphism

        # Capture Logs

        # Pytest
        # Allure Reports