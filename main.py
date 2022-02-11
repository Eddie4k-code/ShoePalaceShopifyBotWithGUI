from tkinter import *
from tkinter import ttk
import tkinter as tk
from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.options import Options

root = tk.Tk()
root.title('ShoePalace AutoCheckout')
root.geometry('1000x500')

main = ttk.Notebook(root)
main.pack()



#chrome_options = Options()                  #Creates a headless browser if you want activated
#chrome_options.add_argument("--headless")


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH) #chrome_options= chrome_options)



def add_to_cart(cart):

    cart = driver.find_element_by_class_name("productForm-buttons")
    cart.click()


def checkout(out):
    driver.get("https://www.shoepalace.com/checkout")







def get_product(keyword_entry):

    #Step 1 Look for Keywords
    product = driver.get(f"https://www.shoepalace.com/search?q={keyword_entry}")
    response_label['text'] = 'Searching for product'
    while True:

        #Step 2 Grab product and select it
        select = driver.find_element_by_class_name("spf-product-card__inner")
        select.click()






        time.sleep(1)

        try:        #Add the product to cart
            response_label['text'] = 'Adding Product To Cart'
            time.sleep(1)
            add_to_cart('cart')

        except:
            response_label['text'] = 'Cannot Add to Cart'
            break

        time.sleep(1)

        try:        #Go to checkout Page
            response_label['text'] = 'Attempting to hit Checkout'
            time.sleep(1)
            checkout('out')
        except:
            response_label['text'] = 'Cannot Checkout'
            break


        def go():

            # Billing Info
            email = f'{email_entry.get()}'
            first_name = f'{first_name_entry.get()}'
            last_name = f'{last_name_entry.get()}'
            address = f'{addy_entry.get()}'
            city = f'{city_entry.get()}'
            #country = f'{country_entry.get()}'
            state = f'{state_entry.get()}'
            phone = f'{phone_entry.get()}'
            zip_code = f'{zipcode_entry.get()}'

            # Payment Info
            credit = f'{credit_entry.get()}'
            name_card = f'{card_name_entry.get()}'
            exp_date = f'{exp_month_entry.get()}'
            exp_date2 = f'{exp_year_entry.get()}'
            ssn = f'{ssn_entry.get()}'

            response_label['text'] = 'Filling Shipping information'

            email_grab = driver.find_element_by_name("checkout[email]")
            email_grab.send_keys(email)

            # First Name
            first_name_grab = driver.find_element_by_name("checkout[shipping_address][first_name]")
            first_name_grab.send_keys(first_name)

            # Last Name
            last_name_grab = driver.find_element_by_name("checkout[shipping_address][last_name]")
            last_name_grab.send_keys(last_name)

            # Address
            address_grab = driver.find_element_by_name("checkout[shipping_address][address1]")
            address_grab.send_keys(address)

            # City
            city_grab = driver.find_element_by_name("checkout[shipping_address][city]")
            city_grab.send_keys(city)

            # Country
            #country_grab = driver.find_element_by_name("checkout[shipping_address][country]")
            #country_grab.send_keys(country)

            # State
            state_grab = driver.find_element_by_name("checkout[shipping_address][province]")
            state_grab.send_keys(state)

            # ZIP CODE
            zip_grab = driver.find_element_by_name("checkout[shipping_address][zip]")
            zip_grab.send_keys(zip_code)

            # Phone
            phone_grab = driver.find_element_by_name("checkout[shipping_address][phone]")
            phone_grab.send_keys(phone)

            # terms
            terms = driver.find_element_by_name("checkout[attributes][I agree to the Terms and Conditions]")
            terms.click()

            # Continue
            cont = driver.find_element_by_id("continue_button")
            cont.click()

            # Contine to paymet
            cont_payment = driver.find_element_by_id("continue_button")
            cont_payment.click()

            response_label['text'] = 'Submitting Payment Information'

            time.sleep(3)

            # Credit Card / Debit Card
            cc_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]').send_keys(credit)



            # Name on card
            name_card_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Name on card"]')
            name_card_grab.send_keys(name_card)


            # Exp date
            exp_date_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Expiration date (MM / YY)"]')
            exp_date_grab.send_keys(exp_date)
            exp_date_grab.send_keys(exp_date2)

            # Security Code
            ssn_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Security code"]')
            ssn_grab.send_keys(ssn)

            # Submit Payment
            response_label['text'] = 'Hitting Submit Payment'
            time.sleep(2)

            try:
                payment = driver.find_element_by_id("continue_button")
                payment.click()
            except:
                response_label['text'] = 'Payment error'

            time.sleep(6)

            try:
                driver.find_elements_by_class_name("notice__text")
                response_label['text'] = 'Payment Failed, Invalid Payment Information.'
            except:
                response_label['text'] = 'Payment Success'

        go()

def quit():
    root.quit()


'''
GUI GUI GUI GUI GUI
'''
ShoePalace = tk.Frame(main, width=1000, height=600, bg='gray')
billing = tk.Frame(main, width=1000, height=600, bg='gray')

ShoePalace.pack(fill='both', expand=1)
billing.pack(fill='both', expand=1)

main.add(ShoePalace, text='ShoePalace')
main.add(billing, text='Billing Info')

#Canvas Size of Program
canvas = tk.Canvas(root, height=600, width=1000)
canvas.pack()

