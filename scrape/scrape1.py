#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:08:38 2021

@author: mike
"""

import smtplib
from email.mime.text import MIMEText
import email_to
from urllib.request import urlopen
import re

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import datetime
import sys


def report(message = ''):
    timestamp = datetime.datetime.now()
    print(str(timestamp) + ' ' + str(message))



class Scrape:
    def __init__(self):
        self.__data = {}        
        self.__log_file = open('scrape.log', 'a')
        
        
    def run(self):
        self.log()
        self.log('running')
        while True:
            self.scrape()
            time.sleep(10)
        
        
    def log(self, message = '------------------------------------------'):
        timestamp = datetime.datetime.now()
        self.__log_file.write(str(timestamp) + ' ' + str(message) + "\n")
        self.__log_file.flush()



    def scrape(self):
      # https://realpython.com/python-web-scraping-practical-introduction/
        
      # courses of interest (empty list means check all courses)
      ucas_codes = []
      #ucas_codes = ['H401']
      #ucas_codes = ['HW73', 'H422', 'H401', 'H490', 'H491', '09F4']
      url = 'http://www.southampton.ac.uk/clearing/course-vacancies'
        
      #sys.stdout.flush()  
    
      self.log('scraping url: ' + url)
        
      try:
        response = requests.get(url)
        #soup = BeautifulSoup(response.text, 'html.parser')
        
        html = response.text
        text = re.sub('<[^<]+?>', '', html) # remove HTML tags        
        lines = re.sub('\t', '', text) # remove tabs
        
        prev_line = ''
        course_name = ''
        ucas_code = ''
        availability = ''

        for line in lines.splitlines():
          if not line.isspace() and line != '': # ignore blank or empty lines
                
            if prev_line == 'Course name:':
                course_name = line
            if prev_line == 'UCAS code:':
                ucas_code = line
            if prev_line == 'Availability:':
                availability = line
                    
            if line == 'Course name:': # start of next record
              #print(str(ucas_code) + ' | ' + str(course_name) + ' | ' + str(availability))
                    
              if ucas_code != '':
                        
                if not ucas_codes or ucas_code in ucas_codes:
                  saved_record = self.__data.get(ucas_code)
                  
                  if saved_record is not None:
                    saved_availability = saved_record.get('availability')
                            
                    if False:
                      self.log(str(ucas_code) + ' | ' + str(course_name) + ' | ' \
                           + str(availability) + ' | ' \
                           + str(saved_availability))
                    
                    # change in availability
                    if saved_availability != availability:
                      change_message = str(ucas_code) + ' ' \
                                     + str(course_name) \
                                     + ' - availability has changed from ' \
                                     + str(saved_availability) + ' to ' \
                                     + str(availability)
                      self.log(change_message)
                                
                      email_message = change_message + "\n\n" + url
                                
                      self.send_mail(change_message, email_message)
                    
              self.__data[ucas_code] = {'ucas_code': ucas_code, 
                                        'course_name': course_name, 
                                        'availability': availability}
              course_name = ''
              ucas_code = ''
              availability = ''
                    
            prev_line = line
       
      except OSError as err:
        print("OS error: {0}".format(err))
      except requests.exceptions.ConnectionError as err:
        print("Connection error: {0}".format(err))
        print("Connection error:", sys.exc_info()[0])
      except:
        print("Unexpected error:", sys.exc_info()[0])
          
          
          
    def send_mail(self, mail_to, subject, body):
        # https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python

        self.log('sending email to ' + str(mail_to))
        mail_from = 'Bing Bong<bing@bong.com>'
        
        msg = MIMEText(body)

        msg['Subject'] = subject
        msg['From'] = mail_from
        msg['To'] = mail_to
        
        server = smtplib.SMTP('smtp.dreamhost.com', 587)
        server.starttls()
        server.login('mike@stol.uk', 'Denverdog1')
        
        server.sendmail(mail_from, [mail_to], msg.as_string())
        server.quit()        
        
        self.log('sent')



    def send_mails(self, subject, body):
        mailing_list = ['mike@stollery.uk', 'mike2sheds@gmail.com', 'sandra@stollery.co.uk']
        
        for mail_to in mailing_list:
            self.send_mail(mail_to, subject, body)


    """
        
    def send_mail2(self):
        # https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python

        me = 'Bing Bong<bing@bong.com>'
        you = 'mike@stollery.uk'
        
        # Create a text/plain message
        msg = MIMEText('Test message 2')

        msg['Subject'] = 'Test Subject 2'
        msg['From'] = me
        msg['To'] = you

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        #server = smtplib.SMTP('localhost')
        
        server = smtplib.SMTP('smtp.dreamhost.com', 587)
        server.starttls()
        server.login('mike@stol.uk', 'Denverdog1')
        
        server.sendmail(me, [you], msg.as_string())
        server.quit()


    def send_mail3(self):
        # https://pypi.org/project/email-to/

        server = email_to.EmailServer('smtp.dreamhost.com', 587, 'mike@stol.uk', 'Denverdog1')

        message = server.message()
        message.add('This is a test message')

        message.send('mike@stollery.uk', 'This is a test email')


    def scrape1(self):
        # https://realpython.com/python-web-scraping-practical-introduction/
        print()
        print('scraping url: ' + self.__url)
        page = urlopen(self.__url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print(html)    
    """
    
    
if __name__ == "__main__":

    scrape = Scrape()
    #scrape.send_mails('Scrape test email', 'This is a test email for the web scraper.')
    scrape.run()
    
    