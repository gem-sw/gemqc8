#!/usr/bin/env python
from datetime import datetime,date,time
from time import sleep
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
#import serial
import time
import xlrd
from xlrd import xldate
import re
import sys
#import statistics
from xmlConversion import generateXMLHeader, generateDataSetMultipleParts, writeToFile,writeToFile1
from xmlConversion import generateXMLDatafastamb,generateXMLDatafast,generateXMLDatalongamb,generateXMLDatalong, generateXMLData3,generateXMLData3a,generateXMLData4,generateXMLData4a,generateXMLData5a,generateXMLData5,generateXMLData4s, generateXMLData5s, generateXMLDataStrips, generateXMLDataStandGeoConf
#from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine, MetaData, Table, and_
#from sqlalchemy.sql import select


#QC5
def xml_from_excel5(excel_file):
	#wb = xlrd.open_workbook(excel_file)
	#sh = wb.sheet_by_index(0)
	user = sys.argv[3]
	location=sys.argv[2]
	Start=sys.argv[5]
	Stop=sys.argv[6]
        Run=sys.argv[7]
        ch1=sys.argv[8]
        ch2=sys.argv[9]
        ch3=sys.argv[10]
        ch4=sys.argv[11]
        ch5=sys.argv[12]
        ch6=sys.argv[13]
        ch7=sys.argv[14]
        ch8=sys.argv[15]
        ch9=sys.argv[16]
        ch10=sys.argv[17]
 	ch11=sys.argv[18]
        ch12=sys.argv[19]
        ch13=sys.argv[20]
        ch14=sys.argv[21]
        ch15=sys.argv[22]
        ch16=sys.argv[23]
        ch17=sys.argv[24]
        ch18=sys.argv[25]
        ch19=sys.argv[26]
        ch20=sys.argv[27]
 	ch21=sys.argv[28]
        ch22=sys.argv[29]
        ch23=sys.argv[30]
        ch24=sys.argv[31]
        ch25=sys.argv[32]
        ch26=sys.argv[33]
        ch27=sys.argv[34]
        ch28=sys.argv[35]
        ch29=sys.argv[36]
        ch30=sys.argv[37]

        flip2=sys.argv[38]
        flip4=sys.argv[39]
        flip6=sys.argv[40]
        flip8=sys.argv[41]
        flip10=sys.argv[42]
        flip12=sys.argv[43]
        flip14=sys.argv[44]
        flip16=sys.argv[45]
        flip18=sys.argv[46]
        flip20=sys.argv[47]
        flip22=sys.argv[48]
        flip24=sys.argv[49]
        flip26=sys.argv[50]
        flip28=sys.argv[51]
        flip30=sys.argv[52]

        flow2=sys.argv[53]
        flow4=sys.argv[54]
        flow6=sys.argv[55]
        flow8=sys.argv[56]
        flow10=sys.argv[57]
	flow12=sys.argv[58]
        flow14=sys.argv[59]
        flow16=sys.argv[60]
        flow18=sys.argv[61]
        flow20=sys.argv[62]
	flow22=sys.argv[63]
        flow24=sys.argv[64]
        flow26=sys.argv[65]
        flow28=sys.argv[66]
        flow30=sys.argv[67]
	comment=sys.argv[4]
	#type = "S"
	chamberCheck = "select"

	root = generateXMLHeader("QC8_GEM_STAND_GEOMETRY_CONF","GEM STAND GEOMETRY CONFIGURATION QC8", "GEOMETRY STAND CONFIGURATION",str(Run),str(Start),str(Stop),str(comment),str(location),str(user))
	dataSet = generateDataSetMultipleParts(root,comment,"1")
	if chamberCheck!= str(ch1):
		type = "L" if "-L" in str(ch1) else "S"
		generateXMLDataStandGeoConf(dataSet,str(ch1),'1/1/B',str(flow2),'11201',type,str(flip2),'2','2')
        if chamberCheck!= str(ch2):
	        type = "L" if "-L" in str(ch2) else "S"
		generateXMLDataStandGeoConf(dataSet,str(ch2),'1/1/T',str(flow2),'11101',type,str(flip2),'2','3')
	if chamberCheck!= str(ch3):
		type = "L" if "-L" in str(ch3) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch3),'2/1/B',str(flow4),'11203',type,str(flip4),'2','4')
        if chamberCheck!= str(ch4):
		type = "L" if "-L" in str(ch4) else "S"
        	generateXMLDataStandGeoConf(dataSet,str(ch4),'2/1/T',str(flow4),'11103',type,str(flip4),'2','5')
        if chamberCheck!= str(ch5):
	        type = "L" if "-L" in str(ch5) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch5),'3/1/B',str(flow6),'11205',type,str(flip6),'2','6')
        if chamberCheck!= str(ch6):
	        type = "L" if "-L" in str(ch6) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch6),'3/1/T',str(flow6),'11105',type,str(flip6),'2','7')
        if chamberCheck!= str(ch7):
	        type = "L" if "-L" in str(ch7) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch7),'4/1/B',str(flow8),'11207',type,str(flip8),'2','8')
        if chamberCheck!= str(ch8):
	        type = "L" if "-L" in str(ch8) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch8),'4/1/T',str(flow8),'11107',type,str(flip8),'2','9')
        if chamberCheck!= str(ch9):
	        type = "L" if "-L" in str(ch9) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch9),'5/1/B',str(flow10),'11209',type,str(flip10),'2','10')
        if chamberCheck!= str(ch10):
	        type = "L" if "-L" in str(ch10) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch10),'5/1/T',str(flow10),'11109',type,str(flip10),'2','11')
        if chamberCheck!= str(ch11):
	        type = "L" if "-L" in str(ch11) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch11),'1/2/B',str(flow12),'11211',type,str(flip12),'4','2')
        if chamberCheck!= str(ch12):
	        type = "L" if "-L" in str(ch12) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch12),'1/2/T',str(flow12),'11111',type,str(flip12),'4','3')
        if chamberCheck!= str(ch13):
	        type = "L" if "-L" in str(ch13) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch13),'2/2/B',str(flow14),'11213',type,str(flip14),'4','4')
        if chamberCheck!= str(ch14):
	        type = "L" if "-L" in str(ch14) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch14),'2/2/T',str(flow14),'11113',type,str(flip14),'4','5')
        if chamberCheck!= str(ch15):
	        type = "L" if "-L" in str(ch15) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch15),'3/2/B',str(flow16),'11215',type,str(flip16),'4','6')
        if chamberCheck!= str(ch16):
        	type = "L" if "-L" in str(ch16) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch16),'3/2/T',str(flow16),'11115',type,str(flip16),'4','7')
        if chamberCheck!= str(ch17):
	        type = "L" if "-L" in str(ch17) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch17),'4/2/B',str(flow18),'11217',type,str(flip18),'4','8')
        if chamberCheck!= str(ch18):
	        type = "L" if "-L" in str(ch18) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch18),'4/2/T',str(flow18),'11117',type,str(flip18),'4','9')
        if chamberCheck!= str(ch19):
	        type = "L" if "-L" in str(ch19) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch19),'5/2/B',str(flow20),'11219',type,str(flip20),'4','10')
        if chamberCheck!= str(ch20):
	        type = "L" if "-L" in str(ch20) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch20),'5/2/T',str(flow20),'11119',type,str(flip20),'4','11')
        if chamberCheck!= str(ch21):
	        type = "L" if "-L" in str(ch21) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch21),'1/3/B',str(flow22),'11221',type,str(flip22),'6','2')
        if chamberCheck!= str(ch22):
	        type = "L" if "-L" in str(ch22) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch22),'1/3/T',str(flow22),'11121',type,str(flip22),'6','3')
        if chamberCheck!= str(ch23):
	        type = "L" if "-L" in str(ch23) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch23),'2/3/B',str(flow24),'11223',type,str(flip24),'6','4')
        if chamberCheck!= str(ch24):
	        type = "L" if "-L" in str(ch24) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch24),'2/3/T',str(flow24),'11123',type,str(flip24),'6','5')
        if chamberCheck!= str(ch25):
	        type = "L" if "-L" in str(ch25) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch25),'3/3/B',str(flow26),'11225',type,str(flip26),'6','6')
        if chamberCheck!= str(ch26):
	        type = "L" if "-L" in str(ch26) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch26),'3/3/T',str(flow26),'11125',type,str(flip26),'6','7')
        if chamberCheck!= str(ch27):
	        type = "L" if "-L" in str(ch27) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch27),'4/3/B',str(flow28),'11227',type,str(flip28),'6','8')
        if chamberCheck!= str(ch28):
	        type = "L" if "-L" in str(ch28) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch28),'4/3/T',str(flow28),'11127',type,str(flip28),'6','9')
        if chamberCheck!= str(ch29):
	        type = "L" if "-L" in str(ch29) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch29),'5/3/B',str(flow30),'11229',type,str(flip30),'6','10')
        if chamberCheck!= str(ch30):
	        type = "L" if "-L" in str(ch30) else "S"
	        generateXMLDataStandGeoConf(dataSet,str(ch30),'5/3/T',str(flow30),'11129',type,str(flip30),'6','11')
	writeToFile(fileName, tostring(root))
if __name__ =="__main__":	
	#fname=raw_input("Enter excel data file name:")
	fname = sys.argv[1]
	fileName=fname+".xml"
#	datafile=fname+"_Data.xml"
#	testfile=fname+"_summry.xml"
	xml_from_excel5(fname)