#Frame
frame = tk.Frame(ShoePalace, bg='white', bd=5)
frame.place(relx=0.3,rely=0.2, relwidth=4, relheight=0.1, anchor='s')


#Enter KeyWords Label
keywords_label = tk.Label(frame, bg='white', text='Keywords: ', font=40)
keywords_label.place(relwidth=1, relheight=1)


#KeyWord Entry
keyword_entry = tk.Entry(keywords_label, font=40, bg='white')
keyword_entry.place(relx=0.51, rely=0.40, relwidth=0.10)


#Response Label
response_label = tk.Label(ShoePalace, bg='gray', bd=5)
response_label.place(relwidth=0.55, relheight=0.50, relx=0.28, rely=0.30)

#Start Task Button
task_btn = tk.Button(ShoePalace, text='Start Task', bg='white', font=40, command= lambda: get_product(keyword_entry.get()))
task_btn.place(relx=0.28, rely=0.80, relwidth=0.3)

#Quit Button
quit_btn = tk.Button(ShoePalace, text='Quit', bg='white', font=40, command=quit)
quit_btn.place(relx=0.60, rely=0.80,relwidth=0.2)

#Email Label
email_label = tk.Label(billing, bg='white', text='Email')
email_label.place(relx=0.10, rely=0.10, relwidth=0.10)

#Email Entry
email_entry = tk.Entry(billing)
email_entry.place(relx=0.22, rely=0.10)

#First Name Label
first_name_label = tk.Label(billing, bg='white', text='First Name')
first_name_label.place(relx=0.10, rely=0.15, relwidth=0.10)

#First Name Entry
first_name_entry = tk.Entry(billing, bg='white', text='Last Name')
first_name_entry.place(relx=0.22, rely=0.15)

#last name label
last_name_label = tk.Label(billing, bg='white', text='Last Name')
last_name_label.place(relx=0.10, rely=0.20, relwidth=.10)

#Last Name Entry
last_name_entry = tk.Entry(billing, bg='white')
last_name_entry.place(relx=0.22, rely=0.20)

#Address Label
addy_label = tk.Label(billing, bg='white', text='Address')
addy_label.place(relx=0.10, rely=0.25, relwidth=.10)

#Address Entry
addy_entry = tk.Entry(billing, bg='white')
addy_entry.place(relx=0.22, rely=0.25)

#City Label
city_label = tk.Label(billing, bg='white', text='City')
city_label.place(relx=0.10,rely=.30, relwidth=.10)

#City Entry
city_entry = tk.Entry(billing, bg='white')
city_entry.place(relx=0.22, rely=0.30)

#Country Label
Country_label = tk.Label(billing, bg='white', text='Country')
Country_label.place(relx=0.10, rely=0.35, relwidth=0.10)

#Country Entry
#country_entry = tk.Entry(billing, bg='white')
#country_entry.place(relx=0.22, rely=0.35)

#State Label
state_label = tk.Label(billing, bg='white', text='State')
state_label.place(relx=0.10, rely=0.35, relwidth=0.10)

#State Entry
state_entry = tk.Entry(billing, bg='white')
state_entry.place(relx=0.22, rely=0.35)

#Zip Code Label
zipcode_label = tk.Label(billing, bg='white', text='Zip Code')
zipcode_label.place(relx=0.10, rely=0.40, relwidth=0.10)

#Zip Code Entry
zipcode_entry = tk.Entry(billing, bg='white')
zipcode_entry.place(relx=0.22, rely=0.40)

#Phone Label
phone_label = tk.Label(billing, bg='white', text='Cell Phone')
phone_label.place(relx=0.10, rely=0.45, relwidth=0.10)

#Phone Entry
phone_entry = tk.Entry(billing, bg='white')
phone_entry.place(relx=0.22, rely=0.45)

#Credit Card Label
credit_label = tk.Label(billing, bg='white', text='Card Number')
credit_label.place(relx=0.10, rely=0.50, relwidth=0.10)

#Credit Card Entry
credit_entry = tk.Entry(billing, bg='white')
credit_entry.place(relx=0.22, rely=0.50)


#Name On Card Label
card_name_label = tk.Label(billing, bg='white', text='Card Name')
card_name_label.place(relx=0.10, rely=0.55, relwidth=0.10)

#Name on card Entry
card_name_entry = tk.Entry(billing, bg='white')
card_name_entry.place(relx=0.22, rely=0.55)

#Expiration Month Label
exp_month_label = tk.Label(billing, bg='white', text='Exp Month')
exp_month_label.place(relx=0.10, rely=0.60, relwidth=0.10)

#Exp Month Entry
exp_month_entry = tk.Entry(billing, bg='white')
exp_month_entry.place(relx=0.22, rely=0.60)

#Exp Year Label
exp_year_label = tk.Label(billing, bg='white', text='Exp Year')
exp_year_label.place(relx=0.10, rely=0.65, relwidth=0.10)

#Exp Year Entry
exp_year_entry = tk.Entry(billing, bg='white')
exp_year_entry.place(relx=0.22, rely=0.65)

#SSN Label
ssn_label = tk.Label(billing, bg='white', text='SSN')
ssn_label.place(relx=0.10, rely=0.70, relwidth=0.10)

#SSN Entry
ssn_entry = tk.Entry(billing, bg='white')
ssn_entry.place(relx=0.22, rely=0.70)




root.mainloop()
driver.quit()
