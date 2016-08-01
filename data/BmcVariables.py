#!/usr/bin/python

##
#    @file    Variables
#    @brief   Contains all the user inputs
#
#    @author  Anusha Dathatri
#
#    @date     July 14, 2016
##

class BmcVariables():

    OPENBMC_HOST = '<HOSTNAME>'
    OPENBMC_ID = '<USERID>'
    OPENBMC_PWD = '<PASSWORD>'
    IMG_PATH = '<PATH>'
    CURL_LOGIN_CMD = '<CMDTOLOGIN>'
    PRESERVE_IP_CMD = '<PRESERVE_CMD>'
    GET_STATUS_CMD = '<STATUS_CHECK_CMD>'
    REBOOT_CMD = '<REBOOT_CDM>'
    JENKINS_URL = '<RESOURCE_JENKINS_URL>'
    JENKINS_USER_ID = '<JENKINS_USER_ID>'
    JENKINS_PASSWORD = '<JENKINS_PWD>'
    BUILD_URL = 'https://openpower.xyz/job/openbmc-build/distro=ubuntu,target=barreleye/lastSuccessfulBuild/artifact/images/barreleye/'
    #BUILD_URL = 'https://openpower.xyz/job/openbmc-build/distro=ubuntu,target=palmetto/lastSuccessfulBuild/artifact/images/palmetto/'

    #Xpath
    SUBMIT_XPATH = "xpath=//button[@id='yui-gen1-button']"
    LOGIN_USER_XPATH = "xpath=//input[@name='j_username']"
    LOGIN_PASSWD_XPATH = "xpath=//input[@name='j_password']"
    SUBMIT_XPATH = "xpath=//button[@id='yui-gen1-button']"
    CELL_TABLE_XPATH = "xpath=//table[@class='pane']"



